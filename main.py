import os

from src.components import data_ingestion
from srcc.textSummarizer.logging import logger
from srcc.textSummarizer.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from srcc.textSummarizer.pipeline.data_transformation_pipeline import DataTransformationPipeline
from srcc.textSummarizer.pipeline.model_trainer_pipeling import ModelTrainerPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f"Starting stage: {STAGE_NAME}")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f"Starting stage: {STAGE_NAME}")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.initiate_data_transformation()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Training Stage"
try:
    logger.info(f"Starting stage: {STAGE_NAME}")
    model_trainer_pipeline = ModelTrainerPipeline()
    model_trainer_pipeline.initiate_model_training()
    logger.info(f"{STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e
