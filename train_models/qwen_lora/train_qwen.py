import os
import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    BitsAndBytesConfig,
    TrainingArguments,
    Trainer,
)
from peft import get_peft_model, LoraConfig, TaskType
from datasets import load_dataset, concatenate_datasets

# === 1. Paths ===
model_path = "../../Models/Qwen3-0.6B-Base"
data_dir = "../../datasets/dataset_1/"

# === 2. Load tokenizer and model in 4-bit ===
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    trust_remote_code=True,
    quantization_config=bnb_config
)

# === 3. Apply LoRA ===
peft_config = LoraConfig(
    r=8,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type=TaskType.CAUSAL_LM
)
model = get_peft_model(model, peft_config)

# === 4. Load all .parquet files manually and keep only 'ingredients' column ===
all_datasets = []
for filename in os.listdir(data_dir):
    if filename.endswith(".parquet"):
        path = os.path.join(data_dir, filename)
        ds = load_dataset("parquet", data_files=path, split="train")
        ds = ds.filter(lambda x: x.get("ingredients") is not None)
        ds = ds.remove_columns([col for col in ds.column_names if col != "ingredients"])
        all_datasets.append(ds)

dataset = concatenate_datasets(all_datasets)

# === 5. Tokenize and add labels ===

def tokenize(example):
    prompt = f"Ingredients: {example['ingredients']}\nRecipe:"
    target = example.get("directions", "")  # or "" if no target

    full_input = prompt + target

    # Tokenize full input once
    tokens = tokenizer(
        full_input,
        padding="max_length",
        truncation=True,
        max_length=256
    )

    # Identify the target portion offset
    target_start = len(tokenizer(prompt, truncation=True, max_length=256)["input_ids"])
    
    # Set labels: ignore tokens before the start of target
    labels = [-100] * target_start + tokens["input_ids"][target_start:]
    labels += [-100] * (256 - len(labels))  # pad to 256
    labels = labels[:256]  # truncate just in case

    tokens["labels"] = labels
    return tokens


tokenized = dataset.map(tokenize, batched=False)
tokenized.set_format(type='torch', columns=["input_ids", "attention_mask", "labels"])

# === 6. TrainingArguments ===
training_args = TrainingArguments(
    output_dir="../../Models/qwen3_lora",
    per_device_train_batch_size=1,
    num_train_epochs=16,
    logging_steps=10,
    save_strategy="epoch",
    fp16=False,
    bf16=True,
    report_to="none",
)
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    tokenizer=tokenizer,
)

# === 8. Train ===
torch.cuda.empty_cache()
torch.cuda.reset_peak_memory_stats()
trainer.train()
model.save_pretrained("../../Models/qwen3_lora_adapter")  # Save only the adapter
tokenizer.save_pretrained("../../Models/qwen3_lora_adapter")

