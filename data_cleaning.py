import pandas as pd
from dateutil.parser import parse
import re
import numpy as np


class DataCleaning:

    def clean_user_data(self, df):
        """
        The function `clean_user_data` takes a DataFrame as input, removes nonsense values, cleans the phone
        number and join date columns, converts the date of birth and join date columns to datetime format,
        drops rows with missing values, and replaces 'GGB' with 'GB' in the country code column.
        
        :param df: The parameter `df` is a pandas DataFrame that contains user data
        """
        
        # Remove nonsense values
        df = self.remove_nonsense(df)
        
        # Reset index
        df = df.reset_index(drop=True)
        
        # Clean phone number column
        df['phone_number'] = df['phone_number'].str.replace(r'^(?:\(\+\d+\))|\D', '', regex=True)
        df['join_date'] = df['join_date'].str.replace(r'^(?:\(\+\d+\))|\D', '', regex=True)
        
        # Convert date_of_birth and join_date to datetime format
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'].astype(str), format='mixed', errors='coerce')
        df['join_date'] = pd.to_datetime(df['join_date'].astype(str), format='mixed', errors='coerce')
        
        # Drop rows with missing values in specified columns
        df.dropna(subset=['date_of_birth', 'country_code'], inplace=True)
        
        # Replace 'GGB' with 'GB' in country_code column
        df['country_code'] = df['country_code'].apply(lambda x: x.replace('GGB', 'GB'))
        
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

        df = self.remove_nonsense(df)
        df = df.dropna(subset=['address', 'latitude', 'longitude'])
        df.loc[:, 'longitude'] = pd.to_numeric(df.loc[:, 'longitude'], errors='coerce')
        df.loc[:, 'latitude'] = pd.to_numeric(df.loc[:,'latitude'], errors='coerce')
        df.loc[:, 'staff_numbers'] = df.loc[:,'staff_numbers'].str.replace(r'^(?:\(\+\d+\))|\D', '', regex=True)
        df.loc[:, 'opening_date'] = pd.to_datetime(df.loc[:, 'opening_date'].astype(str), format='mixed', errors='coerce')
        df = df.drop(['lat'], axis=1)
        df = df[df['address'].str.len() > 5]
        df = df.drop_duplicates(subset=['address', 'latitude', 'longitude'], keep='first')
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
        clean_df.columns = clean_df.columns.str.lower()
        clean_df = self.remove_nonsense(clean_df)
        clean_df = clean_df.dropna(subset=['weight'])
        clean_df.loc[:, 'weight'] = clean_df.loc[:, 'weight'].str.strip('.')
        clean_df.loc[:, 'date_added'] = pd.to_datetime(clean_df.loc[:, 'date_added'].astype(str), format='mixed', errors='coerce')
        
        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].apply(lambda x: x.replace('g', ''))
        print('g replaced')

        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].apply(lambda x: x.replace('ml', ''))
        print('ml replaced')
        
        #This method of cleaning the oz's might break something
        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].apply(lambda x: x.replace('oz', ''))
        print('ml replaced')

        clean_df.loc[:, 'weight'] = clean_df.loc[:,'weight'].str.replace(r'^[0-9]+\sx\s+[0-9]+$', '', regex=True)
        clean_df.replace('', 0, inplace=True)
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
    
        """
        The function `drop_columns` is used to drop a specified column from a DataFrame in Python.
        
        :param df: The dataframe on which you want to drop columns
        :param column_name: The column_name parameter is the name of the column that you want to drop from
        the DataFrame
        """
    def drop_columns(self, df, column_name):
        df = df.drop(column_name, inplace=False, axis=1)
        return df

    def clean_orders_data(self, df):
        """
        The function `clean_orders_data` takes a DataFrame as input, creates a copy of it, removes nonsense
        values, drops specific columns, drops rows with missing values in certain columns, and returns the
        cleaned DataFrame.
        
        :param df: The parameter `df` is a pandas DataFrame that contains the orders data
        :return: the cleaned dataframe, `clean_df`.
        """
        # Create a copy of the DataFrame
        clean_df = df.copy()
        # Remove nonsense values
        clean_df = self.remove_nonsense(clean_df)
        # Drop specific columns
        clean_df = self.drop_columns(clean_df, 'first_name')
        clean_df = self.drop_columns(clean_df, 'last_name')
        clean_df = self.drop_columns(clean_df, '1')
        # Drop rows with missing values in specified columns
        #clean_df = clean_df.dropna(subset=['first_name', 'last_name', '1'])
        
        return clean_df
    
    def clean_date_times(self, df):
        """
        The function `clean_date_times` takes a DataFrame as input, removes nonsense values, drops any rows
        with missing values, converts the 'month', 'year', 'day', and 'timestamp' columns to their
        appropriate data types, and returns the cleaned DataFrame.
        
        :param df: The parameter `df` is a pandas DataFrame that contains date and time information
        :return: the original dataframe `df`, not the cleaned dataframe `clean_df`.
        """
        clean_df = df.copy()
        clean_df = self.remove_nonsense(clean_df)
        clean_df = clean_df.dropna()
        clean_df['month'] = pd.to_numeric(clean_df['month'], errors='coerce')
        clean_df['year'] = pd.to_numeric(clean_df['year'], errors='coerce')
        clean_df['day'] = pd.to_numeric(clean_df['day'], errors='coerce')
        clean_df['timestamp'] = pd.to_datetime(clean_df['timestamp'], format='%H:%M:%S', errors='coerce')
        return df
