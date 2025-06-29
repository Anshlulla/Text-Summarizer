import os

from src.components import data_ingestion
from srcc.textSummarizer.logging import logger
from srcc.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Starting stage: {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e