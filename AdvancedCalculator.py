#!/usr/bin/env python
from StringModification import *
from Functions import *


def main():

    string = input("please enter your equation:")
    print("1")
    string = erase_space(string)
    print(string)
    print("2")
    validate_chars(string)
    print(string)
    print("3")
    validate_parentheses(string)
    print(string)
    print("4")
    string = erase_minus(string)
    print(string)
    validate_operands(string)
    print(string)


if __name__ == "__main__":
    main()