class Solution:
    def maximum69Number(self, num: int) -> int:
        number = list(str(num))

        for i in range(len(number)):
            if number[i] == '6':
                number[i] = '9'
                break
        return int(''.join(number))


s = Solution()
print(s.maximum69Number(num=9669))
print(s.maximum69Number(num=9996))
print(s.maximum69Number(num=9999))
