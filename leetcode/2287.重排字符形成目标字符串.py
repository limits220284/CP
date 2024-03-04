class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        dic_s=Counter(s)
        dic_tar=Counter(target)
        mi=1e9
        for x,y in dic_tar.items():
            mi=min(mi,dic_s[x]//y)
        return mi
