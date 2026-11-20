# 2601582 INF1103 Week 10 Lab
from __future__ import annotations
from week11_product import Product
from week11_orderline import OrderLine
from week11_discount import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id:str, discount: DiscountStrategy | None = None):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []
        self.__discount: DiscountStrategy = discount if discount is not None else NoDiscount()

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return self.__discount.apply(total)

    def display_information(self) -> None:
        print(f"Order ID: {self.__order_id}")
        for line in self.__order_lines:
            line.display_information()
        print(f"Total: ${self.calculate_total():.2f}")

    def remove_order_line(self,product_id: str) -> None:
        for line in self.__order_lines:
            if line.get_product().get_product_id() == product_id:
                self.__order_lines.remove(line)
                return
        print("Order line not found.")