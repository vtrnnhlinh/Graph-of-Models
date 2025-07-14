# Graph-of-Models
My work on LLM

---

## Setup

### Setup conda environment

```bash
conda env create -f environment.yml
conda activate Graph-of-Models
```

### Process datasets

Remember to change the directory of `.csv` input files to `.parquet` output files. We need to convert 3 dataset files of `dataset_1`.

Download link of `datasets` is in file `README.md` of `datasets` folder.

```bash
python datasets/csv_to_parquet.py
```

### Merge datasets to calculate the relevant score

- Run the `general_preprocess.ipynb` of `edges_calculation` folder.

## Current structure

│   environment.yml
│   LICENSE
│   README.md
│
├───datasets
│   │   csv_to_parquet.py
│   │   dataset_1.parquet
│   │   dataset_2.parquet
│   │   dataset_3.parquet
│   │
│   ├───dataset_1
│   │       fruits.parquet
│   │       vegetables.parquet
│   │       vegetables_seafood.parquet
│   │
│   ├───dataset_2
│   │       all-recipes_0.parquet
│   │       all-recipes_1.parquet
│   │       all-recipes_2.parquet
│   │       all-recipes_3.parquet
│   │       recipe_nlg.parquet
│   │
│   └───dataset_3
│           cocktail_recipes.parquet
│
├───edges_calculation
│   │   general_preprocess.ipynb
│   │
│   ├───cosine_similarity
│   │   │   cosine_calculate.ipynb
│   │   │   cosine_preprocess.ipynb
│   │   │
│   │   └───results
│   │           avg_cosine_similarity_matrix.csv
│   │
│   └───jaccard_index
└───graph_visualization
    ├───cosine_similarity
    │       cosine_graph.ipynb
    │
    └───jaccard_index

## My blog posts

The collection of posts I wrote while doing this project

### Literature Review

> This part has the posts I wrote about the works I researched and read about to develop my own work.

- [Graph-of-Models - Literature Review 1 - Transformer and MoH](https://vtrnnhlinh.github.io/blog/2025/gom-literature-review-0/)
- [Graph-of-Models - Literature Review 2 - GaCLLM](https://vtrnnhlinh.github.io/blog/2025/gom-literature-review-1/)
- [Graph-of-Models - Literature Review 3 - and they call LLM and KG](https://vtrnnhlinh.github.io/blog/2025/gom-literature-review-2/)

### Design Ideas

> The figures, diagrams and most vague ideas will be shared here.

- [Graph-of-Models - First Sketch](https://vtrnnhlinh.github.io/blog/2025/gom-design-0/)
