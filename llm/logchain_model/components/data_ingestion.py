import os
import zipfile
import gdown
from llm.logchain_model import logger
from llm.logchain_model.utils.common import get_size
from llm.logchain_model.entity.entity_config import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self)-> str:
        """ Download the data from google drive """
        try: 
            dataset_url = self.config.source_URL
            download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Start downloading data from {dataset_url} into file {download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id,download_dir)

            logger.info(f"End download data from {dataset_url} into file {download_dir}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

