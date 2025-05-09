import os
import sys
from src.exception import CustomException  # Custom exception handling
from src.logger import logging  # Logging utility

import pandas as pd  # Data manipulation library
from sklearn.model_selection import train_test_split  # For splitting data into train/test
from dataclasses import dataclass  # To create simple data container classes


# Data class for storing configuration paths for data ingestion
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')  # Path for train data
    test_data_path: str = os.path.join('artifacts', 'test.csv')    # Path for test data
    raw_data_path: str = os.path.join('artifacts', 'data.csv')    # Path for raw data


class DataIngestion:
    def __init__(self):
        # Initialize configuration object
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the CSV file from the specified location
            df = pd.read_csv("C:/Users/Dell/Desktop/ML Project/notebook/data/student_data.csv")
            logging.info("Read the dataset")

            # Create directory for artifacts if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save the raw dataset to the raw data path
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Log and split dataset into train and test sets
            logging.info("Train Test Split Initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test datasets to their respective paths
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")
            # Return paths to the saved train and test data
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Handle exceptions with CustomException
            raise CustomException(e, sys)


if __name__ == '__main__':
    # Instantiate DataIngestion class and run data ingestion process
    obj = DataIngestion()
    obj.initiate_data_ingestion()