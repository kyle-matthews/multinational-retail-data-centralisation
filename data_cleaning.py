import pandas as pd
from dateutil.parser import parse
import re
import numpy as np


class DataCleaning:

    def clean_user_data(self, df):
        """
        The function `clean_user_data` cleans the user data by dropping missing values, converting the
        'date_column' to datetime format, and converting the 'numeric_column' to numeric format.
        """
        df = df.dropna()
        df = self.remove_nonsense(df)
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
        df = self.remove_nonsense(df)
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
        """
        The `clean_product_weights` function takes a DataFrame as input, removes nonsense values, drops rows
        with missing weight values, cleans the weight column by removing units and special characters, and
        returns the cleaned DataFrame.
        
        :param df: The `df` parameter is a pandas DataFrame that contains product data
        :return: the cleaned dataframe, `clean_df`.
        """
        clean_df = df.copy()
        self.remove_nonsense(clean_df)
        clean_df = clean_df.dropna(subset=['weight'])
        clean_df.loc[:, 'weight'] = clean_df.loc[:, 'weight'].str.strip('.')
        
        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].apply(lambda x: x.replace('g', ''))
        print('g replaced')

        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].apply(lambda x: x.replace('ml', ''))
        print('ml replaced')
        
        #This method of cleaning the oz's might break something
        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].apply(lambda x: x.replace('oz', ''))
        print('ml replaced')

        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].str.replace(r'^[0-9]+\sx\s+[0-9]+$', '', regex=True)
        clean_df.replace('', np.nan, inplace=True)
        print('x gone')

        clean_df.loc[:, 'weight'] = clean_df.loc[:, 'weight'].astype(str).apply(lambda x: float(x) /1000 if 'k' not in x else x)

        clean_df.loc[:,'weight'] = clean_df.loc[:,'weight'].astype('str').apply(lambda x: x.replace('k', ''))


        return clean_df
    

    def convert_weight(self,value):
        """
        The function `convert_weight` converts a weight value to a numeric format by removing any non-digit
        characters.
        
        :param value: The `value` parameter is the weight value that needs to be converted
        :return: the numeric value of the input `value` after removing any non-digit characters. If the
        input `value` is `NaN` (not a number), it will return `NaN` itself.
        """
        if pd.notna(value):
            return pd.to_numeric(re.sub(r'\D', '', str(value)))
        else:
            return value
        
    def remove_nonsense(self, df):
        """
        The function removes any values in the dataframe that consist of 8 to 10 uppercase letters or
        digits.
        
        :param df: The parameter `df` is a pandas DataFrame object
        :return: the modified dataframe after removing the rows that match the specified regular expression
        pattern.
        """
        df.replace(r'^[A-Z0-9]{8,10}$', None, regex=True, inplace=True)
        return df