import sys

"""
Program which takes in a string as a command line argument and evaluates whether its parentheses are properly matched,
disregarding any other characters it encounters
Ex: (()) returns True, and (1*(2+3)) returns True as well
Ex: )() returns False, and )1*2+(3) returns False as well
Ex: )( returns False, and )1*2+3( returns False as well
"""

def matched_parens(s):
    paren = 0
    for c in s:
        if c=="(":
            paren+=1
        elif c==")":
            paren-=1
            if paren<0:
                return False
        else:
            continue
    if paren==0:
        return True
    else:
        return False

s = sys.argv[1]
print(matched_parens(s))
