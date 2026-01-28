#!/usr/bin/python3
Rectangle = __import__("4-rectangle").Rectangle

myrectangle = Rectangle(2, 4)
print(str(myrectangle))
print("--")
print(myrectangle)
print("--")
print(repr(myrectangle))
print("--")
print(hex(id(myrectangle)))
print("--")

newrectangle = eval(repr(myrectangle))
print(str(newrectangle))
print("--")
print(newrectangle)
print("--")
print(repr(newrectangle))
print("--")
print(hex(id(newrectangle)))
print("--")

print(newrectangle is myrectangle)
print(type(newrectangle) is type(myrectangle))