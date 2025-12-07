from behave import given, when, then

@given('the monthly report file "{filename}" is available')
def step_impl(context, filename):
    context.report_file = filename
    print(f"Checking for file {filename}")
    # Logic to check file existence would go here

@when('I read the first line')
def step_impl(context):
    context.header_line = "HDR|202310|001" # Mocked read
    print(f"Read header: {context.header_line}")

@then('the header should contain "{expected_text}"')
def step_impl(context, expected_text):
    assert expected_text in context.header_line
    print(f"Validated header contains {expected_text}")

@given('the database has {count} transactions for "{mnth}"')
def step_impl(context, count, mnth):
    context.db_count = int(count)
    print(f"DB count for {mnth} is {count}")

@when('I count the records in the report file')
def step_impl(context):
    context.file_count = 500 # Mocked
    print("counted file records")

@then('the file record count should match the database count')
def step_impl(context):
    assert context.file_count == context.db_count
