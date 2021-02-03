# “ Greatest Common Factor
# Given two integers, create rGCF(num1,num2) to recursively determine Greatest Common Factor (the largest integer dividing evenly into both). Greek mathematician Euclid demonstrated these facts:
    gcf(a,b) == a, if a == b;
      gcf(a,b) == gcf(a-b,b), if a>b;
      gcf(a,b) == gcf(a,b-a), if b>a.

# Second: rework facts #2 and #3 to reduce stack consumption and expand rGCF’s reach. You should be able to compute rGCF(123456,987654).”

# Excerpt From: Martin Puryear. “Algorithm Challenges: E-book for Dojo Students.” iBooks.

def gcf(a, b):
    if(a > b):
        c = a % b
        if(c == 0):
            return b
        else:
            return gcf(b, c)
    elif(a < b):
        c = b % a
        if(c == 0):
            return a
        else:
            return gcf(a,c)
    else:
        return a

print(gcf(123456, 987654))