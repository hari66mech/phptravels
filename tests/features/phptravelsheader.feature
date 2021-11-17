Feature: clicking the php travels header

    Scenario: test the user clicking the php travels header, it navigate the home page
        Given I am launching chrome browser
        When I am clicking the php travels header
        Then verify the landing page url