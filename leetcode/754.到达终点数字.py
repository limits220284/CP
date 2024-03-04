class Solution:
    def reachNumber(self, target: int) -> int:
        # 贪心算法
        target=abs(target)
        n=1
        tot=0
        while tot<target or (tot-target)%2:
            tot+=n
            n+=1
        return n-1