class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def K(x):
            return int(x[-1])
        access_times.sort(key = K)
        dic = defaultdict(list)
        ans = set()
        def check(x,y):
            hx = int(x[:2])
            mx = int(x[2:])
            hy = int(y[:2])
            my = int(y[2:])
            dis = hy*60+my-hx*60-mx
            return abs(dis) < 60
        for at in access_times:
            dic[at[0]].append(at[1])
            if len(dic[at[0]]) >=3 and check(dic[at[0]][-1],dic[at[0]][-3]):
                ans.add(at[0])
        return list(ans)