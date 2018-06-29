from Stack import *


def paratheses_checker(data):
    '''Balanced parantheses checker function'''
    s = Stack()
    balanced = True
    index = 0
    while index < len(data) and balanced:
        symbol = data[index]
        print(symbol)
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")":
            if s.is_empty():
                balanced = False
            else:
                r=""
                while r!="(" :
                    if(s.is_empty()):
                        balanced = False
                        break
                    s.pop()
        index = index + 1

    # check if stack is empty and symbols are balanced
    if balanced and s.is_empty():
        return True
    else:
        return False


## Example
#print(paratheses_checker('((())))'))