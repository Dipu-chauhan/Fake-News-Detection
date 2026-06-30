import pandas as pd


# Load files (IMPORTANT: data folder)
fake_df = pd.read_csv("data/Fake.csv")
true_df = pd.read_csv("data/True.csv")

# Labels
fake_df["label"] = 0
true_df["label"] = 1


# Merge datasets
data = pd.concat([fake_df, true_df], ignore_index=True)

# Shuffle dataset
data = data.sample(frac=1).reset_index(drop=True)

# Check
print(data.head())
print(data.shape)