class Solution:
    def secondHighest(self, s: str) -> int:
        fir,sec=-1,-1
        n=len(s)
        for x in s:
            if x.isdigit():
                k=int(x)
                if k>fir:
                    sec=fir
                    fir=k
                elif k<fir and k>sec:
                    sec=k
        return sec