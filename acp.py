m =[[2,7,4],
    [5,2,9],
    [1,4,6]]

for l in m:
    for e in l:
        print(e,end=" ")
    print()

sum = 0
print("Sum of Rows")

for i in range(len(m)):
    for j in range(len(m[0])):
        sum += m[i][j]
    print(sum,end = " ")
    sum = 0

