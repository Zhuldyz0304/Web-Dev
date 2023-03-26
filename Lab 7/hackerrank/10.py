if __name__ == '__main__':
    N = int(input())
    ls = []
    for _ in range(N):
        s, *lk = input().split()
        lk = list(map(int, lk));
        if s == 'insert':
            ls.insert(lk[0], lk[1])
        if s == 'append':
            ls.append(lk[0])
        if s == 'print':
            print(ls)
        if s == 'pop':
            ls.pop()
        if s == 'sort':
            ls.sort()
        if s == 'reverse':
            ls.reverse()
        if s == 'remove':  
            ls.remove(lk[0])