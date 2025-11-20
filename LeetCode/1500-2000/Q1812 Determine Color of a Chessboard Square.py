class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        map1 = {x: i for i, x in enumerate('abcdefgh')}
        map2 = {str(x): x - 1 for x in range(1, 9)}
        return (map1[coordinates[0]] + map2[coordinates[1]]) % 2 == 1


s = Solution()
print(s.squareIsWhite(coordinates="a1"))
print(s.squareIsWhite(coordinates="h3"))
print(s.squareIsWhite(coordinates="c7"))
