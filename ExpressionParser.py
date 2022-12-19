class ExpressionParser:

    def is_calculation_finish(expr):
        """
        @param expr: the expression
        returns if there are no more calculations left to do - return tuple of True and the final expression.
        otherwise, return false and the original string.
        """
        # Don't let the float point to disturb
        int_expr = expr.replace('.', '')
        # if the expression is a number
        if int_expr.isdigit():
            return True, expr
        # if the expression is a negative number
        elif int_expr[0] == '-' and int_expr[1:].isdigit():
            return True, expr
        # if the expression is a number except the open/close parenthesis that was left after the splits.
        elif int_expr[0] == '(' and int_expr[1:].isdigit():
            return True, expr[1:]
        elif int_expr[-1] == ')' and int_expr[:-1].isdigit():
            return True, expr[:-1]
        elif int_expr[0] == '(' and int_expr[-1] == ')' and int_expr[1:-1].isdigit():
            return True, expr[1:-1]
        # if the expression is negative and has parenthesis '-(something)'
        elif int_expr[0] == '-' and int_expr[1] == '(' and int_expr[-1] == ')':
            # if "something" is '-X', meaning -(-X), return X
            if len(int_expr) >= 5 and int_expr[2] == '-' and int_expr[3:-1].isdigit():
                return True, expr[3:-1]
            # if "something" is 'X', meaning -(X), return -X
            elif len(int_expr) >= 4 and int_expr[2:-1].isdigit():
                return True, "-" + expr[2:-1]
        return False, expr

    def find_expression_before_close_parenthesis(expr, left_operand_index):
        """
        The function extracts the expression/number that placed before the given close parenthesis index.
        @param expr: the expression
        @param left_operand_index: index of the close parenthesis
        returns tuple of (the extracted left operand, the index of the first char of the operand)
        @raise SyntaxError if the parenthesis aren't balanced
        """
        # save the close parenthesis index
        close_index = left_operand_index
        # go back to the last char (but the first one before the close parenthesis)
        left_operand_index -= 1
        # counter to find the balance between close and open parenthesis.
        # cnt = 0 means balance, cnt < 0 means more open chars, cnt > 0 means more close.
        # counter start with 1 because we already found the first close parenthesis.
        open_close_cnt = 1
        while left_operand_index >= 0:
            # found open parenthesis - adjust the counter and check if we are on balance parenthesis situation.
            if expr[left_operand_index] == '(':
                open_close_cnt -= 1
                # found the full expression between the parenthesis
                if open_close_cnt == 0:
                    return expr[left_operand_index + 1:close_index], left_operand_index
            # found close parenthesis - adjust the counter
            elif expr[left_operand_index] == ')':
                open_close_cnt += 1
            # continue searching after the full expression
            left_operand_index -= 1
        # parenthesis aren't balanced
        raise SyntaxError("didn't find matching parenthesis")

    def find_expression_after_open_parenthesis(expr, right_operand_index):
        """
        The function extracts the expression/number that starts after the given open parenthesis index.
        @param expr: the expression
        @param right_operand_index: index of the open parenthesis
        returns tuple of (the extracted right operand, the index of the last char of the operand)
        @raise SyntaxError if the parenthesis aren't balanced
        """
        # save the open parenthesis index
        open_index = right_operand_index
        # The function needs to support also an expression that surrounded by parenthesis but also have a negative sign
        # before it.
        # For example, after an operator there is '-(expression)' and not the regular (expression)
        # Thus, to support this - if the first char of the right operand is '-' and the next char is '(':
        # the 'open_index' will represent actually the index of the negative sign
        # and the 'right_operand_index' should advance to the open parenthesis
        if expr[right_operand_index] == '-':
            right_operand_index += 1
        # advance to the first char after the open parenthesis
        right_operand_index += 1
        # counter to find the balance between close and open parenthesis.
        # cnt = 0 means balance, cnt < 0 means more open chars, cnt > 0 means more close.
        # counter start with -1 because we already found the first open parenthesis.
        open_close_cnt = -1
        while right_operand_index < len(expr):
            # found close parenthesis - adjust the counter and check if we are on balance parenthesis situation.
            if expr[right_operand_index] == ')':
                open_close_cnt += 1
                # found the full expression between the parenthesis
                if open_close_cnt == 0:
                    return expr[open_index: right_operand_index + 1], right_operand_index
            # found open parenthesis - adjust the counter
            elif expr[right_operand_index] == '(':
                open_close_cnt -= 1
            # continue searching after the full expression
            right_operand_index += 1
        # parenthesis aren't balanced
        raise SyntaxError("didn't find matching parenthesis")

    def find_left_number(expr, left_operand_index):
        """
        The function extracts the number that ends at the given index.
        @param expr: the expression
        @param left_operand_index: the index that we need to start looking backwards towards a number
        returns tuple of (the extracted left operand number, the index of the first char of the operand number)
        """
        # save the "last" digit index
        starting_index = left_operand_index
        # get back to the previous char (because I will scan the number backwards)
        left_operand_index -= 1
        # counter of floating point occurrences to check that the number is valid
        # must end up on 0 or 1
        float_point_cnt = 0
        # continue searching after the full number we can extract
        while left_operand_index >= 0 and (expr[left_operand_index].isdigit() or expr[left_operand_index] == '.'):
            # found '.'
            if expr[left_operand_index] == '.':
                float_point_cnt += 1
                if float_point_cnt > 1:
                    raise SyntaxError("invalid left number - has more than 1 floating point in it")
                # (keep scanning the expression because one floating point is OK)
            left_operand_index -= 1
        # check if the char we stopped on it is a '-' char
        if expr[left_operand_index] == '-':
            if left_operand_index == 0:
                # the '-' char is the first char in the given expression
                # so it acts as a negative sign and not as a minus operator
                # therefore, return the number (including the negative sign) and the starting index of it
                return expr[left_operand_index: starting_index + 1], left_operand_index
            elif left_operand_index >= 1 and \
                    (expr[left_operand_index - 1] != ')' and not expr[left_operand_index - 1].isdigit()):
                # the '-' char is not coming after a ')' or a digit in the given expression
                # so it acts as a negative sign and not as a minus operator
                # therefore, return the number (including the negative sign) and the starting index of it
                return expr[left_operand_index: starting_index + 1], left_operand_index
        # adjust the index to "point" on the first digit
        left_operand_index += 1
        # return the extracted number and the starting index of it
        return expr[left_operand_index: starting_index + 1], left_operand_index

    def find_right_number(expr, right_operand_index):
        """
        The function extracts the number that starts at the given index.
        @param expr: the expression
        @param right_operand_index: the index that we need to start looking toward a number
        returns tuple of (the extracted right operand number, the index of the last char of the operand number)
        """
        # save the "first" digit index
        starting_index = right_operand_index
        # advance to the next char
        right_operand_index += 1
        # counter of floating point occurrences to check that the number is valid
        # must end up on 0 or 1
        float_point_cnt = 0
        # continue searching after the full number we can extract
        while right_operand_index < len(expr) and (expr[right_operand_index].isdigit() or
                                                   expr[right_operand_index] == '.'):
            # found '.'
            if expr[right_operand_index] == '.':
                float_point_cnt += 1
                if float_point_cnt > 1:
                    raise SyntaxError("invalid right number - has more than 1 floating point in it")
                # (keep scanning the expression because one floating point is OK)
            right_operand_index += 1
        number = expr[starting_index:right_operand_index]
        return number, right_operand_index - 1

    def find_left_operand(expr, operator_index):
        """
        The function extracts the operand that placed at the left of the given index.
        @param expr: the expression
        @param operator_index: the index that we need to start searching for left operand
        returns tuple of (the extracted left operand, the index of the first char of the operand)
        @raise SyntaxError if an invalid char was found
        """
        # go back to the first char before the operator
        left_operand_last_index = operator_index - 1
        # if the first char before (left to) the operator is digit, extract the full number
        if expr[left_operand_last_index].isdigit():
            number, left_operand_first_index = ExpressionParser.find_left_number(expr, left_operand_last_index)
            return number, left_operand_first_index, left_operand_last_index
        # if the first char before the operator is ')', extract the full expression between the parenthesis
        elif expr[left_operand_last_index] == ')':
            exp, left_operand_first_index = ExpressionParser.find_expression_before_close_parenthesis \
                (expr, left_operand_last_index)
            return exp, left_operand_first_index, left_operand_last_index
        raise SyntaxError("invalid char left to %s operator" % expr[operator_index])

    def find_right_operand(expr, operator_index):
        """
        The function extracts the operand that placed at the right of the given index.
        @param expr: the expression
        @param operator_index: the index that we need to start searching for right operand
        returns tuple of (the extracted right operand, the index of the last char of the operand)
        @raise SyntaxError if an invalid char was found
        """
        # advance to the first char after the operator
        right_operand_first_index = operator_index + 1
        # if the first char after the operator is:
        # digit OR negative sign and then a digit -> extract the full number
        if expr[right_operand_first_index].isdigit() or \
                (right_operand_first_index + 1 < len(expr) and expr[right_operand_first_index] == '-' and
                 expr[right_operand_first_index + 1].isdigit()):
            number, right_operand_last_index = ExpressionParser.find_right_number(expr, right_operand_first_index)
            return number, right_operand_first_index, right_operand_last_index
        # if the first char after the operator is:
        # '(' OR negative sign and then a '(' -> extract the full expression between the parenthesis
        elif expr[right_operand_first_index] == '(' or \
                (right_operand_first_index + 1 < len(expr) and expr[right_operand_first_index] == '-'
                 and expr[right_operand_first_index + 1] == '('):
            exp, right_operand_last_index = \
                ExpressionParser.find_expression_after_open_parenthesis(expr, right_operand_first_index)
            return exp, right_operand_first_index, right_operand_last_index
        raise SyntaxError("invalid char right to %s operator" % expr[operator_index])

    def split_expression_to_left_operand(expr, operator_index):
        left_operand, left_operand_first_index, left_operand_last_index = \
            ExpressionParser.find_left_operand(expr, operator_index)
        return operator_index, left_operand, left_operand_first_index

    def split_expression_to_right_operand(expr, operator_index):
        right_operand, right_operand_first_index, right_operand_last_index = \
            ExpressionParser.find_right_operand(expr, operator_index)
        return operator_index, right_operand, right_operand_last_index

    def split_expression_to_two_operands(expr, operator_index):
        """
        The function split the expression for the two operands that on the sides of the operator.
        In addition to the extracted operands, the function finds:
        - the index of the first char of the left operand (named "left_operand_first_index")
        - the index of the last char of the right operand (named "right_operand_last_index")
        For example, if the expression is "3*(5+2)+10" and the operator is '*' the function will return:
            left_operand = 3, left_operand_index = 0, right_operand = (5+2), right_operand_index = 6
        @param expr: the expression
        @param operator_index: the index of the operator the function splits by
        returns a tuple of left_operand, left_operand_first_index, left_operand_last_index, right_operand,
        right_operand_first_index, right_operand_last_index
        """
        left_operand, left_operand_first_index, left_operand_last_index = \
            ExpressionParser.find_left_operand(expr, operator_index)
        right_operand, right_operand_first_index, right_operand_last_index = \
            ExpressionParser.find_right_operand(expr, operator_index)
        return left_operand, left_operand_first_index, right_operand, right_operand_last_index

    def find_first_minus_operator(expr):
        """
        The function searching for the first '-' char that represents a minus operator and not a negative sign
        A minus operator is identified by locating right after a digit or a ')'.
        @param expr: the expression to look for minus operator in it
        @return the index we found
        """
        minus_index = 0
        while minus_index < len(expr):
            if expr[minus_index] == '-':
                # if the first char in the expression is '-', it cannot represent a minus operator
                if minus_index != 0:
                    # A minus operator is identified by locating right after a digit or a ')'.
                    if expr[minus_index - 1].isdigit() or expr[minus_index - 1] == ')':
                        return minus_index
            minus_index += 1
        # didn't find any minus operator
        return -1

    def find_first_operator_to_execute(operators_index):
        """
        The function receives a dictionary of {index1:operator1, index2:operator2 ...}.
        The function searches for the lowest index (excluding -1) and returns this index and its matching operator
        @param operators_index: the dictionary.
        returns a tuple of the lowest index and its operator.
        NOTE: if there isn't an operator to execute - return -1 and ''.
        For example, receiving a dictionary of { 4:"$", -1:"@", 2:"&" } will return (2, '&').
        """
        # remove occurrences of -1.
        # -1 as the index value means that the index is not exist in the given expression
        operators_index = {index: operator for (index, operator) in operators_index.items() if index != -1}
        # if the dictionary is empty now - didn't find any relevant operators
        if len(operators_index) == 0:
            return '', -1
        lowest_index = min(operators_index)
        operator = operators_index[lowest_index]
        return operator, lowest_index

    def replace_expression_with_result(expr, left_operand_first_index, right_operand_last_index, operator_result):
        """
        The function replaces the expression with its calculated result.
        @param expr: the expression
        @param left_operand_first_index: the index of the first char of the left operand
        @param right_operand_last_index: the index of the last char of the right operand
        @param operator_result: the result to fill in instead if its related expression.
        NOTE: if I will face two consecutive '-' chars, I will replace them with '+'
        returns the new expression
        """
        # check if there are redundant parentheses that surrounding the number
        if (left_operand_first_index - 1 >= 0 and right_operand_last_index + 1 < len(expr)) and \
                (expr[left_operand_first_index - 1] == '(' and expr[right_operand_last_index + 1] == ')'):
            # pass on the parentheses on both sides
            left_operand_first_index -= 1
            right_operand_last_index += 1
        # check if there is another char before the left operand
        # and if it is '-' char
        # and if the operator_result is negative
        if left_operand_first_index - 1 >= 0 and \
                (operator_result[0] == '-' and expr[left_operand_first_index - 1] == '-'):
            # if the consecutive '-' comes at the first of the string, remove them because they offset each other
            if expr[:left_operand_first_index - 1] == "":
                return operator_result[1:] + expr[right_operand_last_index + 1:]
            else:
                # fill in the result (and replace the two consecutive '-' into '+' on the way)
                return expr[:left_operand_first_index - 1] + "+" + operator_result[1:] + expr[
                                                                                         right_operand_last_index + 1:]
        # fill in the result
        return expr[:left_operand_first_index] + operator_result + expr[right_operand_last_index + 1:]
