Feature: Quirky Quiz : Super power


  Scenario: TC:011 : Blank Scenario
    Given the user is at the challenge page
     When the user click zap the answer
     Then the user is shown zap successfully message

  Scenario: TC:012 : Positive Scenario
    Given the user is at the challenge page
    When the user type "Invisible"
    AND the user click zap the answer
    Then the user is shown zap successfully message

  Scenario: TC:013 : 3 Underscore Scenario
      Given the user is at the challenge page
      When the user type "___"
      AND the user click zap the answer
      Then the user is shown zap successfully message

  Scenario: TC:014 : 3 space Scenario
      Given the user is at the challenge page
      When the user type "   "
      AND the user click zap the answer
      Then the user is shown zap successfully message
  
  Scenario: TC:015 : Special Character Scenario
      Given the user is at the challenge page
      When the user type "@#!$%"
      AND the user click zap the answer
      Then the user is shown zap successfully message

  Scenario: TC:016 : Number Scenario
      Given the user is at the challenge page
      When the user type "123456"
      AND the user click zap the answer
      Then the user is shown zap successfully message
  

