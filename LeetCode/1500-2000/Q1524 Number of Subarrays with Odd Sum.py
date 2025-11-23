from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        count = 0
        mode = 1e9 + 7

        for start_index in range(n):
            current_sum = 0
            for end_index in range(start_index, n):
                current_sum += arr[end_index]
                if current_sum % 2:
                    count += 1
        return int(count % mode)

    def numOfSubarrays2(self, arr: List[int]) -> int:
        mode = 1e9 + 7
        count = 0
        prefix_sum = 0
        odd_count = 0
        even_count = 1

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                count += even_count
                odd_count += 1
            else:
                count += odd_count
                even_count += 1
        return int(count % mode)

    def numOfSubarrays3(self, arr: List[int]) -> int:
        n = len(arr)
        mode = 1e9 + 7
        count = 0
        dp_odd = [0 for _ in range(n + 1)]
        dp_even = [0 for _ in range(n + 1)]

        for i in reversed(range(n)):
            if arr[i] % 2:
                dp_odd[i] = 1 + dp_even[i + 1]
                dp_even[i] = dp_odd[i + 1]
            else:
                dp_odd[i] = dp_odd[i + 1]
                dp_even[i] = 1 + dp_even[i + 1]
            count += dp_odd[i]
        return int(count % mode)

    def numOfSubarrays4(self, arr: List[int]) -> int:
        mode = 1e9 + 7
        count = 0
        odd_count = 0
        even_count = 0

        for num in arr:
            if num % 2:
                odd_count, even_count = 1 + even_count, odd_count
            else:
                even_count += 1
            count += odd_count
        return int(count % mode)


s = Solution()
print(s.numOfSubarrays([1, 3, 5]))
print(s.numOfSubarrays([2, 4, 6]))
print(s.numOfSubarrays([1, 2, 3, 4, 5, 6, 7]))

print(s.numOfSubarrays2([1, 3, 5]))
print(s.numOfSubarrays2([2, 4, 6]))
print(s.numOfSubarrays2([1, 2, 3, 4, 5, 6, 7]))

print(s.numOfSubarrays3([1, 3, 5]))
print(s.numOfSubarrays3([2, 4, 6]))
print(s.numOfSubarrays3([1, 2, 3, 4, 5, 6, 7]))

print(s.numOfSubarrays4([1, 3, 5]))
print(s.numOfSubarrays4([2, 4, 6]))
print(s.numOfSubarrays4([1, 2, 3, 4, 5, 6, 7]))
