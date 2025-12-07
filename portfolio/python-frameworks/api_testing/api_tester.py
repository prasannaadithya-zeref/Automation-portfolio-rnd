import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class APITester:
    """
    Utility for API testing and validation.
    Wraps 'requests' library with built-in validation assertions.
    """
    
    def __init__(self, base_url):
        self.base_url = base_url.rstrip('/')

    def validate_get_status(self, endpoint, expected_status=200):
        """Verifies that a GET request returns the expected status code."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == expected_status:
                logger.info(f"PASS: GET {endpoint} returned {response.status_code}")
                return True, response.json() if response.content else {}
            else:
                logger.error(f"FAIL: GET {endpoint} returned {response.status_code}. Expected {expected_status}.")
                return False, {}
        except requests.exceptions.RequestException as e:
            logger.error(f"ERROR: Request failed - {str(e)}")
            return False, {}

    def validate_json_schema(self, endpoint, required_keys):
        """Verifies specific keys exist in the JSON response."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)
        data = response.json()
        
        missing = [key for key in required_keys if key not in data]
        if not missing:
            logger.info(f"PASS: Schema validation for {endpoint}. Keys found: {required_keys}")
            return True, data
        else:
            logger.error(f"FAIL: Schema validation for {endpoint}. Missing keys: {missing}")
            return False, data

    def validate_post_creation(self, endpoint, payload):
        """Verifies a POST request successfully creates a resource."""
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=payload)
        if response.status_code == 201:
            logger.info(f"PASS: POST {endpoint} created resource. ID: {response.json().get('id')}")
            return True
        else:
            logger.error(f"FAIL: POST {endpoint} failed. Status: {response.status_code}")
            return False
