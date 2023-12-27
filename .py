import pandas as pd

df = pd.read_csv('extracted_payment_data.csv')
unique_cards = df['card_provider'].unique()

print(unique_cards)