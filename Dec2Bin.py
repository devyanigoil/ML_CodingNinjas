## Read input as specified in the question.
## Print output as specified in the question.

n = int(input())
temp = 0
s = ""
while n>=2:
    temp = n % 2
    s = str(temp) + s
    n = n//2
temp = n%2
s = str(temp) + s

print(s)