class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        # 直接采用栈进行模拟即可
        res=[]
        pre=0
        for i,x in enumerate(target):
            if x!=pre:
                res+=['Push','Pop']*(x-pre-1)
            res.append('Push')
            pre=x
        return res
                
            