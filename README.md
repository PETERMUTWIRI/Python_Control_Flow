# Python_Control_Flow
This repository contains a collection of Python scripts showcasing different control flow logic in real-world scenarios. The examples are designed to demonstrate the power of conditionals, loops, functions, error handling, and modularization in Python. The three examples included in this project are:

## Prime Number Finder
 ## Shopping Discount Calculator
   ## Order Management System

### Table of Contents
Prime Number Finder
Shopping Discount Calculator
Order Management System
Requirements
How to Run
License

# Prime Number Finder
The Prime Number Finder script checks for prime numbers within a given range. Prime numbers are integers greater than 1 that are only divisible by 1 and themselves.

How it Works
The user inputs an integer n, and the program returns all prime numbers less than n.
The logic uses nested loops to check divisibility of each number and a helper function to flag whether a number is prime.

# Shopping Discount Calculator
The Shopping Discount Calculator script is a simple tool for calculating the total price of items in a shopping cart after applying various discounts. It includes error handling to ensure valid discounts are applied.

Key Features
The function apply_discount() ensures discounts are between 0% and 100%.
Invalid discounts are handled using try-except blocks, returning 0 for invalid values.
The calculate_cart() function aggregates the total price of the cart after applying discounts.