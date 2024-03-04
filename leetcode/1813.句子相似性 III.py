class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1)>len(sentence2):
            sentence1,sentence2=sentence2,sentence1
        s2=sentence2.strip().split()
        n=len(s2)
        print(s2,sentence1)
        for i in range(n):
            for j in range(i,n+1):
                res=" ".join(s2[0:i]+s2[j:])
                # print(res)
                if res==sentence1:
                    return True
        return False
                
