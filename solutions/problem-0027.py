# Daily Coding Problem: Problem #27 [Easy]

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
# For example, given the string "([])[]({})", you should return true.
# Given the string "([)]" or "((()", you should return false.

# Time: O(n), where n = len(brackets)
# Space: O(n)

def is_balanced(brackets):
    s = []
    p = {"(":")", "[":"]", "{":"}"}

    for b in brackets:
        if b in p.keys():
            s.append(p[b])
        else:
            c = s.pop()
            if(c != b):
                return False

    if len(s) == 0:
        return True
    return False
        

if __name__ == '__main__':
    print('"([])[]({})" should return true: ' + str(is_balanced("([])[]({})")))
    print('"([)]" should return false: ' + str(is_balanced("([)]")))
    print('"((()" should return false: ' + str(is_balanced("((()")))