class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans=0.0
        pre=0
        for i,c in enumerate(brackets):
            if income>=c[0]:
                ans+=(c[0]-pre)*(c[1]/100)
                pre=c[0]
            else:
                ans+=(income-pre)*(c[1]/100)
                break
        return ans