# Given a string made up of the following brackets: ()[]{}, determine whether the brackets match
# Idea: Pop twice once you get a closing bracket

from collections import deque

def check_brackets(bracket_string: str) -> bool:
    if bracket_string is None or bracket_string == "":
        return False
    if len(bracket_string) % 2 == 1:
        return False

    stack = deque()
    prev = ""
    for bracket in bracket_string:
        curr = bracket
        stack.append(bracket)
        if curr == ")" or curr == "]" or curr == "}":
            if not pairChecker(stack):
                return False

    try:
        stack.pop()
        return False
    except IndexError:
        return True

def pairChecker(stack: deque) -> bool:
    b2 = stack.pop()
    try:
        b1 = stack.pop()
    except IndexError:
        return False
    if (b1 == "[" and b2 == "]") or (b1 == "{" and b2 == "}") or (b1 == "(" and b2 == ")"):
        return True
    return False

# driver
bracket_string = "(((((()()()"
print(bracket_string)
print(check_brackets(bracket_string))