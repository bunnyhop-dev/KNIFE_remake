import logging
from datetime import datetime
from pathlib import Path
from typing import Dict

class ScanLogger:
    def __init__(self, log_file: str = "scanner.log"):
        self.log_file = Path(log_file)
        self._setup_logger()

    def _setup_logger(self):
        """Set up logging configuration"""
        logging.basicConfig(
                filename=self.log_file,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                level=logging.INFO
                )
        self.logger = logging.getLogger("NetworkScanner")

    def log_scan_start(self, target: str):
        """Log scan start event"""
        self.logger.info(f"Starting scan of {target}")

    def log_scan_result(self, target: str, result: Dict):
        """Log scan results"""
        self.logger.info(f"Scan completed for {target}: {result}")

    def log_error(self, error: Exception):
        """Log error event"""
        self.logger.error(f"Error occurred: {str(error)}")

    def log_info(self, message: str):
        """Log general information"""
        self.logger.info(message)
