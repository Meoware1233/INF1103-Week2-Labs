# 2601582 INF1103 Week 10 Lab
from week10_product import Product
from week10_orderline import OrderLine

class Order:
    def __init__(self, order_id:str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def get_order_lines(self) -> list[OrderLine]:
        return self.__order_lines

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def calculate_total(self) -> float:
        total = 0.0
        for line in self.__order_lines:
            total += line.calculate_subtotal()
        return total

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