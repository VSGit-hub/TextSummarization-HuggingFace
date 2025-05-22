from src.textsummarizer.logging import logger
from src.textsummarizer.pipeline.stage_1_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.textsummarizer.pipeline.stage_2_data_transformation_pipeline import DataIngestionTransformationPipeline
from src.textsummarizer.pipeline.stage_3_model_trainer_pipeline import ModelTrainerPipeline
from src.textsummarizer.pipeline.steage_4_model_evaluation_piepline import ModelEvaluationTrainingPipeline

# STAGE_NAME="DATA INGESTION STAGE"

# try:
#     logger.info(f"stage {STAGE_NAME} initiated")
#     data_ingestion_pipeline=DataIngestionTrainingPipeline()
#     data_ingestion_pipeline.initiate_data_ingestion()
#     logger.info(f"Stage {STAGE_NAME} Completed")
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME="DATA TRANSFORMATION STAGE"

# try:
#     logger.info(f"STAGE {STAGE_NAME} STARTED")
#     data_transformation_pipeline = DataIngestionTransformationPipeline()
#     data_transformation_pipeline.initiate_data_tranformation()
#     logger.info(f"STAGE {STAGE_NAME} COMPLETED")
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME="MODEL TRAINING STAGE"

# try:
#     logger.info(f"STAGE {STAGE_NAME} STARTED")
#     model_trainer = ModelTrainerPipeline()
#     model_trainer.initiate_model_trainer()
#     logger.info(f"STAGE {STAGE_NAME} COMPLETED")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "MODEL EVALUATION STAGE"
try:
    logger.info(f"STAGE {STAGE_NAME} STARTED")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f"STAGE {STAGE_NAME} COMPLETED")
except Exception as e:
        logger.exception(e)
        raise e
