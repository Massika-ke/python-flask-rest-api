# from typing import List

# def list_avg(sequence: List) -> float:
#     return sum(sequence) / len(sequence)
 
# def divide(dividend, divisor):
#     if divisor == 0:
#         raise ZeroDivisionError("Divisor cannot be 0")
    
#     return dividend / divisor

# def calculate(*values, operator):
#     return operator(*values)

# result = calculate(23, 0, operator=divide)
# print(result)
















# class Book:
#     TYPES = ("hardcover", "paperback")

#     def __init__(self, name, book_type, weight):
#         self.name = name
#         self.book_type = book_type
#         self.weight = weight

#     def __repr__(self):
#         return f"Book {self.name}, {self.book_type}, weighing {self.weight}grams"
    
#     @classmethod
#     def hardcover(cls, name, page_weight):
#         return Book(name, Book.TYPES[0], page_weight * 100)
    
# # book = Book("Harry Potter", "hardcover", 1000)
# book = Book.hardcover("Harry Potter", 1500)
# print(book)

# INHERITENCE
# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected =  True

#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"
    
#     def diconnect(self):
#         self.connected = False
#         print("Disconnected")

# # printer = Device("Printer", "USB")
# # print(printer)
# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str__(self):
#         return super().__str__() 