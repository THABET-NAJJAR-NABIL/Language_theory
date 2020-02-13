def char_range(_char_1, _char_2):
    """To Generate the characters from _char_1 to _char_2 ."""
    for c in range(ord(_char_1), ord(_char_2) + 1):
        yield chr(c)


def isInE(string):
    stack = []
    Opened_Round_Bracket, Closed_Round_Bracket = "(", ")"
    i = 0
    while i < (len(string)):
        if string[i] == Opened_Round_Bracket:
            stack.append(string[i])
        elif string[i] == Closed_Round_Bracket and len(stack) > 0:
            stack.pop()
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
