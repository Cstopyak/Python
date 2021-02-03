def reverseString(stringInput):
    newstring = ""
    for i in range(len(stringInput)-1, -1,-1):
        newstring += stringInput[i]

    return newstring

def isPalindrome(stringInput):
    stringInput = stringInput.replace(" ", "")
    if stringInput == reverseString(stringInput):
        return True
    else:
        return False
    #your code here
    #return either True or False

def isPal2(stringInput):
    for i in range(0, len(stringInput)//2, 1):
        if stringInput[i] != stringInput[len(stringInput)-1-i]:
            return False

    return True



print(reverseString("hello"))


# print(isPalindrome("hello"))
print(isPalindrome("race car"))
# print(isPalindrome("x 0 x"))


# print(isPal2("race car"))
# print(isPal2("potato"))

