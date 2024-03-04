class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        Trie={}
        for word in words:
            t=Trie
            for c in word:
                t=t.setdefault(c,{})
                t['cnt']=t.get('cnt',0)+1
        # 统计
        ans=[]
        for word in words:
            t=Trie
            cnt=0
            for c in word:
                t=t[c]
                cnt+=t['cnt']
            ans.append(cnt)
        return ans