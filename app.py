# app.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("CORD-19 Research Dataset Explorer 📊")

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("metadata.csv")

df = load_data()

st.subheader("Dataset Overview")
st.write(df.head())

# Clean data
df = df.dropna(subset=["title", "abstract"])
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Sidebar filter
year_filter = st.sidebar.slider("Select Year", int(df["publish_time"].dt.year.min()), int(df["publish_time"].dt.year.max()), int(df["publish_time"].dt.year.min()))
filtered_df = df[df["publish_time"].dt.year == year_filter]

st.subheader(f"Papers Published in {year_filter}")
st.write(filtered_df[["title", "journal", "authors"]].head(10))

# Visualization: Publications per year
st.subheader("📈 Publications Over Time")
pubs_per_year = df["publish_time"].dt.year.value_counts().sort_index()
fig, ax = plt.subplots()
pubs_per_year.plot(kind="line", marker="o", ax=ax)
ax.set_xlabel("Year")
ax.set_ylabel("Number of Papers")
st.pyplot(fig)

# Top journals
st.subheader("🏛 Top Journals")
top_journals = df["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(x=top_journals.values, y=top_journals.index, palette="viridis", ax=ax)
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)
