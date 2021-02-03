def sigma(num):
    #base case- when we know exactly what to return and don't have to do any further calculations
    if num == 1:
        return num
    else:
        #this is the recursion part of the function
        return num + sigma(num-1) #foreward progress is when the function calls itself with an argument that takes the function one step closer to the base case


print(sigma(12))


def factorial(num):
    if num == 1:
        return num
    else:
        return num * factorial(num-1)


factorial(5)