x = input().split()
n, m, k = int(x[0]), int(x[1]), int(x[2])
pa = {}
vis = {}
lands = {}
ptr = {}


def check(x, y):
    m, n = len(x), len(y)
    if m < n:
        for i in range(m):
            if ord(x[i]) > ord(y[i]):
                return True
            elif ord(x[i]) < ord(y[i]):
                return False
        return False
    else:
        for i in range(n):
            if ord(x[i]) > ord(y[i]):
                return True
            elif ord(x[i]) < ord(y[i]):
                return False
        return True


def findPa(x):
    if pa[x] == x:
        return x
    else:
        pa[x] = findPa(pa[x])
        return pa[x]


for _ in range(k):
    Input = input().split()
    name, x, y = Input[0], int(Input[1]), int(Input[2])
    pa[name] = name
    lands[name] = 1
    ptr[name] = [x, y]
    if (x, y) not in vis:
        vis[(x, y)] = name
        lands[name] = 1
    else:
        name_pre = vis[(x, y)]
        name_pre = findPa(name_pre)
        if check(name_pre, name):
            pa[name] = name_pre
        else:
            pa[name_pre] = name
            lands[name] = 1
            vis[(x, y)] = name
q = int(input())


def check_out(x, y):
    return x > 0 and x <= n and y > 0 and y <= m


for _ in range(q):
    order = input().split()
    name, opt = order[0], order[1]
    if name not in pa or pa[name] != name:
        print("unexisted empire.")
        continue
    x, y = ptr[name]
    if opt == 'W':
        x, y = x - 1, y
    elif opt == 'A':
        x, y = x, y - 1
    elif opt == 'S':
        x, y = x + 1, y
    else:
        x, y = x, y + 1
    # print(x,y)
    if not check_out(x, y):
        print("out of bounds!")
        continue
    if (x, y) not in vis:
        vis[(x, y)] = name
        lands[name] += 1
        ptr[name] = [x, y]
        print("vanquish!")
    else:
        name_pre = vis[(x, y)]
        name_pre = findPa(name_pre)
        if name_pre == name:
            print("peaceful.")
            ptr[name] = [x, y]
            continue
        if lands[name_pre] > lands[name]:
            pa[name] = name_pre
            lands[name_pre] += lands[name]
        elif lands[name_pre] < lands[name]:
            pa[name_pre] = name
            lands[name] += lands[name_pre]
        else:
            if check(name_pre, name):
                pa[name] = name_pre
                lands[name_pre] += lands[name]
            else:
                pa[name_pre] = name
                lands[name] += lands[name_pre]
        print(pa[name] + ' wins!')
        ptr[name] = [x, y]

