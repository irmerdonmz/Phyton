"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""
class Order:
    def __init__(self, price, discount_strategy):
        self.price = price
        self.discount_strategy = discount_strategy

    def final_price(self):
        return self.discount_strategy.apply_discount(self.price)


class DiscountStrategy:
    def apply_discount(self, price):
        raise NotImplementedError("Subclasses must implement apply_discount.")

class MorningDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price - price * 0.5

class ElderDiscount(DiscountStrategy):
    def apply_discount(self, price):
        return price - price * 0.9

# Usage example
order = Order(100, MorningDiscount())
print(order.final_price())  # Output: 50.0

order = Order(100, ElderDiscount())
print(order.final_price())  # Output: 10.0
