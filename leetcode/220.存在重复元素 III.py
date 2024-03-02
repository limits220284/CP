from sortedcontainers import SortedList
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # 平衡树+二分
        # 滑动窗口
        # 枚举j，然后在indexDiff内找到是否存在一个值
        n = len(nums)
        st = SortedList()
        for i, x in enumerate(nums):
            if len(st) > indexDiff:
                st.remove(nums[i-indexDiff-1])
            if not st:
                st.add(x)
                continue
            # 在st中进行二分，找到最合适的位置，看看是否满足条件三
            l, r = 0, len(st) - 1
            while l < r:
                mid = (l + r) // 2
                if st[mid] >= x:
                    r = mid
                else:
                    l = mid + 1
            if l > 0:
                if abs(x - st[l-1]) <= valueDiff:
                    return True
            if abs(x - st[l]) <= valueDiff:
                return True
            st.add(x)
            # print(st)
        return False
        