Feature: validate ISBN Number
  Scenario Outline: validation of ISBN Number
    Given ISBN Number validation
    When the number is <number>
		Then Its <result>
		Examples:
			| number                                        | result |
			| 978-3-16-148410-0                             | True   |
			| 9783161484100                                 | True   |
			| 9-7-8-3-1-6-1-4-8-4-1-0-0                     | True   |
			| 000000000000000000000000000000000000000000000 | False  |
			| 0000000000000                                 | True   |
			| 0000000000001                                 | False  |
      		| 54337646532123                                | False  |
      		| 4635263215234                                 | True   |
      		| 1234567890123                                 | False  |
