class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt=0
        dic={'type':0,'color':1,'name':2}
        for i,item in enumerate(items):
            if item[dic[ruleKey]]==ruleValue:
                cnt+=1
        return cnt
