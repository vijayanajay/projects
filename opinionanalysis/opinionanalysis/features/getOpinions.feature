Feature: Getting the contents of multiple feeds and displaying to user
 
  Scenario: Get a list of articles of the Feed
    Given a feed
    When all the articles are extracted
    Then I see 50 feeds in the Article table
    And all the fields are filled in

 
