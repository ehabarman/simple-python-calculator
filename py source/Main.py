import sys
import Stack
from balanced_parantheses import *
from postfix_eval import *
from infix_to_postfix import *
from decimal_to_binary import *


if __name__ == '__main__':
    expr = "(((5)))"
    print(paratheses_checker(expr))
