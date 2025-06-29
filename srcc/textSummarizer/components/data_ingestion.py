from srcc.textSummarizer.entity import DataIngestionConfig
import urllib.request as request
import zipfile
from srcc.textSummarizer.logging import logger
import os

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} has been downloaded successfully")
        else:
            logger.info(f"File already exists")
    
    def unzip_file(self):
        unzip_dir = self.config.unzip_dir
        os.makedirs(unzip_dir, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, "r") as file:
            file.extractall(unzip_dir)