Feature: FizzBuzz
  Scenario Outline: FizzBuzz game
    Given there is FizzBuzz game
    When I get the number <number>
    Then Its <result>
    Examples:
      | number | result |
      | 5 | Buzz |
      | 3 | Fizz |
      | 15 | FizzBuzz |
      | 41 | 41 |
      | 225 | FizzBuzz |
