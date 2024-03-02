class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        # 倍增的思想, 需要维护点和路径和
        m = k.bit_length()-1
        n = len(receiver)
        pa = [[p] + [-1] * m for p in receiver]
        tot = [[p] + [0] * m for p in receiver]
        for i in range(m):
            for x in range(n):
                p, t = pa[x][i], tot[x][i]
                pa[x][i+1] = pa[p][i]
                tot[x][i+1] = tot[p][i] + t
        ans = 0
        for node in range(n):
            num = node
            for j in range(k.bit_length()):
                if (k >> j) & 1:
                    num += tot[node][j]
                    node = pa[node][j]
            ans = max(ans, num)
        return ans

                

            
        