class Solution:
    def categorizeBox(self, length, width, height, mass):
        maxd = max(length, width, height)
        vol = length * width * height
        isBulky = maxd >= 10000 or vol >= 10**9
        isHeavy = mass >= 100
        if isBulky and isHeavy:
            return 'Both'
        if isBulky:
            return 'Bulky'
        if isHeavy:
            return 'Heavy'
        return 'Neither'