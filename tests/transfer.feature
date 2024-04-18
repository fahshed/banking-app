Feature: Transfer Money

  Scenario: Transfer money from one account to another

    Given there is an account with account number 123456789 and balance 1000
    And there is an account with account number 987654321 and balance 2000
    When I transfer 500 from account 123456789 to account 987654321
    Then the transfer should be successful