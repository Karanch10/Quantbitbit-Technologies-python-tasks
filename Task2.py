# Valid Parentheses Checker 

def is_valid(s: str) -> bool:
    open_brackets = "({["
    close_brackets = ")}]"
    stack = []
    for i in s:
        if i in open_brackets:
            stack.append(i)
        elif i in close_brackets:
            if not stack or open_brackets.index(stack.pop()) != close_brackets.index(i):
                return False
    return not stack

s = "{[()]}"
print(is_valid(s))  # Output: True
s = "{[(])}"
print(is_valid(s))  # Output: False
