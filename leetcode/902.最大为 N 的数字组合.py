class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        s=str(n)
        # i代表当前填到了第几位数
        # mask类似于状态压缩的思想，看看前面是否已经使用过了当前的数字
        # is_lim 代表前面的数字是否都填了对应位置的数字
        # is_num 代表前面是否填了数字
        @cache
        def f(i:int,is_lim:bool,is_num:bool):
            res=0
            if i==len(s):
                return int(is_num)
            if not is_num:
                res+=f(i+1,False,False)
            up=s[i] if is_lim else '9'
            for d in digits:
                if d>up:break
                res+=f(i+1,is_lim and d==s[i],True)
            return res
        return f(0,True,False)
