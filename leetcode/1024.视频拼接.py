class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # 贪心算法
        right_most=[0] * 101
        for clip in clips:
            right_most[clip[0]] = max(right_most[clip[0]],clip[1])
        next_right = cur_right = 0
        ans = 0
        for i in range(time):
            next_right = max(right_most[i],next_right)
            if i == cur_right:
                if i == next_right:
                    return -1
                cur_right = next_right
                ans += 1
        return ans