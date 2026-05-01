import logging
import sys

from mlproject.components.data_ingestion import DataIngestion
from mlproject.components.data_transformation import DataTransformaiton
from mlproject.components.model_tranier import ModelTrainer
from mlproject.exception import CustomException

if __name__ == "__main__":
    try:
        data_ingestion = DataIngestion()
        train_path, test_path = data_ingestion.initiate_data_ingestion()

        data_tranformation = DataTransformaiton()
        train_arr, test_arr, _= data_tranformation.initiate_data_transformation(train_path, test_path)

        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(train_arr, test_arr)

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e, sys)