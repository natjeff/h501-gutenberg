import pandas as pd
#Load datasets and confirm the authors info
gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
gutenberg_languages = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
gutenberg_subjects = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')
gutenberg_authors.info()


# Load necessary datasets
authors_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
metadata_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"

authors = pd.read_csv(authors_url)
metadata = pd.read_csv(metadata_url)

# Count translations per gutenberg_author_id
translation_counts = (
    metadata.groupby("gutenberg_author_id")["language"]
    .count()
    .reset_index(name="translation_count")
)

# Merge with authors to get aliases
merged = authors.merge(translation_counts, on="gutenberg_author_id", how="inner")

# Remove messy/empty aliases
merged = merged[merged["alias"].notna() & (merged["alias"].str.strip() != "")]

# Sort by translation count
merged = merged.sort_values("translation_count", ascending=False)

# Final list of aliases
author_aliases_sorted = merged["alias"].tolist()

print(author_aliases_sorted[:20])  # show the first 20 most translated
