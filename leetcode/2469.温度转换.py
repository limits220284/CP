class Solution:
    def convertTemperature(self, c: float) -> List[float]:
        return [273.15+c,c*1.80+32.00]