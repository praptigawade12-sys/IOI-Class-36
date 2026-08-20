m = [[6,9,1],
     [3,7,2],
     [4,7,0]]

ans = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(len(m)):
    for j in range(len(m[0])):
        ans[i][j] = m[j][i]

for r in ans:
    print(r)