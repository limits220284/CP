class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        dic=Counter("!@#$%^&*()-+")
        a=False
        b=False
        c=False
        d=False
        for i,x in enumerate(password):
            if x.islower():
                a=True
            elif x.isupper():
                b=True
            elif x.isdigit():
                c=True
            elif x in dic:
                d=True
            if i and password[i]==password[i-1]:
                return False
        return a and b and c and d