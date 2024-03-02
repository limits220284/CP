class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        if m == 1 and flowerbed[0] == 0: return True
        for i, x in enumerate(flowerbed):
            if n == 0: return True
            if x == 1:
                continue
            else:
                if i == 0:
                    if i + 1 < m and flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                    else:
                        continue
                elif i == m-1:
                    if flowerbed[i-1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                    else:
                        continue
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        n -= 1
                        flowerbed[i] = 1
                    else:
                        continue
        return n == 0