# “ Recursive Fibonacci
# Write rFib(num). Recursively compute and return numth Fibonacci value. As earlier, treat first two (num = 0, num = 1) Fibonacci vals as 0 and 1. Examples: rFib(2) = 1 (0+1); rFib(3) = 2 (1+1); rFib(4) = 3 (1+2); rFib(5) = 5 (2+3). rFib(3.65) = rFib(3) = 2, rFib(-2) = rFib(0) = 0.”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.


def rFib(n):
    if n <= 1:
        return n
    else:
        return (rFib(n-1) + rFib(n-2))

funnum= 10

if funnum<=0:
        pass
else:
    for x in range(funnum):
        print(rFib(x))


    #recursive case with forward progress (recursion is when the function calls itself)


rFib(1)