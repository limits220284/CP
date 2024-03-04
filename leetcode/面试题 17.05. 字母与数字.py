class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        pre = 0
        dic = {0:0}
        l, r = 0, 0
        for i, x in enumerate(array):
            pre += 1 if x.isalpha() else -1
            if pre in dic:
                if i + 1 - dic[pre] > r - l:
                    l, r = dic[pre], i + 1
            else:
                dic[pre] = i + 1
        return array[l:r]