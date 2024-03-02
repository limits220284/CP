from sortedcontainers import SortedList
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        # 计算出所有的可能性
        # 用sortedlist维护过程
        n = len(nums)
        pos = []
        for i in range(1, n // 2 + 1):
            pos.append(nums[i] - nums[0])
        for k in pos:
            if k == 0 or k % 2 != 0: continue
            st = SortedList(nums)
            flag = True
            ans = []
            while st:
                be = st[0]
                ed = st[0] + k
                if ed not in st:
                    flag = False
                    break
                idx = st.index(ed)
                ans.append((be + ed) // 2)
                st.pop(idx)
                st.pop(0)
            if flag:
                print(k // 2)
                return ans
        return None