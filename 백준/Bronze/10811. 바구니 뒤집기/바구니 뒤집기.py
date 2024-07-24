n, m = map(int, input().split())
x = [i for i in range(1, n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    x[a-1:b] = x[a-1:b][::-1]  # 슬라이스를 사용하여 역순으로 리스트 부분을 직접 변경

for i in x:
    print(i)
