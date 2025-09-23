class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]
        max_n = max(len(v1), len(v2))
        for i in range(abs(len(v1) - len(v2))):
            if len(v1) < max_n:
                v1.append(0)
            else:
                v2.append(0)
        i = 0
        while i < max_n:
            if v1[i] == v2[i]:
                i += 1
            elif v1[i] > v2[i]:
                return 1
            else:
                return -1
        return 0


s = Solution()
print(s.compareVersion(version1="1.2", version2="1.10"))
print(s.compareVersion(version1="1.01", version2="1.001"))
print(s.compareVersion(version1="1.0", version2="1.0.0.0"))
