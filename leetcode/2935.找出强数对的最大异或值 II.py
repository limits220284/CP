class Node:
    __slots__ = 'children', 'cnt'

    def __init__(self):
        self.children = [None, None]
        self.cnt = 0  # 子树大小

class Trie:
    HIGH_BIT = 19

    def __init__(self):
        self.root = Node() #本身包括一个节点

    # 添加 val
    def insert(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if cur.children[bit] is None:
                cur.children[bit] = Node()
            cur = cur.children[bit]
            cur.cnt += 1

    # 删除 val，但不删除节点
    # 要求 val 必须在 trie 中
    def remove(self, val: int) -> None:
        cur = self.root
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            cur = cur.children[bit]
            cur.cnt -= 1

    # 返回 val 与 trie 中一个元素的最大异或和
    # 要求 trie 中至少有一个元素
    def max_xor(self, val: int) -> int:
        cur = self.root
        ans = 0
        for i in range(Trie.HIGH_BIT, -1, -1):
            bit = (val >> i) & 1
            if cur.children[bit ^ 1] and cur.children[bit ^ 1].cnt:
                ans |= 1 << i
                bit ^= 1
            cur = cur.children[bit]
        return ans

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        nums.sort()
        t = Trie()
        ans = left = 0
        for y in nums:
            t.insert(y)
            while nums[left] * 2 < y:
                t.remove(nums[left])
                left += 1
            ans = max(ans, t.max_xor(y))
        return ans
    def maximumStrongPairXor1(self, nums: List[int]) -> int:
        nums.sort()
        ans = mask = 0
        highBit = max(nums).bit_length() - 1
        for i in range(highBit, -1, -1):
            mask |= 1 << i
            new_ans = ans | (1 << i)
            vis = dict()
            for y in nums:
                new_y = y & mask
                if new_y ^ new_ans in vis and vis[new_y ^ new_ans] * 2 >= y:
                    ans = new_ans
                    break
                vis[new_y] = y
        return ans
            