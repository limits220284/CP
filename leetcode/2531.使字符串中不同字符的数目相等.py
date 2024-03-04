class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        d1=Counter(word1)
        d2=Counter(word2)
        # 枚举d1和d2要进行交换的字母
        a1=list(d1.keys())
        a2=list(d2.keys())
        
        for x in a1:
            for y in a2:
                n1=len(d1)
                n2=len(d2)
                if x==y:
                    if n1==n2:
                        return True
                else:
                    if d1[x]==1:
                        n1-=1
                    if y not in d1:
                        n1+=1
                    if d2[y]==1:
                        n2-=1
                    if x not in d2:
                        n2+=1
                    if n1==n2:
                        return True
        return False
                
                