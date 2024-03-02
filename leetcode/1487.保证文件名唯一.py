class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        ans = []
        index = {}
        for name in names:
            # 如果name不在index里面,直接加入结果中
            if name not in index:
                ans.append(name)
                index[name] = 1
            else:
                k = index[name]
                while name + '(' + str(k) + ')' in index:
                    k += 1
                t = name + '(' + str(k) + ')'
                ans.append(t)
                index[name] = k + 1
                index[t] = 1
        return ans