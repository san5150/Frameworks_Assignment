# analysis.py

import pandas as pd

# Load dataset
df = pd.read_csv("metadata.csv")

# Preview first 5 rows
print("\nFirst 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Missing values
print("\nMissing values per column (top 10):")
print(df.isnull().sum().head(10))

# Drop rows with missing title/abstract
df = df.dropna(subset=["title", "abstract"])
print("\nAfter cleaning, shape:", df.shape)

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Publications per year
pubs_per_year = df["publish_time"].dt.year.value_counts().sort_index()
print("\nPublications per year:")
print(pubs_per_year)

# Top 10 journals
top_journals = df["journal"].value_counts().head(10)
print("\nTop 10 Journals:")
print(top_journals)
