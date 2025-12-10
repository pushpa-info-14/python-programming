from typing import List


class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int],
                         experience: List[int]) -> int:
        n = len(energy)
        res = 0
        for i in range(n):
            req_energy = max(0, energy[i] - initialEnergy + 1)
            req_experience = max(0, experience[i] - initialExperience + 1)
            initialEnergy -= energy[i]
            initialEnergy += req_energy
            initialExperience += experience[i]
            initialExperience += req_experience
            res += req_energy + req_experience
        return res


s = Solution()
print(s.minNumberOfHours(initialEnergy=5, initialExperience=3, energy=[1, 4, 3, 2], experience=[2, 6, 3, 1]))
print(s.minNumberOfHours(initialEnergy=2, initialExperience=4, energy=[1], experience=[3]))
