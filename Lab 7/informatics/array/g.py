n = int(input())
ls = list(map(int, input().split()))

for i in range(n//2):
    x = ls[-1*i-1]
    ls[-1*i-1] = ls[i]
    ls[i] = x


for i in range(n):
    print(ls[i], end = ' ')