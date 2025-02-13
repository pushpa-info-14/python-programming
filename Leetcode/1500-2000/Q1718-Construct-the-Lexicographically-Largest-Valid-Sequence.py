from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        size = n * 2 - 1
        result_sequence = [0] * size
        is_number_used = [0] * (n + 1)

        def backtracking(i):
            if i == size:
                return True
            if result_sequence[i] != 0:
                return backtracking(i + 1)

            for num in reversed(range(1, n + 1)):
                if is_number_used[num]:
                    continue

                is_number_used[num] = 1
                result_sequence[i] = num

                if num == 1:
                    if backtracking(i + 1):
                        return True
                elif i + num < size and result_sequence[i + num] == 0:
                    result_sequence[i + num] = num
                    if backtracking(i + 1):
                        return True
                    result_sequence[i + num] = 0
                is_number_used[num] = 0
                result_sequence[i] = 0
            return False

        backtracking(0)
        return result_sequence


s = Solution()
print(s.constructDistancedSequence(3))
print(s.constructDistancedSequence(10))
