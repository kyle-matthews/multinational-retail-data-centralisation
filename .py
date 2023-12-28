import pandas as pd

df = pd.read_csv('extracted_store_data.csv')
unique_store_types = df['store_type'].unique()

print(unique_store_types)
