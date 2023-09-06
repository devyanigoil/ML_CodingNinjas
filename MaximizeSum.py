#Given 2 sorted arrays (in increasing order), find a path through the intersections that produces maximum 
#sum and return the maximum sum.
#That is, we can switch from one array to another array only at common elements.
#If no intersection element is present, we need to take sum of all elements from the array with greater sum.
#
#input:
#6
#1 5 10 15 20 25
#5
#2 4 5 9 15
#
#output:
#81

m = int(input())
lim = [int(i) for i in input().split()]
n = int(input())
lin = [int(i) for i in input().split()]

i,j=0,0
sum1 = 0
sum2 = 0
result = 0
while (i<m and j<n):
    if lim[i]<lin[j]:
        sum1 += lim[i]
        i+=1
    elif lim[i]>lin[j]:
        sum2 += lin[j]
        j+=1
    else:
        result += max(sum1,sum2) + lim[i]
        sum1=0
        sum2=0
        i+=1
        j+=1

while i<m:
    sum1 += lim[i]
    i = i+1
    
while j<n:
    sum2 += lin[j]
    j+=1
    
result += max(sum1,sum2)  

print(result)