class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = days = 0
        for p, g in sorted(zip(plantTime, growTime), key=lambda z: -z[1]):
            days += p  # 累加播种天数
            ans = max(ans, days + g)  # 再加上生长天数，就是这个种子的开花时间
        return ans