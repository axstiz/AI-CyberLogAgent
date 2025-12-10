import os
from pathlib import Path

class LogManageSettings:
    """Settings for log management.

    Attributes:
        logs_path (str): Path to the analyse_logs directory.
        logs_file (str): Name of the log file.
        logs_file_path (str): Full path to the log file.
        logs_file_size (int): Maximum size of the log file in bytes.
        gigachat_api_key (str): API key for GIGACHAT service.

    """

    def __init__(self):
        """Initialize LogManageSettings with default values."""
        self.logs_path = "RAG_data"
        self.logs_file = "analyse_logs.txt"
        self.logs_file_path = f"{self.logs_path}/{self.logs_file}"
        self.logs_file_size = 10000000  # 10 MB
        
# Load environment variables from .env file
env_path = Path(__file__).parent / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):  # Skip empty lines and comments
                key, value = line.split("=", 1)
                os.environ[key] = value

GIGACHAT_API_KEY = os.getenv("GIGACHAT_API_KEY")
