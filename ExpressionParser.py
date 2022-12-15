class ExpressionParser:

    def is_calculation_finish(expr):
        """
        @param expr: the expression
        returns if there are no more calculations left to do - return tuple of True and the final expression.
        otherwise, return false and the original string.
        """
        # if the expression is a number
        if expr.isdigit():
            return True, expr

        # if the expression is a number except the open/close parenthesis that was left after the splits.
        elif expr[0] == '(' and expr[1:].isdigit():
            return True, expr[1:]
        elif expr[-1] == ')' and expr[:-1].isdigit():
            return True, expr[:-1]
        elif expr[0] == '(' and expr[-1] == ')' and expr[1:-1].isdigit():
            return True, expr[1:-1]

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
        # advance to the first char
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
                    return expr[open_index: right_operand_index + 1], right_operand_index + 1

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

        # continue searching after the full number we can extract
        while left_operand_index >= 0 and expr[left_operand_index].isdigit():
            left_operand_index -= 1

        # adjust the index to "point" on the first digit
        left_operand_index += 1
        number = expr[left_operand_index:starting_index + 1]
        return number, left_operand_index

    def find_right_number(expr, right_operand_index):
        """
        The function extracts the number that starts at the given index.
        @param expr: the expression
        @param right_operand_index: the index that we need to start looking toward a number
        returns tuple of (the extracted right operand number, the index of the last char of the operand number)
        """
        # save the "first" digit index
        starting_index = right_operand_index

        # continue searching after the full number we can extract
        while right_operand_index < len(expr) and expr[right_operand_index].isdigit():
            right_operand_index += 1

        number = expr[starting_index:right_operand_index]
        return number, right_operand_index

    def find_left_operand(expr, operator_index):
        """
        The function extracts the operand that placed at the left of the given index.
        @param expr: the expression
        @param operator_index: the index that we need to start searching for left operand
        returns tuple of (the extracted left operand, the index of the first char of the operand)
        @raise SyntaxError if an invalid char was found
        """
        # go back to the first char before the operator
        left_operand_index = operator_index - 1

        # if the first char before the operator is digit, extract the full number
        if expr[left_operand_index].isdigit():
            number, left_operand_index = ExpressionParser.find_left_number(expr, left_operand_index)
            # print("left number : " + number)
            return number, left_operand_index

        # if the first char before the operator is ')', extract the full expression between the parenthesis
        elif expr[left_operand_index] == ')':
            exp, left_operand_index = ExpressionParser.find_expression_before_close_parenthesis(expr,
                                                                                                left_operand_index)
            # print("left exp : " + exp)
            return exp, left_operand_index

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
        right_operand_index = operator_index + 1

        # if the first char after the operator is digit, extract the full number
        if expr[right_operand_index].isdigit():
            return ExpressionParser.find_right_number(expr, right_operand_index)

        # if the first char after the operator is '(', extract the full expression between the parenthesis
        elif expr[right_operand_index] == '(':
            return ExpressionParser.find_expression_after_open_parenthesis(expr, right_operand_index)

        raise SyntaxError("invalid char right to %s operator" % expr[operator_index])
