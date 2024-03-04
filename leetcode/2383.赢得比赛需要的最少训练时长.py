class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        sm = sum(energy)
        trainingHours = 0 if initialEnergy > sm else sm + 1 - initialEnergy
        for e in experience:
            if initialExperience <= e:
                trainingHours += 1 + (e - initialExperience)
                initialExperience = 2 * e + 1
            else:
                initialExperience += e
        return trainingHours