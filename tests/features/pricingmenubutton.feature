Feature: Access 7-days free trial for ticket booking

    Scenario: Test the user giving the valid credentials, it navigate to trail-success page
        Given I am launching chrome browser
        When I am giving valid credentials and click download button
        Then verify the landing page url