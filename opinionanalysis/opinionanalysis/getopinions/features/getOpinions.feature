Feature: Demonstrate how to use the mechanize browser to do useful things.
 
  Scenario: Logging in to our new Django site
 
    Given a user
    When I log in
    Then I see my account summary
     And I see a warm and welcoming message
 
  Scenario: Loggout out of our new Django site
    Given a user
    When I log in
    And I log out
    Then I see a cold and heartless message