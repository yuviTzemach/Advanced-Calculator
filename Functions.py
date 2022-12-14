from ValidateFunctions import *


class MathOperations:

    def add(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 + op2

    def sub(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 - op2

    def mul(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 * op2

    def div(op1, op2):
        ValidateOperations.validate_div((op1, op2))
        return op1 / op2

    def power(op1, op2):
        ValidateOperations.validate_trivial_operation(op1, op2)
        return pow(op1, op2)

    def modulo(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 % op2

    def max(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        if (op1 > op2):
            return op1
        else:
            return op2

    def min(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        if (op1 < op2):
            return op1
        else:
            return op2

    def avg(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        return ((op1 + op2) / 2)

    def tilda(op1):
        ValidateOperations.validate_tilda(op1)
        return op1 * -1

    def factorial(op1):
        ValidateOperations.validate_factorial(op1)
        fact = 1
        for x in range(1, op1 + 1):
            fact = fact * x
        return fact

    def sum_numbers(op1):
        ValidateOperations.validate_sum_numbers(op1)
        op1 = int(str(op1).replace('.', ''))
        sum1 = 0
        while op1 != 0:
            sum1 += (op1 / 10)
            op1 /= 10
        return sum1
