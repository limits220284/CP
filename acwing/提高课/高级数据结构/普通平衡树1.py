import random

class Node:
    def __init__(self):
        self.l = self.r = 0
        self.key = self.val = 0
        self.cnt = self.size = 0    #这里初始值设为1会出错

N = 100010
tr = [Node() for i in range(N)]
root = idx = 0

def pushup(p):
    tr[p].size = tr[tr[p].l].size + tr[tr[p].r].size + tr[p].cnt

def get_node(key):
    global idx
    idx += 1
    tr[idx].key, tr[idx].val, tr[idx].cnt, tr[idx].size = key, random.random(), 1, 1
    return idx

def zig(p):  #右旋   这里的p相当于指针，每次更改节点位置都要相应更改指针位置
    q = tr[p].l
    tr[p].l = tr[q].r; tr[q].r = p; p = q
    pushup(tr[p].r); pushup(p)
    return p

def zag(p):   #左旋
    q = tr[p].r
    tr[p].r = tr[q].l; tr[q].l = p; p = q
    pushup(tr[p].l); pushup(p)
    return p

def build():
    global root
    root = get_node(-float("inf"))    #建立两个哨兵节点root为1,root.r为2
    tr[root].r = get_node(float("inf"))
    pushup(root)
    if tr[1].val < tr[2].val: root = zag(root)

def insert(p, key):
    if not p: p = get_node(key)
    elif tr[p].key == key: tr[p].cnt += 1
    elif tr[p].key > key:
        tr[p].l = insert(tr[p].l, key)
        if tr[tr[p].l].val > tr[p].val: p = zig(p)
    else:
        tr[p].r = insert(tr[p].r, key)
        if tr[tr[p].r].val > tr[p].val: p = zag(p)
    pushup(p)
    return p

def remove(p, key):
    if not p: return p
    if tr[p].key == key:
        if tr[p].cnt > 1: tr[p].cnt -= 1
        elif tr[p].l or tr[p].r:
            if not tr[p].r or tr[tr[p].l].val > tr[p].val:
                p = zig(p)
                tr[p].r = remove(tr[p].r, key)   #右旋后当前点位于原点的右子树
            else:
                p = zag(p)
                tr[p].l = remove(tr[p].l, key)
        else: p = 0
    elif tr[p].key > key: tr[p].l = remove(tr[p].l, key)
    else: tr[p].r = remove(tr[p].r, key)
    pushup(p)
    return p

def get_rank_by_key(p, key):
    if not p: return 0   #本题中不会出现这种情况
    if tr[p].key == key: return tr[tr[p].l].size + 1
    if tr[p].key > key: return get_rank_by_key(tr[p].l, key)
    return tr[tr[p].l].size + tr[p].cnt + get_rank_by_key(tr[p].r, key)

def get_key_by_rank(p, rank):
    if not p: return float("inf")
    if tr[tr[p].l].size >= rank: return get_key_by_rank(tr[p].l, rank)
    if tr[tr[p].l].size + tr[p].cnt >= rank: return tr[p].key
    return get_key_by_rank(tr[p].r, rank - tr[tr[p].l].size - tr[p].cnt)

def get_prev(p, key):
    if not p: return -float("inf")
    if tr[p].key >= key: return get_prev(tr[p].l, key)
    return max(tr[p].key, get_prev(tr[p].r, key))

def get_next(p, key):
    if not p: return float("inf")
    if tr[p].key <= key: return get_next(tr[p].r, key)
    return min(tr[p].key, get_next(tr[p].l, key))

build()
n = int(input())
for i in range(n):
    opt, x = map(int, input().split())
    if opt == 1: root = insert(root, x)
    elif opt == 2: root = remove(root, x)
    elif opt == 3: print(get_rank_by_key(root, x) - 1)   #因为有两个哨兵节点所以要排除-float("inf")的点
    elif opt == 4: print(get_key_by_rank(root, x + 1))
    elif opt == 5: print(get_prev(root, x))
    else: print(get_next(root, x))
