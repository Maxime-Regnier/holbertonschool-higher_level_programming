#!/usr/bin/python3
import sys
num_args = len(sys.argv) - 1
if __name__ == "__main__":
    if num_args == 0:
        print("0 arguments.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print(f"{num_args} arguments:")
    for i in range(1, len(sys.argv)):
        print(f"{i}: {sys.argv[i]}")
