import pytest
from AdvancedCalculator import *


def testing_simple_errors():
    """
    testing if it raises SyntaxError or ArithmeticError when the input is not valid
    """
    assert pytest.raises(ArithmeticError, run_calculator, "8~8")  # 1
    assert pytest.raises(ArithmeticError, run_calculator, "3^*2")  # 2
    assert pytest.raises(SyntaxError, run_calculator, "/5+9")  # 3
    assert pytest.raises(SyntaxError, run_calculator, "#7+8")  # 4
    assert pytest.raises(ArithmeticError, run_calculator, "4~@3")  # 5


def testing_gibberish():
    """
    testing if it raises SyntaxError when the input contains chars that is not operators or operands
    """
    assert pytest.raises(SyntaxError, run_calculator, "hey;=;")
    assert pytest.raises(SyntaxError, run_calculator, "dbvjegsjc")
    assert pytest.raises(SyntaxError, run_calculator, "3f5ski+89by")


def testing_spaces_tabs_input():
    """
    testing if it raises SyntaxError when the input contains empty string, only white spaces string, only tabs string
    and a string with white spaces and tabs
    """
    assert pytest.raises(SyntaxError, run_calculator, "       ")
    assert pytest.raises(SyntaxError, run_calculator, "")
    assert pytest.raises(SyntaxError, run_calculator, " \t \t   \t")
    assert pytest.raises(SyntaxError, run_calculator, "\t")


def testing_simple_equations():
    """
    testing if the program returns the correct result for all the simple equations with all the possible operators
    """
    assert run_calculator("8+5") == "13.0"  # 1
    assert run_calculator("6-3") == "3.0"  # 2
    assert run_calculator("4*2") == "8.0"  # 3
    assert run_calculator("7/7") == "1.0"  # 4
    assert run_calculator("3^3") == "27.0"  # 5
    assert run_calculator("16%4") == "0.0"  # 6
    assert run_calculator("-2$7") == "7.0"  # 7
    assert run_calculator("5&-4") == "-4.0"  # 8
    assert run_calculator("8@4") == "6.0"  # 9
    assert run_calculator("~7") == "-7.0"  # 10
    assert run_calculator("5!") == "120.0"  # 11
    assert run_calculator("78#") == "15.0"  # 12
    assert run_calculator("78##") == "6.0"  # 13
    assert run_calculator("12#!") == "6.0"  # 14
    assert run_calculator("5!#") == "3.0"  # 15


def testing_complicated_equations():
    """
    testing if the program returns the correct result for all the complicated equations with all the possible operators
    """
    assert run_calculator("52# +   (8/4)/2  * 3!   + ~7 - 8@2") == "1.0"  # 1
    assert run_calculator("(5!-~7   +((8*  (4  $3))  /2) &  10)") == "137.0"  # 2
    assert run_calculator("(  5  5$  3! -((6 *   2  0) /  3 )  @ 1001)") == "-465.5"  # 3
    assert run_calculator("(((2^ 3 ) !  - 7!)  # *1   5)@( (1 2/ 3)  & 86)") == "137.0"  # 4
    assert run_calculator("(124 /  5)# # + (  -~ 3)! --7 *8+4 0") == "107.0"  # 5
    assert run_calculator("(99 8. 98##) ! @8! + ( ( 1 28 % 5) %3) -10") == "22670.0"  # 6
    assert run_calculator("82 0 @8 ! -((5 00 $ 6!) /3)^ 2 -8") == "-37038.0"  # 7
    assert run_calculator(" 35 /2 + (10*  5)# @  25 - 3! * 3^2.5") == "-61.030743608719376"  # 8
    assert run_calculator(" 5 * ------23.25# $ 15 - (  8  %  4) * (7! + ~720) / 10") == "75.0"  # 9
    assert run_calculator(" (20  5 * 16.  7 5) / 2 5 .5 - (6 ! ) @ (  5!)") == "-285.343137254902"  # 10
    assert run_calculator(" 2    / ----- 8 * ( 1  25 %2  0 )# -~( 3!  )") == "4.75"  # 11
    assert run_calculator(" 7!  $ ( 4 ! / 3 0 + 4 00  % 35 )   ----1 50") == "5190.0"  # 12
    assert run_calculator(" 1 50 2 #!  / 2 0 0 -- 285 + 2 4 * 12") == "774.6"  # 13
    assert run_calculator(" ( (12 ^ 0.2 5) ^2 ) & 7 - -  --5 / 2 0") == "3.7141016151377544"  # 14
    assert run_calculator("(1 - 2 5  0 + 15 @ 6! + 5 ^5 /8  0) /  400") == "0.39390625"  # 15
    assert run_calculator("  (5 2 548 & (14 ^ 4) - 7 21 * 22   )  @ - 10 0") == "11227.0"  # 16
    assert run_calculator(" 1 8  % 15 * 25 ^ 4 - 1 33 47 + 9 30 + (8  @  6 )") == "1159465.0"  # 17
    assert run_calculator(" ( ( 7 49 * 2 1^ 1.5 )  @ 0 .00 1 ) $ 10") == "36039.66705298021"  # 18
    assert run_calculator("( 845 6 / 3 5 * 19 ^ 3 * ( 26 %1 2 ) ^ 4 ) @ 1 00") == "13257125.2"  # 19
    assert run_calculator("(((~- -- 84 654## * 3 5) ^2 )  % 20 )  @ 700") == "352.5"  # 20
