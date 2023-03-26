n = int(input())
ls = list(map(int, input().split()))
cnt = 0
for i in range(0, n):
    if i < n-1 and  i > 0 and ((ls[i] > ls[i-1] ) and (ls[i] > ls[i+1])):
       cnt += 1
print(cnt)
