Feature: The php travels login

    Scenario: verify the user login with valid credential
        Given i am launching chrome browser
        When login as the valid credential
        Then redirect to the home page