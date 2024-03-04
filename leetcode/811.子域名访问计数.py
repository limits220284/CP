class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        #hash表计数即可
        dic=defaultdict(int)
        for x in cpdomains:
            x=x.replace('.',' ').split()
            if len(x)==4:
                dic['.'.join(x[-3:])]+=int(x[0])
            dic['.'.join(x[-2:])]+=int(x[0])
            dic['.'.join(x[-1:])]+=int(x[0])
        res=[]
        return [f'{s} {c}' for c,s in dic.items()]
            