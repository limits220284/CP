class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        m,mx={},0
        for name,id,view in zip(creators,ids,views):
            if name in m:
                t=m[name]
                t[0]+=view
                if view>t[1] or view==t[1] and t[2]>id:
                    t[1],t[2]=view,id
                m[name]=t
            else:
                m[name]=[view,view,id]
            mx=max(mx,m[name][0])
        print(m)
        return [[name,id] for name,[tot,up,id] in m.items() if tot==mx] 