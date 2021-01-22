Feature: Convert Number to Roman Numeral
  converts decimal numbers to roman numerals

  Scenario Outline: Convert number to roman numeral
    Given a decimal number equal to <arabic>
    When a roman number equal to <roman>
    Then arabic number should be equal to roman

    Examples:
      | arabic | roman     |
      |  5     | V         |
      |  24    | XXIV      |
      |  163   | CLXIII    |
      |  402   | CDII      |
      |  911   | CMXI      |
      |  3000  | MMM       |
