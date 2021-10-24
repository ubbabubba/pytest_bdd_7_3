# Created by jmill at 10/24/2021
Feature: Apple Cart
  As an apple picker,
  I want to carry apples all around,
  So I don't drop them

  Scenario: Add apples to the cart
    Given the cart has 0 apples
    When 4 apples are added to the cart
    Then the cart contains 4 apples

  Scenario: Remove apples from the cart
    Given the cart has 8 apples
    When 4 apples are removed from the cart
    Then the cart contains 4 apples