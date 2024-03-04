class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #凡是能够交换现有字符，都可以认为是可以进行排序的
        m,n=len(word1),len(word2)
        if m!=n:return False
        #种类一样，数量一样即可
        w_1=Counter(word1)
        w_2=Counter(word2)
        a=sorted(list(w_1.keys()))
        b=sorted(list(w_2.keys()))
        if a!=b:return False
        c=sorted(list(w_1.values()))
        d=sorted(list(w_2.values()))
        if c!=d:return False
        return True
        