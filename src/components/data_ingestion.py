import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException  # Ensure this file exists in src/exception.py
from src.logger import logging  # Ensure this file exists in src/logger.py

from src.components.data_transformation import DataTransformation  # Ensure this exists
from src.components.data_transformation import DataTransformationConfig  # Unused, can be removed

@dataclass
class DataIngestionConfig:
    """
    Configuration class that holds file paths for data ingestion outputs.
    """
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'data.csv')


class DataIngestion:
    """
    Class to handle reading raw data and splitting it into training and testing sets.
    """

    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads the raw dataset, saves it, and splits it into training and testing datasets.
        Returns:
            Tuple[str, str]: Paths to train and test datasets.
        """
        logging.info("Entered the data ingestion method/component")

        try:
            df = pd.read_csv("C:/Users/Dell/Desktop/ML Project/notebook/data/student_data.csv")
            logging.info("Dataset loaded successfully")

            # Ensure artifact directory exists
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved to {self.ingestion_config.raw_data_path}")

            # Split the data
            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test sets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info(f"Train and test data saved to {self.ingestion_config.train_data_path} and {self.ingestion_config.test_data_path}")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            logging.error("Error occurred during data ingestion", exc_info=True)
            raise CustomException(e, sys)


if __name__ == '__main__':
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    # Trigger data transformation after ingestion
    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data, test_data)
