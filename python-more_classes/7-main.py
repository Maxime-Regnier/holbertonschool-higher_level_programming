#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

myrectangle1 = Rectangle(8, 4)
print(myrectangle1)
print("--")
myrectangle1.print_symbol = "&"
print(myrectangle1)
print("--")

myrectangle2 = Rectangle(2, 1)
print(myrectangle2)
print("--")
Rectangle.print_symbol = "C"
print(myrectangle2)
print("--")

myrectangle3 = Rectangle(7, 3)
print(myrectangle3)
print("--")
myrectangle3.print_symbol = ["C", "is", "fun!"]
print(myrectangle3)
print("--")
