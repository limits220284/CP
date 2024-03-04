class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        mx=max(nums)
        # 枚举公因数的数目
        dic=Counter(nums)
        ans=0
        for i in range(1,mx+1):
            subgcd=0
            for j in range(i,mx+1,i):
                if j in dic:
                    if subgcd==0:
                        subgcd=j
                    else:
                        subgcd=gcd(subgcd,j)
                    if subgcd==i:
                        ans+=1
                        break
        return ans