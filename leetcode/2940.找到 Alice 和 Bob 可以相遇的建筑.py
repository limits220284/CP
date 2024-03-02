class Node:
    def __init__(self,l=None,r = None,val = None):
        self.left = l
        self.right = r
        self.val = val # max num
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        def build(l,r):
            if l == r:
                v = Node(val = heights[l])
                return v
            mid = (l+r)//2
            v = Node()
            v.left,v.right = build(l,mid),build(mid+1,r)
            v.val =max(v.left.val,v.right.val)
            return v
        n = len(heights)
        m = len(queries)
        root = build(0,n-1)
        ans = [0]*m
        @cache
        def query(x,v,l,r,left,right):
            if v.val <= x:
                return 10**5
            if l == r:
                if l >= left:
                    return l
                else:
                    return 10**5
            mid = (l+r)//2
            if left > mid:
                return query(x,v.right,mid+1,r,left,right)
            elif right <= mid:
                return query(x,v.left,l,mid,left,right)
            elif left > l or right < r:
                return min(query(x,v.left,l,mid,left,right),query(x,v.right,mid+1,r,left,right))
            else:
                
                if v.left.val > x:
                    return query(x,v.left,l,mid,left,right)
                else:
                    return query(x,v.right,mid+1,r,left,right)
            return 10**5
        for i in range(m):
            x = max(heights[queries[i][0]],heights[queries[i][1]])
            if heights[min(queries[i])]<heights[max(queries[i])] or queries[i][0]==queries[i][1]:
                ans[i] = max(queries[i])
            else:
                ans[i] = query(x,root,0,n-1,max(queries[i])+1,n-1)
            if ans[i] == 10**5:
                ans[i] = -1
        return ans