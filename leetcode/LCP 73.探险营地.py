class Solution:
    def adventureCamp(self, ex: List[str]) -> int:
        dic = {}
        for c in ex[0].split('->'):
            dic[c] = True
        # print(dic)
        n = len(ex)
        ans = -1
        mx = 0
        for i in range(1, n):
            cnt = 0
            for c in set(ex[i].split('->')):
                if c != '' and c not in dic:
                    cnt += 1
                    dic[c] = True
            # print(i,cnt)
            if cnt > mx:
                mx = cnt
                ans = i
        return ans