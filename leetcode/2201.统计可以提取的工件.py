class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        valid = {tuple(pos) for pos in dig}#转为tuple才能够进行hash操作
        
        ans = 0
        for (r1, c1, r2, c2) in artifacts:
            check = True
            for r in range(r1, r2 + 1):
                for c in range(c1, c2 + 1):
                    if (r, c) not in valid:
                        check = False
                        break
                if not check:
                    break
            
            if check:
                ans += 1

        return ans