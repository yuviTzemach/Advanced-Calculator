from ExpressionParser import *
from Definitions import *

"""
The class is calculating the priority of each operator.
"""


def factorial_sum_tilda_priority(string):
    """
    The function is calculating the priority '!', '#' and '~' - in this case, 6 priority
    @param string: the string
    returns by calling the one_operand_operator_priority function with the string and the operator index
    """
    factorial_index = string.find('!')
    sum_index = string.find('#')
    tilda_index = string.find('~')
    operators_index = {factorial_index: '!', sum_index: '#', tilda_index: '~'}
    return one_operand_operator_priority(string, operators_index)


def power_priority(string):
    """
    The function is calculating the priority '^' - in this case, 3 priority
    @param string: the string
    if power_index != -1, returns true, the operator, and calling the split_expression_to_two_operands function with
    the string and the index of the operator
    else, return false, '', ()
    """
    power_index = string.find('^')
    if power_index == -1:
        return False, '', ()
    else:
        return True, '^', ExpressionParser.split_expression_to_two_operands(string, power_index)


def modulo_priority(string):
    """
    The function is calculating the priority '%' - in this case, 4 priority
    @param string: the string
    if power_index != -1, returns true, the operator, and calling the split_expression_to_two_operands function with
    the string and the index of the operator
    else, return false, '', ()
    """
    modulo_index = string.find('%')
    if modulo_index == -1:
        return False, '', ()
    else:
        return True, '%', ExpressionParser.split_expression_to_two_operands(string, modulo_index)


def min_max_avg_priority(string):
    """
    The function is calculating the priority '&', '$' and '@' - in this case, 5 priority
    @param string: the string
    returns by calling the two_operands_operator_priority function with the string and the operators index
    """
    min_index = string.find('&')
    max_index = string.find('$')
    avg_index = string.find('@')
    operators_index = {min_index: '&', max_index: '$', avg_index: '@'}
    return two_operands_operator_priority(string, operators_index)


def mul_div_priority(string):
    """
    The function is calculating the priority '*', and '/' - in this case, 2 priority
    @param string: the string
    returns by calling the two_operands_operator_priority function with the string and the operators index
    """
    mul_index = string.find('*')
    div_index = string.find('/')
    operators_index = {mul_index: '*', div_index: '/'}
    return two_operands_operator_priority(string, operators_index)


def plus_minus_priority(string):
    """
    The function is calculating the priority '+', and '-' - in this case, 1 priority
    @param string: the string
    returns by calling the two_operands_operator_priority function with the string and the operators index
    """
    plus_index = string.find('+')
    minus_index = ExpressionParser.find_first_minus_operator(string)
    operators_index = {plus_index: '+', minus_index: '-'}
    return two_operands_operator_priority(string, operators_index)


def two_operands_operator_priority(string, operators_index):
    """
    The function find the earliest operator & index in the current "level" of operators.
    If found one:
    returns the operator and the operands that were extracted from the sides of the operator.
    @param string: the expression to act on
    @param operators_index: a dictionary of index - operator.
    (see 'find_first_operator_to_execute' for more explanation)
    returns If found an operator:
            True, operator, (left_operand, left_operand_index, right_operand, right_operand_index)
            If not:
            False, '', ()
    """
    # Find the first occurrence of a relevant operator
    operator, lowest_index = ExpressionParser.find_first_operator_to_execute(operators_index)

    # if there isn't such one - get back without doing anything
    if lowest_index == -1:
        return False, '', ()

    return True, operator, ExpressionParser.split_expression_to_two_operands(string, lowest_index)


def one_operand_operator_priority(string, operators_index):
    """
    The function find the earliest operator & index in the current "level" of operators.
    If found one:
    returns the operator and the operands that were extracted from the sides of the operator.
    @param string: the expression to act on
    @param operators_index: a dictionary of index - operator.
    (see 'find_first_operator_to_execute' for more explanation)
    returns If found an operator:
            True, operator, (left_operand, left_operand_index, right_operand, right_operand_index)
            If not:
            False, '', ()
    """
    # Find the first occurrence of a relevant operator
    operator, lowest_index = ExpressionParser.find_first_operator_to_execute(operators_index)
    # if there isn't such one - get back without doing anything
    if lowest_index == -1:
        return False, '', ()
    if operator in right_operations:
        return True, operator, ExpressionParser.split_expression_to_left_operand(string, lowest_index)
    elif operator in left_operation:
        return True, operator, ExpressionParser.split_expression_to_right_operand(string, lowest_index)
