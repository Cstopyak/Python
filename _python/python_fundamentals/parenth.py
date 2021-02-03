# "(()))" #unequal number of open vs closed
# ")(" #not valid b/c premature closing parens


# def parensValid(stringInput):
#     par, temp = "(,()),)"
#     for parensValid in stringInput:
#         if parensValid in temp:
#             par.append(parensValid)
#         elif len(par)== 0 or temp[par.pop] != parensValid:
#             return False
#         return len(par) == 0
            



# print(parensValid("(()))"))

def parensValid(s):
    parensCounter = 0
    for i in range(len(s)):
        if parensCounter < 0:
            return False
        if s[i] == "(":
            parensCounter += 1
        elif s[i] == ")":
            parensCounter -= 1
    if parensCounter == 0:
        return True
    return False