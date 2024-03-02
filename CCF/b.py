x = input().split(' ')
w, h = int(x[0]), int(x[1])
if w == h:
    print(w, h)
if w < h:
    if w * 2 > h:
        print(0, (h - w) * 2)
    elif w * 2 == h:
        print(w, w)
    elif w * 3 > h:
        print(h - w - w, h)
    else:
        print(w, w * 3)
elif w > h:
    if w < h * 2:
        print((w - h) * 2, 0) # 正确
    elif h * 2 == w:
        print(h, h) # 正确
    elif w < 3 * h:
        print(w, w - h - h)
    else:
        print(h * 3, h)