"""
LEARNING LAB: Handling Dynamic JSON Data
========================================
In API testing, we often get JSON responses where keys change or are nested deeply.
Hardcoding `data['response']['body']['items'][0]['id']` is brittle.

This module teaches:
1. Recursive JSON search (finding a key anywhere).
2. Safe access with default values.
"""

def find_key_recursive(data, target_key):
    """
    Scans a nested JSON (dict/list) of ANY depth to find a key.
    Returns value if found, else None.
    """
    if isinstance(data, dict):
        for k, v in data.items():
            if k == target_key:
                return v
            # If value is another dict or list, go deeper
            if isinstance(v, (dict, list)):
                result = find_key_recursive(v, target_key)
                if result: return result
                
    elif isinstance(data, list):
        for item in data:
            result = find_key_recursive(item, target_key)
            if result: return result
            
    return None

def main():
    # Complex Nested JSON (Real world API example)
    api_response = {
        "status": 200,
        "payload": {
            "meta": {"timestamp": 12345},
            "data": {
                "users": [
                    {
                        "id": 1,
                        "attributes": {
                             "role": "Admin",
                             "settings": {"newsletter": True}
                        }
                    }
                ]
            }
        }
    }
    
    print("--- Dynamic JSON Parsing ---")
    
    # Scenario: I want 'newsletter' status but don't want to type the full path.
    # The 'Brittle' way:
    # val = api_response['payload']['data']['users'][0]['attributes']['settings']['newsletter']
    
    # The 'Dynamic' way:
    val = find_key_recursive(api_response, "newsletter")
    print(f"Found 'newsletter' value: {val}")

    # Finds keys even if schema changes structure slightly
    role = find_key_recursive(api_response, "role")
    print(f"Found 'role' value: {role}")

if __name__ == "__main__":
    main()
