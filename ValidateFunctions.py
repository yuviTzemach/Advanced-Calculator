from Definitions import *


class ValidateOperations:

    def validate_left_operand_for_left_operator(op1):
        """
        the function is checking the validation of the left char next to left operator (#, !) - if op1 is ')' or a
        digit, it raises an ArithmeticError
        @param op1: the left operand
        """
        if (op1 == ')' or op1.isdigit()):
            raise ArithmeticError("Left operand for left operator is not valid")

    def validate_right_operand_for_right_operator(op2):
        """
        the function is checking the validation of the right char next to right operator (~) - if op2 is '(', '-' or a
        digit, it raises an ArithmeticError
        @param op2: the right operand
        """
        if (op2 == '(' or op2.isdigit()):
            raise ArithmeticError("Right operand for right operator is not valid")

    def validate_left_operand(op1):
        """
        the function is checking the validation of the char - if op1 is not ')' or a digit, it raises an ArithmeticError
        @param op1: the left operand
        """
        # '!' and '#' are also allowed as the left operand of operators
        if not (op1 == ')' or op1.isdigit() or op1 in right_operations):
            raise ArithmeticError("Left operand is not valid")

    def validate_right_operand(op2):
        """
        the function is checking the validation of the char - if op2 is not '(', '-' or a digit, it raises an
        ArithmeticError
        @param op2: the right operand
        """
        if not (op2 == '(' or op2 == '-' or op2.isdigit() or op2 in left_operation):
            raise ArithmeticError("Right operand is not valid")

    def validate_trivial_operation(op1, op2):
        """
        the function is checking the validation of the two operands
        @param op1: the left operand
        @param op2: the right operand
        """
        ValidateOperations.validate_left_operand(op1)
        ValidateOperations.validate_right_operand(op2)

    def validate_div(op1, op2):
        """
        the function is checking the validation of the two operands in the division operation - if op2 is 0, is raises
        an ArithmeticError
        @param op1: the left operand
        @param op2: the right operand
        """
        ValidateOperations.validate_trivial_operation((op1, op2))
        if op2 == 0:
            raise ArithmeticError("Divided by zero")

    def validate_tilda(op2):
        """
        the function is checking the validation of the char
        @param op2: the right operand
        """
        ValidateOperations.validate_right_operand(op2)

    def validate_factorial(op1):
        """
        the function is checking the validation of the char and also, if the type of the operand is not int, it raises
        an ArithmeticError
        @param op1: the left operand
        """
        ValidateOperations.validate_left_operand(op1)
        if not isinstance(op1, int):
            raise ArithmeticError("Factorial's operand must be an Integer")

    def validate_sum_numbers(op1):
        """
        the function is checking the validation of the char
        @param op1: the left operand
        """
        ValidateOperations.validate_left_operand(op1)
