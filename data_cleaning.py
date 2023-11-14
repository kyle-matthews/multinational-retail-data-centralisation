import pandas as pd
import numpy as np
class DataCleaning:

    def clean_user_data(self, df):
        """
        The `clean_user_data` function cleans and filters a user's data by handling null values, parsing
        dates, converting columns to numeric, and filtering rows based on a condition.
        :return: The `clean_user_data` function returns the `user_data` DataFrame after performing various
        cleaning operations on it.
        """
        self.handle_null_values()
        self.parse_dates()
        self.convert_to_numeric()
        self.filter_wrong_rows()

        return self.user_data

    def handle_null_values(self):
        self.user_data.fillna(method='ffill', inplace=True)

    def parse_dates(self):
        self.user_data['date_column'] = pd.to_datetime(self.user_data['date_column'], errors='coerce')

    def convert_to_numeric(self):
        self.user_data['numeric_column'] = pd.to_numeric(self.user_data['numeric_column'], errors='coerce')

    def filter_wrong_rows(self):
        self.user_data = self.user_data[self.user_data['condition_column'] == 'desired_condition']

        return self.user_data