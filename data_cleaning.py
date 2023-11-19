import pandas as pd


class DataCleaning:

    def clean_user_data(self, df):
        """
        The function `clean_user_data` cleans the user data by dropping missing values, converting the
        'date_column' to datetime format, and converting the 'numeric_column' to numeric format.
        """
        clean_df = df.dropna()
        
        clean_df = df.drop_duplicates(subset=['index'], keep='first')
        clean_df = clean_df.reset_index(drop=True)
        clean_df['date_of_birth'] = pd.to_datetime(clean_df['date_of_birth'], errors='coerce', yearfirst=True, format='mixed')
        clean_df['join_date'] = pd.to_datetime(clean_df['join_date'], errors='coerce', yearfirst=True, format='mixed')
        clean_df['phone_number'] = clean_df['phone_number'].str.replace(r'^(?:\(\+\d+\))|\D', '', regex=True)

        return clean_df