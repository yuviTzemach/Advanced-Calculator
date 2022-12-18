from ValidateFunctions import *
from Definitions import *


def erase_minus(string):
    """
    the function remove all the duplicates minus characters from the string, if there are no minus characters, returns
    the original string
    @param string: gets the string that the calculator supposed to calculate
    returns the new string - the same string but without the duplicates minus characters
    """
    if '-' not in string:
        return string
    if string == "-" or string[-1] == '-':
        raise SyntaxError("the string has incorrect minus characters usage")
    j = 0
    # the function create new string 'new_string', that get the same string as the first, but without the duplicates
    # minus characters, and returns it
    new_string = ""
    while j < len(string):
        count_minus = 0
        # the while copying the first part of the string to the new string, until it gets to minus character
        # to check if the string got into duplicates minus characters
        while j < len(string) and string[j] != '-':
            new_string += string[j]
            j += 1
        # the while counting the number of the minus characters, to check if there are more than 1.
        # in addition, the while isn't copying this part of the string, to the new string.
        while j < len(string) and string[j] == '-':
            count_minus += 1
            j += 1
        # check if the count is even or odd - if even, the string don't supposed to have a minus character,
        # else - the string need to have only one minus character.
        # in both cases it is copy the next character in the string/
        if count_minus % 2 == 0 and count_minus != 0:
            # if the character before the operand (this if is in the if that represent count as even number) is ')'
            # or a digit, or the '!' or '#' operators -  the if add a plus character.
            if new_string != "" and (
                    (new_string[-1] == ')' or new_string[-1].isdigit()) or new_string[-1] in right_operations):
                new_string += '+'
            new_string += string[j]
        elif count_minus % 2 != 0:
            # if there is plus character before the minus character, it doesn't matter and that's why, I can remove it
            # from the string.
            if new_string != "" and new_string[-1] == '+':
                new_string = new_string[:-1]
            new_string += '-'
            new_string += string[j]
        j += 1

    return new_string


def erase_space(string):
    """
    the function remove all the spaces and the tabs from the string, by replacing each space and tab with empty char
    @param string: gets the string that the calculator supposed to calculate
    """
    string1 = string.replace("\t", "")
    string1 = string1.replace(" ", "")
    if string1 == "":
        raise SyntaxError("white spaces expression is invalid")
    return string1


def validate_parentheses(string):
    """
    the function checks if every open parentheses has a close parentheses- if not, raise error
    @param string: gets the string that the calculator supposed to calculate
    """
    # the stack hold the open parentheses to check balance
    stack_parentheses = []
    for char in string:
        if char == '(':
            stack_parentheses.append(char)
        elif char == ')':
            if len(stack_parentheses) > 0:
                stack_parentheses.pop()
            else:
                return False
    if len(stack_parentheses) != 0:
        return False
    return True


def validate_chars(string):
    """
    the function checks if the chars in the string- if not, raise error
    @param string: gets the string that the calculator supposed to calculate
    """
    valid_operations = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', '(', ')']
    for char in string:
        if not char.isdigit() and char not in valid_operations and char != '.':
            raise SyntaxError("the string contains invalid chars")

    if not any(char.isdigit() for char in string):
        raise SyntaxError("the string isn't contain any numbers")


def validate_operands(string):
    if string[-1] in two_operands_operations or string[-1] in left_operation:
        raise SyntaxError("the string ends with an invalid operator")
    if string[0] in right_operations or (string[0] in two_operands_operations and string[0] != '-'):
        raise SyntaxError("the string starts with an invalid operator")
    for index, char in enumerate(string):
        if char in two_operands_operations:
            if char == '-':
                # if the '-' char is not coming after a ')' or a digit in the given expression
                # it acts as a negative sign and not as a minus operator
                # therefore, skip this validation because the '-' that was found is not a minus operator
                if string[index - 1] != ')' and not string[index - 1].isdigit():
                    continue
            ValidateOperations.validate_trivial_operation(string[index - 1], string[index + 1])
        elif char in right_operations:
            ValidateOperations.validate_left_operand(string[index - 1])
            if index + 1 < len(string):
                ValidateOperations.validate_right_operand_for_right_operator(string[index + 1])
        elif char in left_operation:
            if index - 1 >= 0:
                ValidateOperations.validate_left_operand_for_left_operator(string[index - 1])
            ValidateOperations.validate_right_operand(string[index + 1])
