Feature: scrolling down in the php travels

    Scenario: verify the user scrolling down the home page, it shows header menu, whatsapp and 'leave a message'
        Given i am launching chrome browser
        When I have scrolling the home page and verify header menu
        Then I am closing the browser