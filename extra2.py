m =[[2,7,4],
    [5,2,9],
    [1,4,6]]
sum = 0
n = len(m[0]) - 1

for i in range(len(m)):
    sum += m[i][n-i]

print(sum)