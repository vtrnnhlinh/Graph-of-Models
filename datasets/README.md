## Datasets

Unable to upload full datasets due to heavy files, I will provide the information of datasets used to train here.

All data will be keep as `.parquet` files. Code to convert files from `.csv` to `.parquet` is provided.

### Structure

Expected structure will look like something below:

```
├── datasets
│   ├── csv_to_parquet.py
│   ├── dataset_1
│   │   ├── fruits.parquet
│   │   ├── vegetables.parquet
│   │   └── vegetables_seafood.parquet
│   ├── dataset_2
│   │   ├── all-recipes_0.parquet
│   │   ├── all-recipes_1.parquet
│   │   ├── all-recipes_2.parquet
│   │   ├── all-recipes_3.parquet
│   │   └── recipe_nlg.parquet
│   └── dataset_3
│       └── cocktail_recipes.parquet
```

### miniModel_1

This model is fine-tuned by fruits and vegetables nutritions informations.

Kaggle Links, don't have them now :>

### dataset_2

This model is fine-tuned by cooking recipes.

- [Recipe NLG](https://recipenlg.cs.put.poznan.pl/dataset)
- [all-recipes](https://huggingface.co/datasets/corbt/all-recipes)

### miniModel_3

This model is fine-tuned by cocktail recipes.

- [cocktail_recipes](https://huggingface.co/datasets/brianarbuckle/cocktail_recipes)
