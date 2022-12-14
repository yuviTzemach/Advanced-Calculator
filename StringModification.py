from ValidateFunctions import *


def erase_minus(string):
    """
    the function remove all the duplicates minus characters from the string, if there are no minus characters, returns
    the original string
    :param string: gets the string that the calculator supposed to calculate
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
    while len(string) > j:
        count_minus = 0
        # the while copying the first part of the string to the new string, until it gets to minus character
        # to check if the string got into duplicates minus characters
        while string[j] != '-' and j < len(string):
            new_string += string[j]
            j += 1
        # the while counting the number of the minus characters, to check if there are more than 1.
        # in addition, the while isn't copying this part of the string, to the new string.
        while string[j] == '-' and j < len(string):
            count_minus += 1
            j += 1
        # check if the count is even or odd - if even, the string don't supposed to have a minus character,
        # else - the string need to have only one minus character.
        # in both cases it is copy the next character in the string/
        if count_minus % 2 == 0:
            # if the character before the operand (this if is in the if that represent count as even number) is ')'
            # or a digit, the if add a plus character.
            if new_string != "" and (new_string[-1] == ')' or new_string[-1].isdigit()):
                new_string += '+'
            new_string += string[j]
        else:
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
    the function remove all the spaces from the string, by replacing each space with empty char
    :param string: gets the string that the calculator supposed to calculate
    """
    return string.replace(" ", "")


def validate_parentheses(string):
    """
    the function checks if every open parentheses has a close parentheses- if not, raise error
   :param string: gets the string that the calculator supposed to calculate
    """
    # the stack hold the open parentheses to check balance
    stack_parentheses = []
    for char in string:
        if char == '(':
            stack_parentheses.append(char)
        elif char is ')':
            if len(stack_parentheses) > 0:
                stack_parentheses.pop()
            else:
                raise SyntaxError("the string contains an unbalanced number of parentheses")

    if len(stack_parentheses) != 0:
        raise SyntaxError("the string contains an unbalanced number of parentheses")


def validate_chars(string):
    """
    the function checks if the chars in the string- if not, raise error
   :param string: gets the string that the calculator supposed to calculate
    """
    valid_operations = ['+', '-', '*', '/', '^', '%', '$', '&', '@', '~', '!', '#', '(', ')']
    for char in string:
        if not char.isdigit() and char not in valid_operations:
            raise SyntaxError("the string contains invalid chars")


def validate_operands(string):
    two_operands_operations = ['+', '-', '*', '/', '^', '%', '$', '&', '@']
    right_operations = ['!', '#']
    left_operation = ['~']
    if string[-1] in two_operands_operations or string[-1] in left_operation:
        raise SyntaxError("the string ends with an invalid operator")
    if string[0] in right_operations or (string[0] in two_operands_operations and string[0] != '-'):
        raise SyntaxError("the string starts with an invalid operator")

    for index, char in enumerate(string):
        if char in two_operands_operations:
            ValidateOperations.validate_trivial_operation(string[index - 1], string[index + 1])
        elif char in right_operations:
            ValidateOperations.validate_left_operand(string[index - 1])
        elif char in left_operation:
            ValidateOperations.validate_right_operand(string[index + 1])
