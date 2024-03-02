class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # 如果正着会影响后面的，那么倒序就不会影响前面的下标
        for i, source, target in sorted(list(zip(indices, sources, targets)), reverse=True):
            l = len(source)
            if s[i:i + l] == source:
                s = s[:i] + target + s[i + l:]
            print(i, s)
        return s