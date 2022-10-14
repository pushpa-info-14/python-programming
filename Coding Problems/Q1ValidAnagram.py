"""
Given two strings s1 and s2, check if they're
anagrams. Two strings are anagrams if they're
made of the same characters with the same frequencies. 
"""
from collections import Counter


def are_anagrams1(s1, s2):
    if len(s1) != len(s2):
        return False
    freq1 = {}
    freq2 = {}
    for ch in s1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1
    for ch in s2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1
    for key in freq1:
        if key not in freq2 or freq1[key] != freq2[key]:
            return False
    return True
# T(n) = O(n)
# S(n) = O(n)


def are_anagrams2(s1, s2):
    if len(s1) != len(s2):
        return False
    return Counter(s1) == Counter(s2)
# T(n) = O(n)
# S(n) = O(n)


def are_anagrams3(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)
# T(n) = O(nlogn)
# S(n) = O(n)


str1 = "nameless"
str2 = "salesman"
r1 = are_anagrams1(str1, str2)
r2 = are_anagrams2(str1, str2)
print(r1)
print(r2)
