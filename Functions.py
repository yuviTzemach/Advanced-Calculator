from ValidateFunctions import *


class MathOperations:

    def add(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the addition of it
        @param op1: the left operand
        @param op2: the right operand
        returns the addition between the two operands
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 + op2

    def sub(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the subtraction of it
        @param op1: the left operand
        @param op2: the right operand
        returns the subtraction between the two operands
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 - op2

    def mul(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the multiplication of
        it
        @param op1: the left operand
        @param op2: the right operand
        returns the multiplication between the two operands
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 * op2

    def div(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the division of it
        @param op1: the left operand
        @param op2: the right operand
        returns the division between the two operands
        """
        ValidateOperations.validate_div((op1, op2))
        return op1 / op2

    def power(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the power of it
        @param op1: the left operand
        @param op2: the right operand
        returns the power between the two operands
        """
        ValidateOperations.validate_trivial_operation(op1, op2)
        # checking if the result of the power is a complex number - if yes, it raises an error, if no, it returns is
        result = pow(op1, op2)
        if isinstance(result, complex):
            raise ArithmeticError("the result is a complex number")
        else:
            return result

    def modulo(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the modulo of it
        @param op1: the left operand
        @param op2: the right operand
        returns the modulo between the two operands
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        return op1 % op2

    def max(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the maximum operands
        between the two operands
        @param op1: the left operand
        @param op2: the right operand
        returns the maximum operand between the two operands
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        if (op1 > op2):
            return op1
        else:
            return op2

    def min(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the minimum operands
        between the two operands
        @param op1: the left operand
        @param op2: the right operand
        returns the minimum operand between the two operands
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        if (op1 < op2):
            return op1
        else:
            return op2

    def avg(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the average of it
        @param op1: the left operand
        @param op2: the right operand
        returns the average between the two operands
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        return ((op1 + op2) / 2)

    def tilda(op1):
        """
        the function is checking if the right char next to the operator is valid, and if yes - returns the negation of
        it
        @param op1: the right operand
        returns the negation of the operand
        """
        ValidateOperations.validate_tilda(op1)
        return op1 * -1

    def factorial(op1):
        """
        the function is checking if the left char next to the operator is valid, and if yes - returns the factorial of
        it
        @param op1: the left operand
        returns the factorial of the operand
        """
        ValidateOperations.validate_factorial(op1)
        fact = 1
        for x in range(1, op1 + 1):
            fact = fact * x
        return fact

    def sum_numbers(op1):
        """
        the function is checking if the left char next to the operator is valid, and if yes - returns the sum of the
        numbers it contains
        @param op1: the left operand
        returns the sum of the numbers the operand contains
        """
        ValidateOperations.validate_sum_numbers(op1)
        op1 = int(str(op1).replace('.', ''))
        sum1 = 0
        while op1 != 0:
            sum1 += (op1 % 10)
            op1 /= 10
        return sum1
