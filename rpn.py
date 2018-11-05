#!/usr/bin/env python3

import operator
import csv
import sys

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow
}

def readInCSV(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(calculate(' '.join(row)))

def calculate(myarg):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def hello_world():
    print("Hello World")

def main():
    if len(sys.argv) > 1:
        readInCSV(sys.argv[1])
    else:
        while True:
            result = calculate(input("rpn calc> "))
            print("Result: ", result)

if __name__ == '__main__':
    main()
