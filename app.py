import logging
import sys

from mlproject.components.data_ingestion import DataIngestion
from mlproject.exception import CustomException

if __name__ == "__main__":
    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

        logging.info("Data ingestion is completed")

    except Exception as e:
        raise CustomException(e)