n = int(input())
ls = list(map(int, input().split()))
cnt = 0
for i in range(0, n):
    if ls[i] > 0:
       cnt += 1
print(cnt)
