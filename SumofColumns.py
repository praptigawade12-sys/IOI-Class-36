m =[[2,7,4],
    [5,2,9],
    [1,4,6]]

ans = 0

for r in m:
    print(r)

for i in range(len(m)):
    for j in range(len(m[0])):
        ans += m[j][i]

    print(ans,end = " ")
    ans = 0