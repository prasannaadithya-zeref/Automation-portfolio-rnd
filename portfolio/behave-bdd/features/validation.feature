Feature: Monthly Report Validation
  As a Data Engineer
  I want to validate the monthly financial reports
  So that I ensure accurate billing

  Scenario: Verify Header Record in Report
    Given the monthly report file "finance_oct_2023.txt" is available
    When I read the first line
    Then the header should contain "HDR|202310"

  Scenario: Validate Record Totals
    Given the database has 500 transactions for "October"
    When I count the records in the report file
    Then the file record count should match the database count
