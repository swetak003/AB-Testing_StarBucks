import os
import sys
import pandas as pd
from src.__main__.logger import logging
from src.__main__.exceptions import CustomException


class DataIngestion:
    def __init__(self):
        try:
            # Get project root directory
            self.base_dir = os.getcwd()

            # DATA folder path
            self.data_dir = os.path.join(self.base_dir, "DATA")

            # File paths
            self.train_data_path = os.path.join(self.data_dir, "Training.csv")
            self.test_data_path = os.path.join(self.data_dir, "Test.csv")

            logging.info("DataIngestion initialized successfully")
            logging.info(f"Training file path: {self.train_data_path}")
            logging.info(f"Test file path: {self.test_data_path}")

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self):
        try:
            logging.info("Started data ingestion")

            # Load CSV files
            train_df = pd.read_csv(self.train_data_path)
            test_df = pd.read_csv(self.test_data_path)

            logging.info("Training and Test data loaded")

            # Standardize column names
            train_df.columns = train_df.columns.str.lower().str.strip()
            test_df.columns = test_df.columns.str.lower().str.strip()

            logging.info("Column names standardized")

            return train_df, test_df

        except Exception as e:
            logging.error("Data ingestion failed")
            raise CustomException(e, sys)
