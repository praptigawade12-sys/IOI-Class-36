m =[[2,7,4],
    [5,2,9],
    [1,4,6]]

sum_of_main = 0
sum_of_secd = 0

for i in range(len(m)):
    sum_of_main += m[i][i]

for i in range(len(m)):
    sum_of_secd += m[i][len(m[0])-1-i]

diff = abs(sum_of_main - sum_of_secd)

print(diff)
