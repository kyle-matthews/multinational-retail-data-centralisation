import pandas as pd
import re


class DataCleaning:
    def clean_user_data(self, df):
        """
        The function `clean_user_data` takes a DataFrame as input, removes nonsense values, cleans the phone
        number and join date columns, converts the date of birth and join date columns to datetime format,
        drops rows with missing values, and replaces 'GGB' with 'GB' in the country code column.

        :param df: The parameter `df` is a pandas DataFrame that contains user data
        """
        # Aiming for 15284 rows
        # Remove nonsense values
        print("OG df" + str(len(df)))
        df = self.remove_nonsense(df)
        print("removed nonsense " + str(len(df)))
        # Reset index
        #
        df = df.reset_index(drop=True)
        df = df[df.first_name != "NULL"]
        # Clean phone number column
        df.loc[:, "phone_number"] = df.loc[:, "phone_number"].str.replace(
            r"^(?:\(\+\d+\))|\D", "", regex=True
        )
        print("replacing non digit in phone number " + str(len(df)))

        # Convert date_of_birth and join_date to datetime format
        df.loc[:, "date_of_birth"] = df.loc[:, "date_of_birth"].apply(
            pd.to_datetime, errors="ignore"
        )
        print("DOB datetime " + str(len(df)))
        df.loc[:, "join_date"] = df.loc[:, "join_date"].apply(
            pd.to_datetime, errors="ignore"
        )
        print("Join date Datetime " + str(len(df)))

        # Replace 'GGB' with 'GB' in country_code column
        df.loc[:, "country_code"] = (
            df.loc[:, "country_code"]
            .astype(str)
            .apply(lambda x: x.replace("GGB", "GB"))
        )
        print("Edit GGB to GB " + str(len(df)))

        df = df.dropna(how="all", subset=["user_uuid"])
        print("dropna " + str(len(df)))

        return df

    def clean_card_data(self, df):
        """
        The function `clean_card_data` removes rows with missing values in the 'card_number' and
        'expiration_date' columns, converts the 'card_number' column to numeric type, and converts the
        'expiration_date' column to datetime type.
        :param df: The parameter `df` is a pandas DataFrame that contains card data
        """
        card_list = [
            "Diners Club / Carte Blanche",
            "American Express",
            "JCB 16 digit",
            "JCB 15 digit",
            "Maestro",
            "Mastercard",
            "Discover",
            "VISA 19 digit",
            "VISA 16 digit",
            "VISA 13 digit",
        ]
        df = df.dropna(how="all")
        df = df[df["card_provider"].isin(card_list)]
        df.loc[:, "card_number"] = (
            df.loc[:, "card_number"].astype(str).apply(lambda x: x.replace("?", ""))
        )
        df = df.reset_index(drop=True)
        df["card_number"] = df["card_number"].apply(pd.to_numeric, errors="coerce")

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
        store_type = ["Web Portal", "Local", "Super Store", "Mall Kiosk", "Outlet"]
        df = df[df["store_type"].isin(store_type)]
        df = df.dropna(how="all")
        df.loc[:, "longitude"] = pd.to_numeric(df.loc[:, "longitude"], errors="coerce")
        df.loc[:, "latitude"] = pd.to_numeric(df.loc[:, "latitude"], errors="coerce")
        df.loc[:, "staff_numbers"] = df.loc[:, "staff_numbers"].str.replace(
            r"^(?:\(\+\d+\))|\D", "", regex=True
        )
        df.loc[:, "opening_date"] = pd.to_datetime(
            df.loc[:, "opening_date"].astype(str), format="mixed", errors="coerce"
        )
        df = df.drop(["lat"], axis=1)

        df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

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
        clean_df = clean_df.dropna(subset=["weight"])
        clean_df.loc[:, "weight"] = clean_df.loc[:, "weight"].str.strip(".")
        clean_df.loc[:, "date_added"] = pd.to_datetime(
            clean_df.loc[:, "date_added"].astype(str), format="mixed", errors="coerce"
        )

        clean_df.loc[:, "weight"] = clean_df.loc[:, "weight"].apply(
            lambda x: x.replace("g", "")
        )
        print("g replaced")

        clean_df.loc[:, "weight"] = clean_df.loc[:, "weight"].apply(
            lambda x: x.replace("ml", "")
        )
        print("ml replaced")

        # This method of cleaning the oz's might break something
        clean_df.loc[:, "weight"] = clean_df.loc[:, "weight"].apply(
            lambda x: x.replace("oz", "")
        )
        print("ml replaced")

        clean_df.loc[:, "weight"] = clean_df.loc[:, "weight"].str.replace(
            r"^[0-9]+\sx\s+[0-9]+$", "", regex=True
        )
        clean_df.replace("", 0, inplace=True)
        print("x gone")

        clean_df.loc[:, "weight"] = (
            clean_df.loc[:, "weight"]
            .astype(str)
            .apply(lambda x: float(x) / 1000 if "k" not in x else x)
        )

        clean_df.loc[:, "weight"] = (
            clean_df.loc[:, "weight"].astype("str").apply(lambda x: x.replace("k", ""))
        )

        return clean_df

    def convert_weight(self, value):
        """
        The function `convert_weight` converts a weight value to a numeric format by removing any non-digit
        characters.

        :param value: The `value` parameter is the weight value that needs to be converted
        :return: the numeric value of the input `value` after removing any non-digit characters. If the
        input `value` is `NaN` (not a number), it will return `NaN` itself.
        """
        if pd.notna(value):
            return pd.to_numeric(re.sub(r"\D", "", str(value)))
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
        df.replace(r"^[A-Z0-9]{8,10}$", None, inplace=True, regex=True)
        return df

        """
        The function `drop_columns` is used to drop a specified column from a DataFrame in Python.
        
        :param df: The dataframe on which you want to drop columns
        :param column_name: The column_name parameter is the name of the column that you want to drop from
        the DataFrame
        """

        """def drop_columns(self, df, column_name):
        df.drop(column_name, axis=1, inplace=True)
        return df"""

    def clean_orders_data(self, df):
        """
        The function `clean_orders_data` takes a DataFrame as input, creates a copy of it, removes nonsense
        values, drops specific columns, drops rows with missing values in certain columns, and returns the
        cleaned DataFrame.

        :param df: The parameter `df` is a pandas DataFrame that contains the orders data
        :return: the cleaned dataframe, `clean_df`.
        """
        # Create a copy of the DataFrame
        # Drop specific columns
        df = df.drop(["level_0", "1", "first_name", "last_name"], axis=1)
        # Remove nonsense values
        df = self.remove_nonsense(df)

        # Drop rows with missing values in specified columns
        # clean_df = clean_df.dropna(subset=['first_name', 'last_name', '1'])

        return df

    def clean_date_times(self, df):
        df = self.remove_nonsense(df)
        df["month"] = pd.to_numeric(df["month"], errors="coerce")
        df["year"] = pd.to_numeric(df["year"], errors="coerce")
        df["day"] = pd.to_numeric(df["day"], errors="coerce")
        df = df.dropna()

        return df
