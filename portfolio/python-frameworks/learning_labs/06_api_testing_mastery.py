"""
LEARNING LAB: API Testing Mastery (Requests Library)
====================================================
API Testing is crucial for modern automation. We use the 'requests' library.
This guide goes from simple calls to generic wrappers.

SECTION 1: THE BASICS (GET & POST)
----------------------------------
"""
import requests
import json

def basic_api_calls():
    print("--- [1] BASIC API CALLS ---")
    
    # 1. GET Request (Read)
    # ---------------------
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    
    # Validation
    if response.status_code == 200:
        print(f"GET Success. Title: {response.json()['title']}")
    else:
        print("GET Failed")

    # 2. POST Request (Create)
    # ------------------------
    post_url = "https://jsonplaceholder.typicode.com/posts"
    payload = {"title": "Automation", "body": "API Testing", "userId": 1}
    
    # Headers are important! They tell the server you are sending JSON.
    headers = {"Content-Type": "application/json"}
    
    resp_post = requests.post(post_url, json=payload, headers=headers)
    print(f"POST Status: {resp_post.status_code}") # 201 Created

"""
SECTION 2: INTERMEDIATE (Sessions & Auth)
-----------------------------------------
Why use a Session? 
It persists cookies and headers across multiple requests (like a logged-in browser).
"""

def session_management():
    print("\n--- [2] SESSIONS & AUTH ---")
    
    # Create a Session object
    s = requests.Session()
    
    # Add a default header for ALL future requests in this session
    s.headers.update({"Authorization": "Bearer my-secret-token"})
    
    # This request includes the Auth token automatically
    # (Simulated call)
    try:
        r = s.get("https://httpbin.org/headers")
        print(f"Headers sent: {r.json()['headers']['Authorization']}")
    except Exception as e:
        print(f"Connection error (expected in offline demo): {e}")

"""
SECTION 3: EXPERT (Generic API Wrapper)
---------------------------------------
Don't write 'requests.get' in every test. Create a wrapper class.
This handles timeouts, error logging, and base URLs centrally.
"""

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.timeout = 10 # seconds

    def _request(self, method, endpoint, **kwargs):
        """Internal helper to handle all requests consistently."""
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, timeout=self.timeout, **kwargs)
            response.raise_for_status() # Raise error for 4xx/5xx codes
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"[!] HTTP Error: {e}")
        except requests.exceptions.Timeout:
            print("[!] Request Timed Out")
        return None

    def get_user(self, user_id):
        return self._request('GET', f"/users/{user_id}")

    def create_user(self, name):
        return self._request('POST', "/users", json={"name": name})

if __name__ == "__main__":
    basic_api_calls()
    session_management()
    
    print("\n--- [3] WRAPPER DEMO ---")
    client = APIClient("https://jsonplaceholder.typicode.com")
    data = client.get_user(1)
    if data:
        print(f"Wrapper fetched User: {data.get('name')}")
