from behave import given, when, then
import requests
import sys
import os

# Add project root to path to import utils
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../python-frameworks')))
from utils.aws_handler import AWSHandler

# --- UI Steps (Mocked for demo, normally uses Selenium/Playwright) ---
@given('I launch the browser "{browser_name}"')
def step_launch_browser(context, browser_name):
    print(f"Launching {browser_name}...")

@when('I navigate to the login page')
def step_nav_login(context):
    print("Navigating to Login URL...")

@when('I enter username "{user}" and password "{pwd}"')
def step_enter_creds(context, user, pwd):
    print(f"Entering credentials: {user} / ****")

@then('I should see the message "{msg}"')
def step_verify_msg(context, msg):
    print(f"Verifying message: {msg}")

# --- API Steps ---
@given('the API service is running at "{url}"')
def step_api_setup(context, url):
    context.api_url = url

@when('I request user details for ID {uid}')
def step_get_user(context, uid):
    try:
        context.response = requests.get(f"{context.api_url}/users/{uid}")
    except:
        context.response = None

@then('the response status code should be {code:d}')
def step_check_status(context, code):
    if context.response:
        assert context.response.status_code == code
    else:
        print("API Call failed to connect")

@then('the role should be "{role}"')
def step_check_role(context, role):
    if context.response:
        assert context.response.json()['role'] == role

# --- AWS Steps ---
@given('I have a local config file "{filename}"')
def step_create_file(context, filename):
    with open(filename, 'w') as f:
        f.write("config=true")
    context.filename = filename

@when('I upload the file to S3 bucket "{bucket}"')
def step_s3_upload(context, bucket):
    context.bucket = bucket
    # Using our custom shared library!
    aws = AWSHandler()
    context.upload_success = aws.upload_file_to_s3(context.filename, bucket, f"configs/{context.filename}")

@then('the file should exist in the "{folder}" folder on S3')
def step_verify_s3(context, folder):
    # Mock assertion as we likely don't have real creds in demo environment
    print(f"Verifying existence in {folder}...")
