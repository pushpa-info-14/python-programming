class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        is_bulky = False
        if max(length, width, height) >= 10 ** 4 or volume >= 10 ** 9:
            is_bulky = True
        is_heavy = False
        if mass >= 100:
            is_heavy = True

        if is_bulky and is_heavy:
            return 'Both'
        elif not is_bulky and not is_heavy:
            return 'Neither'
        elif is_bulky and not is_heavy:
            return 'Bulky'
        else:
            return 'Heavy'


s = Solution()
print(s.categorizeBox(length=1000, width=35, height=700, mass=300))
print(s.categorizeBox(length=200, width=50, height=800, mass=50))
