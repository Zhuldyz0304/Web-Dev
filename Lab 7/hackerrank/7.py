if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    mx = -200
    mx2 = -200
    for i in sorted(arr):
        if(mx < i):
            mx2 = mx
            mx = i
    print(mx2)
    