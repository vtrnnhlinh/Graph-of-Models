import pandas as pd

# Load CSV
df = pd.read_csv("datasets/dataset_1/vegetables.csv", encoding="latin1")
# Save as Parquet
df.to_parquet("datasets/dataset_1/vegetables.parquet", engine="pyarrow", index=False)
