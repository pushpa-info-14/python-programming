class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        pre_yes = [0] * (n + 1)
        pre_no = [0] * (n + 1)
        for i in range(n):
            yes = 1 if customers[i] == 'Y' else 0
            no = 1 if customers[i] == 'N' else 0
            pre_yes[i + 1] = yes + pre_yes[i]
            pre_no[i + 1] = no + pre_no[i]
        res = 0
        mini = 10 ** 10
        for i in range(n + 1):
            yes = pre_yes[n] - pre_yes[i]
            no = pre_no[i]
            if yes + no < mini:
                res = i
                mini = yes + no
        return res

    def bestClosingTime2(self, customers: str) -> int:
        n = len(customers)
        count_no = 0
        count_yes = customers.count('Y')
        res = 0
        mini = count_no + count_yes
        for i in range(n):
            if customers[i] == 'Y':
                count_yes -= 1
            if customers[i] == 'N':
                count_no += 1
            if count_no + count_yes < mini:
                mini = count_no + count_yes
                res = i + 1
        return res


s = Solution()
print(s.bestClosingTime(customers="YYNY"))
print(s.bestClosingTime(customers="NNNNN"))
print(s.bestClosingTime(customers="YYYY"))
print("---------------")
print(s.bestClosingTime2(customers="YYNY"))
print(s.bestClosingTime2(customers="NNNNN"))
print(s.bestClosingTime2(customers="YYYY"))
