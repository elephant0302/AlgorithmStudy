w =  input()
lst = [0]*26

for i in w:
	lst[ord(i)-97] = w.count(i)
for i in lst:
	print(i, end=" ")