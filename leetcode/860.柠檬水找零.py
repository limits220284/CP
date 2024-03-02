class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        arr = defaultdict(int)
        for x in bills:
            if x == 5:
                arr[5] += 1
            elif x == 10:
                if arr[5] >= 1:
                    arr[5] -= 1
                    arr[10] += 1
                else:
                    return False
            else:
                if arr[10] >= 1 and arr[5] >= 1:
                    arr[10] -= 1
                    arr[5] -= 1
                elif arr[5] >= 3:
                    arr[5] -= 3
                else:
                    return False
        return True