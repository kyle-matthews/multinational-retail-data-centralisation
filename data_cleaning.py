import pandas as pd
import numpy as np
class DataCleaning:
    def clean_user_data(self, user_data):
        """
        The function `clean_user_data` cleans a DataFrame by dropping rows with missing values in the 'date'
        and 'age' columns.
        
        :param user_data: The `user_data` parameter is a pandas DataFrame that contains user data. It is
        assumed that the DataFrame has columns named 'date' and 'age'. The 'date' column is expected to
        contain date values, and the 'age' column is expected to contain numeric age values
        :return: the cleaned user data, which is a pandas DataFrame.
        """
        user_data = user_data.dropna()

        user_data['date'] = pd.to_datetime(user_data['date'], errors='coerce')
        user_data = user_data.dropna(subset=['date'])

        user_data['age'] = pd.to_numeric(user_data['age'], errors='coerce')
        user_data = user_data.dropna(subset=['age'])

        return user_data