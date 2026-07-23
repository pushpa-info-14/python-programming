class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        arr = [1] * children
        money -= children
        if money < 7:
            return 0
        i = 0
        while i < children and money - 7 >= 0:
            arr[i] += 7
            money -= 7
            i += 1

        if money == 0:
            return i
        else:
            if i == children:  # all the children have allocated 8. Still remains some. That goes to the last child. 8+x > 4
                return i - 1
            elif i == children - 1 and arr[i] + money == 4:  # Last child got 4. So we have to give 1 to previous child.
                return i - 1
        return i  # All the i children can be allocated 8


s = Solution()
print(s.distMoney(money=20, children=3))
print(s.distMoney(money=16, children=2))
print(s.distMoney(money=17, children=2))
print(s.distMoney(money=5, children=2))
print(s.distMoney(money=8, children=5))
print(s.distMoney(money=13, children=3))
