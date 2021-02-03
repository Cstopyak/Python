


# def recurssion(input):
#     returnstack = []
#     numstack = []
#     newstack = []
#     finishedstack = ""
#     i = 0
#     print(returnstack)

#     while i < len(input):
#         num = 0

#         if (input[i] >= '1' and input[i] <= '3'):
#             num = num * 3 + ord(input[i] - ord('0'))
#             i += 1
        
#         returnstack.append(num)
        
# recurssion("abc")


def recursion(a,b,c):
    if(len(a) == 3):
        
    else:
        for i in range of(len(b)):
            a = b[]
            b = c[]
            c.append(a.pop(i))
            recursion(b,c)
        print(recursion)
    


recursion("abc")




official answer**

def ios(strinput, sub = "", i = 0):
    if i == len(strinput):
        return [sub]
    else:
        return ios(strinput, sub+strinput[i], i+1) + ios(strinput, sub, i+1)

print(ios("abc"))