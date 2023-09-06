#Given a string S, find the largest substring with no repetition i.e. largest substring which contain all unique characters.

#input:
#abcdabceb

#output:
#dabce

s = input()
d1 = {}
d2 = {}
ans = ""
length = 0
max_val = 0
for j in range(len(s)-1):
	for i in range(j,len(s)):
		if(s[i] in d1):
			if(length>max_val):
				max_val = length
				d2[ans]=length
			d1.clear()
			ans=""
			length=0
			break
		else:
			d1[s[i]]=1
			ans = ans+s[i]
			length = length+1
			
for i in d2:
    if max_val==d2[i]:
        print(i)
        break