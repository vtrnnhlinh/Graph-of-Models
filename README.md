# Graph-of-Models
My work on LLM

---

## Setup

### Setup conda environment

```bash
conda env create -f environment.yml
conda activate Graph-of-Models
```

### Process datasets <reworking>

Remember to change the directory of `.csv` input files to `.parquet` output files. We need to convert 3 dataset files of `dataset_1`.

Download link of `datasets` is in file `README.md` of `datasets` folder.

```bash
python datasets/csv_to_parquet.py
```

### Merge datasets to calculate the relevant score

- Run the `general_preprocess.ipynb` of `edges_calculation` folder.

## Current structure

```
<Reworking>
```
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

### In-Action

> The implementation or everything related to the code here.

- [Graph-of-Models - a journey of a thousand miles begins with a single step](https://vtrnnhlinh.github.io/blog/2025/gom-action-0/)

## Acknowledgements

This section I express my gratitute to my mentor - Mr. Truong, my friend - Dr. [Arthur](https://github.com/Aethor) and BGSV for making this comes true.
