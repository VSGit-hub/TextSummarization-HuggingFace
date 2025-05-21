from src.textsummarizer.entity import DataTransformationConfig
from src.textsummarizer.config.configuration import ConfigurationManager
from src.textsummarizer.components.data_transfromation import DataTransformation

class DataIngestionTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_tranformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transfromation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.convert()
        
