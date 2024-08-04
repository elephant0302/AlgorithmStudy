n = int(input())

# 1번에 4개, 2번에 16개 3번에 64개
# 한줄에 2개, 4개, 8개

result = ( 2 ** n + 1 ) ** 2
print(result)