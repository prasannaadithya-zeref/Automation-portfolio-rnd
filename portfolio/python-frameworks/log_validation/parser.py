import re
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LogParser:
    """
    Utility to parse large log files and extract structured data.
    Demonstrates regex proficiency and efficient file handling.
    """
    def __init__(self, log_file_path):
        self.log_file_path = log_file_path

    def extract_metrics(self, pattern):
        """
        Parses the log file line by line and extracts data matching the regex pattern.
        Returns a list of dictionaries with captured groups.
        """
        results = []
        regex = re.compile(pattern)
        
        try:
            with open(self.log_file_path, 'r', encoding='utf-8') as f:
                for line_no, line in enumerate(f, 1):
                    match = regex.search(line)
                    if match:
                        data = match.groupdict()
                        data['line_no'] = line_no
                        results.append(data)
        except FileNotFoundError:
            logger.error(f"Log file not found: {self.log_file_path}")
            return []
            
        logger.info(f"Extracted {len(results)} records from logs.")
        return results

    def find_errors(self):
        """
        Quick scan for common error keywords.
        """
        error_pattern = r"(ERROR|CRITICAL|FATAL)\s+(.*)"
        return self.extract_metrics(error_pattern)
