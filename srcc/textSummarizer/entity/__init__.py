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