import math
a=int(input())
b=int(input())
for i in range(a, b+1):
    if math.sqrt(i * 1.0) == int(math.sqrt(i)):
        print(i, end=" ")