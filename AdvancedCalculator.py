from StringModification import *
from Functions import *
from OperationsPriority import *


def can_execute_operator(left_operand, right_operand):
    """
    check if we can execute an operator on the given operands -> means that the two of them are numbers.
    @param left_operand: the operand that places left to the operator
    @param right_operand: the operand that places right to the operator
    returns true or false
    """
    return is_operand_number(left_operand) and is_operand_number(right_operand)


def is_operand_number(operand):
    """
    The function checks if the given operand is a number (whether positive or negative)
    @param operand: the string to check on
    returns True if the operand represents a number
            False otherwise
    """
    # ignore the floating point in order to facilitate the validation
    int_operand = operand.replace('.', '')

    # check if the operand is numbers OR starts with a negative sign and then becomes number.
    return (int_operand.isdigit()) or (int_operand[0] == '-' and int_operand[1:].isdigit())


def calculate_expression(string):
    """
    The function calculate the equation by doing it in the order of the priority, first of all - 6 priority and the last
    one is 1 priority
    @param string: the string that represent the equation
    returns the result of each equation
    """
    # if our calculation is over.
    finish, string = ExpressionParser.is_calculation_finish(string)
    if finish:
        return string

    found_factorial_sum_tilda, operator, factorial_sum_tilda_tuple = factorial_sum_tilda_priority(string)
    if found_factorial_sum_tilda:
        operator_index, operand, operand_index = factorial_sum_tilda_tuple
        operand = calculate_expression(operand)

        # if we can execute the operator
        if is_operand_number(operand):
            if operator == '~':
                operator_result = MathOperations.tilda(operand)
                operator_result = '(' + operator_result + ')'
                string = ExpressionParser.replace_expression_with_result\
                    (string, operator_index, operand_index, operator_result)
                return calculate_expression(string)

            elif operator == '!':
                operator_result = MathOperations.factorial(operand)

            elif operator == '#':
                operator_result = MathOperations.sum_numbers(operand)

            string = ExpressionParser.replace_expression_with_result\
                (string, operand_index, operator_index, operator_result)
            return calculate_expression(string)

    found_min_max_avg, operator, min_max_avg_tuple = min_max_avg_priority(string)
    if found_min_max_avg:
        left_operand, left_operand_first_index, right_operand, right_operand_last_index = min_max_avg_tuple
        left_operand = calculate_expression(left_operand)
        right_operand = calculate_expression(right_operand)

        # if we can execute the operator
        if can_execute_operator(left_operand, right_operand):

            # execute the relevant operator
            if operator == '&':
                operator_result = MathOperations.min(left_operand, right_operand)

            elif operator == '$':
                operator_result = MathOperations.max(left_operand, right_operand)

            elif operator == '@':
                operator_result = MathOperations.avg(left_operand, right_operand)

            string = ExpressionParser.replace_expression_with_result \
                (string, left_operand_first_index, right_operand_last_index, operator_result)
            return calculate_expression(string)

    found_modulo, operator, modulo_tuple = modulo_priority(string)
    if found_modulo:
        left_operand, left_operand_first_index, right_operand, right_operand_last_index = modulo_tuple
        left_operand = calculate_expression(left_operand)
        right_operand = calculate_expression(right_operand)

        # if we can execute the operator
        if can_execute_operator(left_operand, right_operand):
            operator_result = MathOperations.modulo(left_operand, right_operand)
            string = ExpressionParser.replace_expression_with_result\
                (string, left_operand_first_index, right_operand_last_index, operator_result)
            return calculate_expression(string)

    found_power, operator, power_tuple = power_priority(string)
    if found_power:
        left_operand, left_operand_first_index, right_operand, right_operand_last_index = power_tuple
        left_operand = calculate_expression(left_operand)
        right_operand = calculate_expression(right_operand)

        # if we can execute the operator
        if can_execute_operator(left_operand, right_operand):
            operator_result = MathOperations.power(left_operand, right_operand)
            string = ExpressionParser.replace_expression_with_result\
                (string, left_operand_first_index, right_operand_last_index, operator_result)
            return calculate_expression(string)

    found_mul_div, operator, mul_div_tuple = mul_div_priority(string)
    if found_mul_div:
        left_operand, left_operand_first_index, right_operand, right_operand_last_index = mul_div_tuple
        left_operand = calculate_expression(left_operand)
        right_operand = calculate_expression(right_operand)

        # if we can execute the operator
        if can_execute_operator(left_operand, right_operand):
            if operator == '*':
                operator_result = MathOperations.mul(left_operand, right_operand)

            elif operator == '/':
                operator_result = MathOperations.div(left_operand, right_operand)

            string = ExpressionParser.replace_expression_with_result\
                (string, left_operand_first_index, right_operand_last_index, operator_result)
            return calculate_expression(string)

    found_plus_minus, operator, plus_minus_tuple = plus_minus_priority(string)
    if found_plus_minus:
        left_operand, left_operand_first_index, right_operand, right_operand_last_index = plus_minus_tuple
        left_operand = calculate_expression(left_operand)
        right_operand = calculate_expression(right_operand)
        # if we can execute the operator
        if can_execute_operator(left_operand, right_operand):
            if operator == '+':
                operator_result = MathOperations.add(left_operand, right_operand)

            elif operator == '-':
                operator_result = MathOperations.sub(left_operand, right_operand)

            string = ExpressionParser.replace_expression_with_result\
                (string, left_operand_first_index, right_operand_last_index, operator_result)
            return calculate_expression(string)

    # if got here - no operator was found - probably only redundant parenthesis was left - remove it
    return calculate_expression(string[1:-1])


def run_calculator(string):
    string = erase_space(string)
    if string == "()" or string == "":
        raise SyntaxError("invalid string")
    validate_chars(string)
    if not validate_parentheses(string):
        raise SyntaxError("Unbalance parentheses")
    string = erase_minus(string)
    print("string : " + string)
    validate_operands(string)
    # remove redundant parentheses
    if string[0] == '(' and string[-1] == ')' and validate_parentheses(string[1:-1]):
        string = string[1:-1]
    print("start calculating... ")
    return calculate_expression(string)


def main():
    try:
        string = input("please enter your equation:")
        print(run_calculator(string))
    # the try take care of the chance that the input will fail because of the EOF exception
    except EOFError as eof:
        print(eof)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
