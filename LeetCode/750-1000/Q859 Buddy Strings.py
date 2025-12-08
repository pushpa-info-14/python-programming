from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            counter = Counter(s)
            for freq in counter.values():
                if freq > 1:
                    return True
            return False

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff) != 2:
            return False

        i = diff[0]
        j = diff[1]
        return s[i] == goal[j] and s[j] == goal[i]

    def buddyStrings2(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            return len(set(s)) != len(s)

        diff = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff.append(i)
        if len(diff) != 2:
            return False

        i = diff[0]
        j = diff[1]
        return s[i] == goal[j] and s[j] == goal[i]


s = Solution()
print(s.buddyStrings(s="ab", goal="ba"))
print(s.buddyStrings(s="ab", goal="ab"))
print(s.buddyStrings(s="aa", goal="aa"))
print(s.buddyStrings2(s="ab", goal="ba"))
print(s.buddyStrings2(s="ab", goal="ab"))
print(s.buddyStrings2(s="aa", goal="aa"))
