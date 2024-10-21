# Python_Control_Flow :rocket:
This repository contains a collection of Python scripts showcasing different control flow logic in real-world scenarios. The examples are designed to demonstrate the power of conditionals, loops, functions, error handling, and modularization in Python. The three examples included in this project are:

1. Prime Number Finder
2. Shopping Discount Calculator
3. Order Management System

### Table of Contents
Prime Number Finder<br>
Shopping Discount Calculator<br>
Order Management System<br>
Requirements<br>
How to Run


# Prime Number Finder
The Prime Number Finder script checks for prime numbers within a given range. Prime numbers are integers greater than 1 that are only divisible by 1 and themselves.

How it Works
The user inputs an integer n, and the program returns all prime numbers less than n.<br>
The logic uses nested loops to check the divisibility of each number and a helper function to flag whether a number is prime.

# Shopping Discount Calculator
The Shopping Discount Calculator script is a simple tool for calculating the total price of items in a shopping cart after applying various discounts. It includes error handling to ensure valid discounts are applied.

 Key Features
The function apply_discount() ensures discounts are between 0% and 100%.
Invalid discounts are handled using try-except blocks, returning 0 for invalid values.
The calculate_cart() function aggregates the total price of the cart after applying discounts.

# Example Usage

```python
# Example cart
cart_items = [(100, 10), (200, 20), (50, 5)]
print(f"Total cart price: {calculate_cart(cart_items)}")  # Output: 315.0
```


# Order Management System
The Order Management System simulates an online store where users can add and remove items from their cart, apply discounts, and process orders. This example demonstrates a robust control flow that incorporates:

-Inventory management: tracking items and their stock.<br>
-Cart management: adding and removing items while updating stock.<br>
-Discount system: applying valid discounts to the total cart price.<br>
-Order processing: checking cart content and completing payment

#Key Features
Inventory validation (checks for stock availability).<br>
Error handling for invalid inputs (like incorrect discount codes or payment methods).<br>
A continuous loop to allow users to interact with the system multiple times.

```python
# Example
# Adding items to cart
add_to_cart('laptop', 2)
add_to_cart('phone', 1)

# Applying a discount and checking out
apply_discount_to_cart("SAVE10")
process_order("credit")
```
# Requirements
Python 3.x
No additional libraries or packages are required for this project.

# How To Run
1 clone the Repository
```bash
git clone https://github.com/PETERMUTWIRI/Python_Control_Flow.git
```
2 Navigate into the project directory
``` bash
cd Python_Control_flow
```
3 Run the Python Scripts
```bash
python prime_numbers.py      # For prime number finder
python shopping_discount.py  # For shopping discount calculator
python Online_order_System.py   # For order management system
```
