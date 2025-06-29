from srcc.textSummarizer.config.configuration import ConfigurationManager
from srcc.textSummarizer.components.data_transformation import DataTransformation
from srcc.textSummarizer.logging import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()