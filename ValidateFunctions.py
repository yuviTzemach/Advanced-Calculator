class ValidateOperations:

    def validate_left_operand(op1):
        if not (op1 == ')' or op1.isdigit()):
            raise ArithmeticError("Left operand is not valid")

    def validate_right_operand(op2):
        if not (op2 == '(' or op2 == '-' or op2.isdigit()):
            raise ArithmeticError("Right operand is not valid")

    def validate_trivial_operation(op1, op2):
        ValidateOperations.validate_left_operand(op1)
        ValidateOperations.validate_right_operand(op2)

    def validate_div(op1, op2):
        ValidateOperations.validate_trivial_operation((op1, op2))
        if op2 == 0:
            raise ArithmeticError("Divided by zero")

    def validate_tilda(op1):
        ValidateOperations.validate_right_operand(op1)

    def validate_factorial(op1):
        ValidateOperations.validate_left_operand(op1)
        if not isinstance(op1, int):
            raise ArithmeticError("Factorial's operand must be an Integer")

    def validate_sum_numbers(op1):
        ValidateOperations.validate_left_operand(op1)
