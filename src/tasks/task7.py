# given a string including only open_parentheses and close_parentheses check if the sequence is regular
# regular means that numbers and signs inserted into the pairs would be valid expressions
# can't start on close_parentheses
# can't end on open parentheses
# each open_parentheses must have a close_parentheses

def regularSequence(s):
    # conditional to rule out start and end edge cases:
    if len(s) == 0:
        return True
    elif s[0] == ")" or s[len(s) -1] == "(":
        return False
    # initialize open_paren at 0
    open_paren = 0
    # loop through the string and increment open_paren on each occurence
    for paren in s:
        # increment open_paren each time paren == "("
        if paren == "(":
            open_paren += 1
        # decrement open_paren each time paren == ")"
        else:
            open_paren -= 1
    # after looping through the sequence if open_paren == 0 the sequence is regular, return True
    if open_paren == 0:
        return True
    # else(implicitly open_paren != 0) return False
    else:
        return False

print(regularSequence("()()(())")) # True
print(regularSequence("()()())"))  # False
print(regularSequence(""))

string = "s)()()()()()()()()(e"
print(string[len(string) - 1])
print(string[0])