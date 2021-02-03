# def generateAcronym(stringInput):
#     result= ""
#     # put the first character from input into result
#     result += stringInput[0]
#     # loop through the string, look for a space characters, and put the characters after the space into the result
#     for i in range(1, len(stringInput), 1):
#         if stringInput[i] == " ":
#             result += (stringInput[i+1])
#         print(result.upper())
#         # return result.upper()
#     #  after we have our acronym upper case it .upper


# (generateAcronym("national basketball association"))


# # "nba"

def acronym2(stringInput):
    y= stringInput.split()
    print(y)
    for x in y:
        result +=x[0]
    return result.upper()



print(acronym2(" national basketball association"))