

# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

# def biggie_size(Input):
#     for i in range(len(Input)):
#         if Input[i] > 0:
#             Input[i]= "biggie"
#     return Input
    
# print(biggie_size([-1, 3, 5, -5]))

# Count Positives - Given a list of numbers, 
# create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it
# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# [1,6,-4,-2,-7,2]

# def count_positives(input):
#     positivecount= 0
#     for i in range(0, len(input),1):
#         if input[i] > 0:
#             positivecount += 1
            
#     # print(positivecount)
#     input[-1] = positivecount
#     # return input

# print(count_positives([1,6,-4,-2,-7,2]))

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

# def sumTotal(Input):
#     temp = 0
#     for i in range(0, len(Input), 1):
#         temp+= Input[i]

#     return temp

# print(sumTotal([1,2,3,4]))

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

# def average(Input):
#     temp = 0
#     for i in range(len(Input)):
#         temp= temp + Input[i]

#     return temp / len(Input)

# print(input([1,2,3,4]))


# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

# def length(input):
#     return len(input)

# print(input([37,2,1,-9]))

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([37,2,1,-9]) should return -9
# Example: minimum([]) should return False

# def minimum(input):
#     currmin= input[0]
#     for i in range(1, len(input),1):
#         if input[i] < currmin:
#             currmin= input[i]

#     return currmin
# print(minimum([37,2,1,-9]))

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, 
# have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

# def maximum(input):
#     currmax = input[0]
#     for i in range(1, len(input),1):
#         if input[i] > currmax:
#             currmax = input[i]
#     return currmax

# print(maximum([37,2,1,-9]))

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

# def ultimate_analysis(input):
#     result = {
#         "sumtotal": sum(input),
#         "average": sum(input)/len(input),
#         "maximum": max(input),
#         "minimum": min(input),
#         "length": len(input)
#     }
#     return result

# print(ultimate_analysis([37,2,1,-9]))

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverse_list(input):
#     for i in range(len(input) -1, -1, -1):
#         input= input[::-1]
#         return input
        
# print(reverse_list([37,2,1,-9]))