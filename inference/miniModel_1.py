import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
from peft import PeftModel

# === Paths ===
base_model_path = "../Models/Qwen3-0.6B-Base"         # pretrained Qwen
adapter_path = "../Models/qwen3_lora_adapter"         # fine-tuned LoRA adapter

# === Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(adapter_path, trust_remote_code=True)

# === Load base model (4-bit quantized for memory efficiency)
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
)

base_model = AutoModelForCausalLM.from_pretrained(
    base_model_path,
    device_map="auto",
    trust_remote_code=True,
    quantization_config=bnb_config
)

# === Load LoRA adapter into the base model
model = PeftModel.from_pretrained(base_model, adapter_path)
model.eval()

# === Example prompt
prompt = "Ingredients: rice, chicken, soy sauce. Recipe:"

# === Tokenize input
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

# === Generate random, creative output
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=1.0,
        top_p=0.95,
        top_k=50,
        repetition_penalty=1.1,
        pad_token_id=tokenizer.eos_token_id,
    )

# === Decode and print output
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

