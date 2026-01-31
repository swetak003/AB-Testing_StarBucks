####JAI GANEHAY NAMAH
import sys
import pandas as pd
from src.__main__.logger import logging
from src.__main__.exceptions import CustomException


class DataTransformation:
    """
    Handles data cleaning and preparation for Starbucks A/B testing.
    Converts raw ingested data into analysis-ready format.
    """

    def __init__(self):
        logging.info("DataTransformation initialized")

    def transform(self, train_df: pd.DataFrame, test_df: pd.DataFrame):
        """
        Transformation steps:
        1. Validate required columns
        2. Select relevant columns
        3. Handle missing values
        4. Map categorical values to binary
        5. Enforce data types
        6. Validate binary data integrity
        """
        try:
            logging.info("Starting data transformation")

            # -------------------------------------------------
            # 1. Validate required columns
            # -------------------------------------------------
            required_columns = ["promotion", "purchase"]

            for col in required_columns:
                if col not in train_df.columns:
                    raise CustomException(
                        f"Missing required column in training data: {col}", sys
                    )
                if col not in test_df.columns:
                    raise CustomException(
                        f"Missing required column in test data: {col}", sys
                    )

            logging.info("Required columns validated")

            # -------------------------------------------------
            # 2. Select required columns only
            # -------------------------------------------------
            train_df = train_df[required_columns].copy()
            test_df = test_df[required_columns].copy()

            logging.info("Selected required columns")

            # -------------------------------------------------
            # 3. Handle missing values
            # -------------------------------------------------
            train_df.dropna(inplace=True)
            test_df.dropna(inplace=True)

            logging.info("Missing values removed")

            # -------------------------------------------------
            # 4. Map categorical values to binary
            # -------------------------------------------------
            binary_mapping = {
                "Yes": 1,
                "No": 0,
                "Y": 1,
                "N": 0,
                "True": 1,
                "False": 0,
                True: 1,
                False: 0,
                1: 1,
                0: 0
            }

            train_df["promotion"] = train_df["promotion"].map(binary_mapping)
            train_df["purchase"] = train_df["purchase"].map(binary_mapping)

            test_df["promotion"] = test_df["promotion"].map(binary_mapping)
            test_df["purchase"] = test_df["purchase"].map(binary_mapping)

            logging.info("Categorical values mapped to binary")

            # -------------------------------------------------
            # 5. Remove rows with unmapped values
            # -------------------------------------------------
            train_df.dropna(inplace=True)
            test_df.dropna(inplace=True)

            logging.info("Invalid categorical rows removed")

            # -------------------------------------------------
            # 6. Enforce integer type
            # -------------------------------------------------
            train_df["promotion"] = train_df["promotion"].astype(int)
            train_df["purchase"] = train_df["purchase"].astype(int)

            test_df["promotion"] = test_df["promotion"].astype(int)
            test_df["purchase"] = test_df["purchase"].astype(int)

            logging.info("Binary conversion completed")

            # -------------------------------------------------
            # 7. Validate binary integrity
            # -------------------------------------------------
            valid_values = {0, 1}

            if not set(train_df["promotion"].unique()).issubset(valid_values):
                raise CustomException(
                    "Invalid values found in promotion column (train)", sys
                )

            if not set(train_df["purchase"].unique()).issubset(valid_values):
                raise CustomException(
                    "Invalid values found in purchase column (train)", sys
                )

            if not set(test_df["promotion"].unique()).issubset(valid_values):
                raise CustomException(
                    "Invalid values found in promotion column (test)", sys
                )

            if not set(test_df["purchase"].unique()).issubset(valid_values):
                raise CustomException(
                    "Invalid values found in purchase column (test)", sys
                )

            logging.info("Binary value validation successful")

            # -------------------------------------------------
            # 8. Log final shapes
            # -------------------------------------------------
            logging.info(f"Final training shape: {train_df.shape}")
            logging.info(f"Final test shape: {test_df.shape}")

            logging.info("Data transformation completed successfully")

            return train_df, test_df

        except Exception as e:
            logging.error("Error occurred during data transformation")
            raise CustomException(e, sys)
