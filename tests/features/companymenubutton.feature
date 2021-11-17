Feature: Select 2018 photos in about-as page

    Scenario: Test the user clicking the about-as under company button, it navigate to the about-us page and see 2018 photos
        Given I am launching chrome browser
        When I am clicking the about-as under company button
        Then verify the landing page url and 2018 photos