h, m = map(int, input().split())
resulth = 0
resultm = 0
if m >= 45:
    resultm = m - 45
    resulth = h
    print(str(resulth) + " " + str(resultm))
elif h > 0 and m < 45:
    resultm = 60 + (m - 45)
    resulth = h - 1
    print(str(resulth) + " " + str(resultm))
elif h == 0 and m < 45:
    resulth = 23
    resultm = 60 + (m - 45)
    print(str(resulth) + " " + str(resultm))
