class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        #判断该数能否被三进制表示出来,如果转换成了三进制，但是各个位置上都不是一，那就不对
        while n!=0:  
            if n%3==2:
                return False
            n//=3
        return True