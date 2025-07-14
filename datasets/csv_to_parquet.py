import pandas as pd

# fruits.parquet
df1_fruits = pd.read_parquet("../datasets/dataset_1/fruits.parquet")
df1_fruits = df1_fruits.rename(columns={"fruit": "ingredients"})
df1_fruits.to_parquet("../datasets/dataset_1/fruits.parquet")
# vegetables_seafood.parquet
df1_vegetables_seafood = pd.read_parquet("../datasets/dataset_1/vegetables_seafood.parquet")
df1_vegetables_seafood = df1_vegetables_seafood.rename(columns={"Food and Serving": "ingredients"})
df1_vegetables_seafood.to_parquet("../datasets/dataset_1/vegetables_seafood.parquet")
# vegetables.parquet
df1_vegetables = pd.read_parquet("../datasets/dataset_1/vegetables.parquet")
df1_vegetables = df1_vegetables.rename(columns={"Name": "ingredients"})
df1_vegetables.to_parquet("../datasets/dataset_1/vegetables.parquet")
