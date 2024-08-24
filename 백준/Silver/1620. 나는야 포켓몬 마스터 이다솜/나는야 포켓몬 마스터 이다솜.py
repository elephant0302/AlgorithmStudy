import sys
input = sys.stdin.read
data = input().splitlines()

n, m = map(int, data[0].split())

dic = {}
rdic = {} 

for i in range(1, n + 1):
    dic[i] = data[i]  
    rdic[data[i]] = i  

results = []
for j in range(n + 1, n + m + 1):
    query = data[j]
    if query.isdigit(): 
        query = int(query)
        if 1 <= query <= n:
            results.append(dic[query]) 
    else:  
        if query in rdic:
            results.append(str(rdic[query]))  

print("\n".join(results))  
