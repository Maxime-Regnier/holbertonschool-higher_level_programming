#!/usr/bin/python3
def lookup(obj):
    pass
    return dir(obj)
class Test:
    def hello(self):
        return "Hi!"
t = Test()
print(lookup(t))