Feature: Web Application Login
  As a user
  I want to login to the portal
  So that I can access secure data

  @ui
  Scenario Outline: Validate Login with Multiple Data Sets on Chrome
    Given I launch the browser "Chrome"
    When I navigate to the login page
    And I enter username "<username>" and password "<password>"
    Then I should see the message "<message>"

    Examples:
      | username    | password     | message                        |
      | tomsmith    | SuperSecret! | You logged into a secure area! |
      | baduser     | wrongpass    | Your username is invalid!      |
