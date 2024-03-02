class Solution:
    def uniqueLetterString(self, s: str) -> int:
        # 转换问题，某个字母最多在多少个子串中出现
        # 先统计所有字符出现的位置，左边的乘以右边的就是最后的结果
        n = len(s)
        dic = defaultdict(list)
        for i, x in enumerate(s):
            dic[x].append(i)
        ans = 0
        for arr in dic.values():
            m = len(arr)
            arr = [-1] + arr + [n]
            for i in range(1, m + 1):
                ans += (arr[i] - arr[i-1]) * (arr[i + 1] - arr[i])
        return ans