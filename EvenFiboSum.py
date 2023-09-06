#Generating Even Fibonacci numbers sum
#the foolowing code only generates even fibonacci numbers instead of the whole series

n = int(input())

a = 0
b = 2
c = 4*b+a
sum=2
while c<=n:
    sum = sum + c
    a = b 
    b = c
    c = 4*b + a

print(sum)