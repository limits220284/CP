#
# @lc app=leetcode.cn id=722 lang=python3
#
# [722] 删除注释
#

# @lc code=start
class Solution:
    def removeComments1(self, source: List[str]) -> List[str]:
        flag = 0
        ans = []
        i, n = 0, len(source)
        word = []
        while i < n:
            s = source[i]
            m = len(s)
            j = 0
            valid = True
            while j < m:
                if s[j] == '/':
                    if s[j+1] == '/':
                        valid = False
                        j += 2
                    elif s[j+1] == '*':
                        if valid == True:
                            flag += 1
                        j += 2
                    else:
                        if flag == 0 and valid == True:
                            word.append(s[j])
                        j += 1
                elif s[j] == '*':
                    # 注释合上了
                    if s[j+1] == '/':
                        valid = True
                        if flag == 0:
                            word.append(s[j])
                            word.append(s[j+1])
                        flag = 0
                        j += 2
                    else:
                        if flag == 0 and valid == True:
                            word.append(s[j])
                        j += 1
                else:
                    if flag == 0 and valid == True:
                        word.append(s[j])
                    j += 1
            if flag == 0:
                ans.append("".join(word))
                word = []
            i += 1
        ans = [word for word in ans if word]
        return ans
    def removeComments(self, source: List[str]) -> List[str]:
    # 匹配所有 // 和 /* */，后者用非贪婪模式。将所有匹配结果替换成空串。最后移除多余空行。
        return list(filter(None, re.sub('//.*|/\*(.|\n)*?\*/', '', '\n'.join(source)).split('\n')))
