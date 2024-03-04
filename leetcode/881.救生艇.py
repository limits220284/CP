class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        n=len(people)
        l,r=0,n-1
        cnt=0
        while l<=r:
            if people[l]+people[r]<=limit:
                r-=1
            l+=1
            cnt+=1
        return cnt