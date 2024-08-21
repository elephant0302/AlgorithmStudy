import sys

n = int(sys.stdin.readline())

ws = []

for i in range(n):
    word = sys.stdin.readline().strip()
    ws.append(word)
    
wss=set(ws)
ws = list(wss)
ws.sort(key = lambda x : (len(x), x))

for x in ws:
    print(x)