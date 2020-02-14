def char_range(_char_1, _char_2):
    """To Generate the characters from _char_1 to _char_2 ."""
    for char in range(ord(_char_1), ord(_char_2) + 1):
        yield chr(char)


def isInE(string):
    stack = []
    Opened_Round_Bracket, Closed_Round_Bracket = "(", ")"
    i = 0
    while i < (len(string)):
        # If (string[i] ) the current char is an opened round bracket and add it to the stack"""
        if string[i] == Opened_Round_Bracket:
            stack.append(string[i])

        # If (string[i] ) the current char is a closed round bracket and pop it from the stack"""
        elif string[i] == Closed_Round_Bracket and len(stack) > 0:
            stack.pop()
        # If (string[i] ) the current char is an alphabet char so verify that is surrounded by opened/closed round
        # brackets""", if so pop the closed round bracket, if not the string is not in E
        elif string[i] in char_range('a', 'z') and 0 < i < len(string) - 1:
            if string[i - 1] == Opened_Round_Bracket and string[i + 1] == Closed_Round_Bracket and len(stack) > 0:
                stack.pop()
                i = i + 1
            else:
                return False
        else:
            return False
        i += 1

    return not len(stack)
