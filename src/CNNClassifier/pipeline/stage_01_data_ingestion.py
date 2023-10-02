from CNNClassifier.config import ConfigurationManager
from CNNClassifier.components import DataIngestion
from CNNClassifier import logging

STAGE_NAME = "Data Ingestion Stage"

logging.info("Data Ingestion Stage Started")

config = ConfigurationManager() 
data_ingestion_config=config.get_data_ingestion_config()
data_ingestion = DataIngestion(config=data_ingestion_config)
data_ingestion.download_file()
data_ingestion.unzip_and_clean()

logging.info("Data Ingestion completed")