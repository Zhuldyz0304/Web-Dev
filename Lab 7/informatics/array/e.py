n = int(input())
ls = list(map(int, input().split()))
cnt = 0
for i in range(0, n):
    if i > 0 and ((ls[i] > 0 and ls[i-1] > 0) or (ls[i] < 0 and ls[i-1] < 0)):
       print("YES")
       break
else:
    print("NO")
