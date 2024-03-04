class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # 纯暴力也是能过得
        def yc(t):
            t+='*'
            arr=[]
            n=len(t)
            cnt=0
            for i in range(n-1):
                if t[i]==t[i+1]:
                    cnt+=1
                else:
                    arr.append([t[i],cnt+1])
                    cnt=0
            return arr
        ans_s=yc(s)
        # print(ans_s)
        res=0
        for word in words:
            arr=yc(word)
            if len(arr)==len(ans_s):
                flag=True
                for i in range(len(arr)):
                    if arr[i][0]!=ans_s[i][0]:
                        flag=False
                        break
                    else:
                        if arr[i][1]!=ans_s[i][1] and (ans_s[i][1]<=2 or arr[i][1]>ans_s[i][1]):
                                flag=False
                                break
                if flag:
                    res+=1
        return res


            