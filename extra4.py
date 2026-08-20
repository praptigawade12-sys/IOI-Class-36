m =[[2,7,4],
    [5,2,9],
    [1,4,6]]

ans = [[0,0,0],
       [0,0,0],
       [0,0,0]]

for i in range(3):
    for j in range(3-1,-1,-1):
        print(m[j][i],end=" ")
    print()

