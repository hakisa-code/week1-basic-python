# Passing Grade
# Task 1 — Procedural vs. OOP
# Instructions
# 1. Write a procedural Python function called calculate_discount(price,
# percentage) that returns the discounted price.
# 2. Write an OOP version using a class called DiscountCalculator with:
# - an initializer that takes percentage
# - a method apply(price) that returns the discounted price
# 3. Call each version once and print the result.
# Procedural version
def calculate_discount(price, percentage):
    discount = price * (percentage / 100)
    return price - discount
# OOP version
class DiscountCalculator:
    def __init__(self, percentage):
        self.percentage = percentage
    def apply(self, price):
        discount = price * (self.percentage / 100)
        return price - discount
# Example usage

if __name__ == "__main__":
    # Procedural
    price = 100
    percentage = 15
    discounted_price_procedural = calculate_discount(price, percentage)
    print(f"Procedural: The discounted price is {discounted_price_procedural}")
    # OOP
    discount_calculator = DiscountCalculator(percentage)
    discounted_price_oop = discount_calculator.apply(price)
    print(f"OOP: The discounted price is {discounted_price_oop}")


