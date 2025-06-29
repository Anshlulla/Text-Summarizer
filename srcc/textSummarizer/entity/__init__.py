from pathlib import Path
from dataclasses import dataclass
from srcc.textSummarizer.logging import logger

@dataclass
class DataIngestionConfig:
  root_dir: Path
  source_URL: Path
  local_data_file: Path
  unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: int
    logging_steps: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path