Feature: Homepage
    As a guest user
    I want to be able to see all articles in one page
    So that I can find them all the latest articles

    Scenario: Check if homepage lists out all articles to guest user

        Given I am a guest user

        When I navigate to the homepage
        Then I will see a atleast 10 articles
        And  I will be able to read the first article
        And  the article has more than 300 words

