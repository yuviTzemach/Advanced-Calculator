from ValidateFunctions import *


class MathOperations:

    def validate_inf(number: str):
        # infinity float number will contain 'e' character in it
        if str(float(number)).find('e') != -1:
            raise ValueError("Error : got infinity number !")
        return True

    def add(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the addition of it
        @param op1: the left operand
        @param op2: the right operand
        returns the addition between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        res = str(float(op1) + float(op2))
        MathOperations.validate_inf(res)
        return res

    def sub(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the subtraction of it
        @param op1: the left operand
        @param op2: the right operand
        returns the subtraction between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        res = str(float(op1) - float(op2))
        MathOperations.validate_inf(res)
        return res

    def mul(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the multiplication of
        it
        @param op1: the left operand
        @param op2: the right operand
        returns the multiplication between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        res = str(float(op1) * float(op2))
        MathOperations.validate_inf(op2)
        return res

    def div(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the division of it
        @param op1: the left operand
        @param op2: the right operand
        returns the division between the two operands
        """
        if float(op2) == 0.0:
            raise ArithmeticError("Dividing by zero")
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        res = str(float(op1) / float(op2))
        MathOperations.validate_inf(res)
        return res

    def power(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the power of it
        @param op1: the left operand
        @param op2: the right operand
        returns the power between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        res = pow(float(op1), float(op2))
        if isinstance(res, complex):
            # checking if the result of the power is a complex number - if yes, it raises an error, if no, it returns is
            raise ArithmeticError("the result is a complex number")
        MathOperations.validate_inf(res)
        return res

    def modulo(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the modulo of it
        @param op1: the left operand
        @param op2: the right operand
        returns the modulo between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        res = str(float(op1) % float(op2))
        MathOperations.validate_inf(res)
        return res

    def max(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the maximum operands
        between the two operands
        @param op1: the left operand
        @param op2: the right operand
        returns the maximum operand between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        return str(float(op1)) if float(op1) > float(op2) else str(float(op2))

    def min(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the minimum operands
        between the two operands
        @param op1: the left operand
        @param op2: the right operand
        returns the minimum operand between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        return str(float(op1)) if float(op1) < float(op2) else str(float(op2))

    def avg(op1, op2):
        """
        the function is checking if the chars next to the operator is valid, and if yes - returns the average of it
        @param op1: the left operand
        @param op2: the right operand
        returns the average between the two operands
        """
        MathOperations.validate_inf(op1) and MathOperations.validate_inf(op2)
        res = str(float((float(op1) + float(op2)) / 2.0))
        MathOperations.validate_inf(res)
        return res

    def tilda(op2):
        """
        the function is checking if the right char next to the operator is valid, and if yes - returns the negation of
        it
        @param op2: the right operand
        returns the negation of the operand
        """
        MathOperations.validate_inf(op2)
        res = str(float(op2) * -1)
        MathOperations.validate_inf(res)
        return res

    def factorial(op1):
        """
        the function is checking if the left char next to the operator is valid, and if yes - returns the factorial of
        it
        @param op1: the left operand
        returns the factorial of the operand
        """
        MathOperations.validate_inf(op1)
        # if op1 represents like a float
        if op1.find('.') != -1:
            # split the float number by its floating point
            op1, after_floating_point = op1.split('.')
            # check if the number after the floating point is 0.
            # if not, op1 isn't an integer and the operation isn't valid.
            if after_floating_point != "0":
                raise ArithmeticError("doesn't work on float numbers")
        # it is ok because op1 is definitely an integer here
        op1 = int(op1)
        factorial = 1
        if op1 < 0:
            raise ArithmeticError("doesn't work on negative numbers")
        elif op1 == 0:
            return str(float(factorial))
        for i in range(1, op1 + 1):
            factorial *= i
        MathOperations.validate_inf(factorial)
        return str(float(factorial))

    def sum_numbers(op1):
        """
        the function is checking if the left char next to the operator is valid, and if yes - returns the sum of the
        numbers it contains
        @param op1: the left operand
        returns the sum of the numbers the operand contains
        """
        # remove the '.' from the operand
        MathOperations.validate_inf(op1)
        op1 = int((op1.replace('.', '')))
        sum = 0
        while op1 != 0:
            sum += (op1 % 10)
            op1 //= 10
        res = str(float(sum))
        MathOperations.validate_inf(res)
        return res
