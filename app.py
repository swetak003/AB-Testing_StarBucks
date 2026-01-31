from src.__main__.logger import logging
from src.__main__.exceptions import CustomException
from src.__main__.components.data_ingestion import DataIngestion

import sys

if __name__ == "__main__":
    logging.info("Application started.")
    try:
        # Main application logic goes here
        logging.info("Performing some operations...")

        ingestion=DataIngestion()
        train_data,test_data=ingestion.initiate_data_ingestion()

        # Simulate an operation that could raise an exception
        print("Training Shape:", train_data.shape)
        print("Test Shape:", test_data.shape)

        logging.info("Data ingestion completed successfully")

    except Exception as e:
        logging.error("Application failed")
        raise CustomException(e, sys)
