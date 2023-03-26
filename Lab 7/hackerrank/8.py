if __name__ == '__main__':
    ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([score, name])
    ls.sort()
    pos = 0
    for i in range(len(ls)):
        if i > 0 and ls[i][0] != ls[i-1][0]:
            pos += 1
        if(pos == 1):
            print(ls[i][1])
        if pos > 1:
            break