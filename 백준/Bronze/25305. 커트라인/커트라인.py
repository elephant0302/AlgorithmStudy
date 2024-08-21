n,m = map(int,input().split())

score = list(map(int,input().split()))

score.sort()

score.reverse()

print(score[m-1])

