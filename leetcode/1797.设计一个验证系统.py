class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.t=timeToLive
        self.dic=dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.dic:
            self.dic[tokenId]=currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.dic and self.dic[tokenId]+self.t>currentTime:
            self.dic[tokenId]=currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt=0
        ans=list(self.dic.keys())
        for x in ans:
            if self.dic[x]+self.t>currentTime:
                cnt+=1
            else:
                self.dic.pop(x)
        return cnt
        



# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)