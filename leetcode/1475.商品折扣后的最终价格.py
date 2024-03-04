class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 单调栈怎么写
        # 涉及到有序，是栈顶元素永远都是离当前数最小的
        n=len(prices)
        st=[0]
        ans=prices[::]
        for i in range(n-1,-1,-1):
            p=prices[i]
            while len(st)>1 and st[-1]>p:
                st.pop()
            ans[i]-=st[-1]
            st.append(p)
        return ans