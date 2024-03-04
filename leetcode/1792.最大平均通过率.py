class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        for cla in classes:
            heappush(h,[-(cla[1]-cla[0])/(cla[1] * (cla[1] + 1)),(cla[0],cla[1])])
        n = len(classes)
        for i in range(extraStudents):
            _ , (y,x) = heappop(h)
            x += 1
            y += 1
            heappush(h,[-(x - y)/(x * (x + 1)),(y,x)])
        ans = 0
        for _,(y,x) in h:
            ans += y/x
        return ans/n
        
            