import pandas as pd


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
    
        df = df.dropna(subset=['card_number', 'expiration_date'])

        df['card_number'] = pd.to_numeric(df['card_number'], errors='coerce')

        df = df.dropna(subset=['card_number'])

        df['expiration_date'] = pd.to_datetime(df['expiration_date'], errors='coerce')

        df = df.dropna(subset=['expiration_date'])