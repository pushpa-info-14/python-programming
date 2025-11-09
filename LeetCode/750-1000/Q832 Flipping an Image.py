from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        is_odd = n % 2
        for i in range(n):
            for j in range(n // 2):
                image[i][j], image[i][n - j - 1] = image[i][n - j - 1], image[i][j]
                image[i][j] ^= 1
                image[i][n - j - 1] ^= 1
            if is_odd:
                image[i][n // 2] ^= 1
        return image


s = Solution()
print(s.flipAndInvertImage(image=[[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
print(s.flipAndInvertImage(image=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
