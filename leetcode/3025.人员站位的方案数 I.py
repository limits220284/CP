class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        def K(x):
            return x[0],x[1]
        points.sort(key = K)
        #print(points)
        n = len(points)
        dic = defaultdict(list)
        for i in range(n):
            dic[points[i][0]].append(points[i][1])
        #print(dic)
        ans = 0
        def find(arr,x):
            l,r =0, len(arr)-1
            while l <= r:
                mid = (l+r)//2
                if arr[mid] < x:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
        for i in range(n):
            p = points[i]
            #print(p)
            a = 0
            minH = -10**19            
            for k,d in dic.items():
                if k < p[0]:
                    continue
                
                h = find(d,p[1])
                #print(k,d,h,minH)
                
                if k != p[0] and h<len(d) and d[h] == p[1]:
                    a+=1
                    minH = 0
                    break
                if h == 0:
                    continue
                if (d[h-1]>minH):
                    a += 1
                    minH = d[h-1]
            ans+=a
        return ans
                