class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = list()
        for ch in number:
            if ch.isdigit():
                digits.append(ch)
        
        n, pt = len(digits), 0
        ans = list()

        while n > 0:
            if n > 4:
                ans.append("".join(digits[pt:pt+3]))
                pt += 3
                n -= 3
            else:
                if n == 4:
                    ans.append("".join(digits[pt:pt+2]))
                    ans.append("".join(digits[pt+2:pt+4]))
                else:
                    ans.append("".join(digits[pt:pt+n]))
                break
        
        return "-".join(ans)
