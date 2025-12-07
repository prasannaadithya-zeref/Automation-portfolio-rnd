Feature: Backend ETL and API Operations

  @api
  Scenario: Validate User API Endpoint
    Given the API service is running at "http://localhost:5000"
    When I request user details for ID 1
    Then the response status code should be 200
    And the role should be "Automation Engineer"

  @aws @etl
  Scenario: Verify ETL Config Upload to S3
    Given I have a local config file "etl_job.conf"
    When I upload the file to S3 bucket "my-datalake-bucket"
    Then the file should exist in the "configs" folder on S3
