class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        s=set()
        for x in nums:
            s.add(x)
            n=0
            while x:
                n=n*10+x%10
                x//=10
            s.add(n)
        return len(s)