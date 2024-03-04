class Solution:
    def monkeyMove(self, n: int) -> int:
        Mod=10**9+7
        return (pow(2,n,Mod)-2)%Mod