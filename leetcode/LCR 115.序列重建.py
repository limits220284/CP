class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n=len(sequences)
        dic=defaultdict(list)
        for i in range(n):
            m=len(sequences[i])
            for j in range(m-1):
                a,b=sequences[i][j],sequences[i][j+1]
                dic[a].append(b)
        for i in range(len(nums)-1):
            if nums[i+1] not in dic[nums[i]]:
                return False
        return True