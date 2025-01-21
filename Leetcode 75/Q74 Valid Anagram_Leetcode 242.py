class Solution:
    def isAnagram1(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1 = {i: 0 for i in s}
        dict2 = {j: 0 for j in t}

        for i in s:
            if i in dict1:
                dict1[i] += 1
        for j in t:
            if j in dict2:
                dict2[j] += 1

        return True if dict1 == dict2 else False

    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        list1 = [i for i in s]
        list2 = [j for j in t]

        list1.sort()
        list2.sort()

        return True if list1 == list2 else False

    def isAnagram3(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0 for i in range(26)]

        a = ord('a')
        for i in s:
            count[ord(i) - a] += 1

        for j in t:
            if count[ord(j) - a] == 0:
                return False
            count[ord(j) - a] -= 1

        return True


solution = Solution()
print(solution.isAnagram1("anagram", "nagaram"))
print(solution.isAnagram1("rat", "car"))
print(solution.isAnagram1("aa", "a"))
print(solution.isAnagram1("aacc", "ccac"))
print("------------------------------")
print(solution.isAnagram2("anagram", "nagaram"))
print(solution.isAnagram2("rat", "car"))
print(solution.isAnagram2("aa", "a"))
print(solution.isAnagram2("aacc", "ccac"))
print("------------------------------")
print(solution.isAnagram3("anagram", "nagaram"))
print(solution.isAnagram3("rat", "car"))
print(solution.isAnagram3("aa", "a"))
print(solution.isAnagram3("aacc", "ccac"))
