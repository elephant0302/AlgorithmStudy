cnt =int(input())
n_list=list(map(int,input().split()))
find = int(input())
answer =0
for i in range(cnt):
	if n_list[i] == find:
		answer+=1
print(answer)
		