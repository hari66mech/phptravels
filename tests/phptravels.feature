Feature: Login the php travels

    Scenario: login with given credential
        Given launch chrome browser
        When login as a given credential
        Then redirect to the home page