import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = 'week2.csv'
OUTPUT_DIR = 'plots'
COLUMN = 'government_consideration'

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(DATA_FILE)
counts = df[COLUMN].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(counts.index.astype(str), counts.values, color='steelblue')
ax.set_title('Government Consideration Response Counts')
ax.set_xlabel('Government Consideration')
ax.set_ylabel('Count')
plt.xticks(rotation=20, ha='right')
plt.tight_layout()

out_path = os.path.join(OUTPUT_DIR, 'government_consideration_bar.png')
plt.savefig(out_path, dpi=150)
plt.close()

print(f'Saved plot to: {out_path}')
