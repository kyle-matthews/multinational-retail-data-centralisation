import pandas as pd
from dateutil.parser import parse
import re


class DataCleaning:

    def clean_user_data(self, df):
        """
        The function `clean_user_data` cleans the user data by dropping missing values, converting the
        'date_column' to datetime format, and converting the 'numeric_column' to numeric format.
        """
        df = df.dropna()
        df = df.drop_duplicates(subset=['index'], keep='first')
        df = df.reset_index(drop=True)
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce', yearfirst=True, format='mixed')
        df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce', yearfirst=True, format='mixed')
        df['phone_number'] = df['phone_number'].str.replace(r'^(?:\(\+\d+\))|\D', '', regex=True)

        return df
    
    def clean_card_data(self, df):
        """
        The function `clean_card_data` removes rows with missing values in the 'card_number' and
        'expiration_date' columns, converts the 'card_number' column to numeric type, and converts the
        'expiration_date' column to datetime type.
        :param df: The parameter `df` is a pandas DataFrame that contains card data
        """
        df = df.dropna()
        
        df = df.reset_index(drop=True)
        
        df['card_number'] = pd.to_numeric(df['card_number'], errors='coerce')
        df["date_payment_confirmed"] = df["date_payment_confirmed"].apply(lambda x: parse(x))
        df['expiry_date'] = pd.to_datetime(df['expiry_date'], errors='ignore', format='%m%y')
        return df
    
    def clean_store_data(self, df):
        """
        The function `clean_store_data` takes a DataFrame as input and performs various cleaning operations
        on it, including converting certain columns to numeric and datetime types, dropping rows with
        missing values in specific columns, dropping a column, removing rows with addresses shorter than 5
        characters, dropping duplicate rows based on specific columns, and resetting the index of the
        DataFrame.
        
        :param df: The parameter `df` is a pandas DataFrame that contains store data
        :return: the cleaned and filtered dataframe.
        """
        df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
        df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
        df['staff_numbers'] = pd.to_numeric(df['staff_numbers'], errors='coerce')
        df['opening_date'] = pd.to_datetime(df['opening_date'], errors='coerce', yearfirst=True, format='mixed')
        
        df = df.dropna(subset=['address', 'latitude', 'longitude'])
        df = df.drop(['lat'], axis=1)
        df = df[df['address'].str.len() > 5]
        df = df.drop_duplicates(subset=['address', 'latitude', 'longitude'], keep='first')
        df = df[(df['latitude'] >= -90) & (df['latitude'] <= 90) & (df['longitude'] >= -180) & (df['longitude'] <= 180)]
        df = df.reset_index(drop=True)

        return df
    
    def clean_product_weights(self, df):
        clean_df = df.copy()
        df = df.dropna()

        def convert_weight(value):
            return pd.to_numeric(re.sub(r'\D', '', value))

        for index, value in enumerate(df['weight']):
            if 'kg' in value:
                clean_df.at[index, 'weight'] = convert_weight(value)
            elif 'g' in value or 'ml' in value:
                clean_df.at[index, 'weight'] = convert_weight(value) / 1000
            else:
                clean_df.at[index,'weight'] = convert_weight(value)

        return clean_df