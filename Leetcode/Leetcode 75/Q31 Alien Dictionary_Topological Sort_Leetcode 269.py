"""
There is a new alien language that uses the English alphabet. However, the order among the letter is
unknown to you.

You are given a list of strings words from the alien language's dictionary, where the strings in words
are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically increasing order
by the new language;s rules. If there is no solution, return "".If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, the letter
in s comes before the in t in the alien language. If the first min(s.length, t.length) letters are the same,
then s is smaller if and only if s.length < t,length.

Example 1:
    Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
    Output: "wertf"
"""
from typing import List


def alien_order(words: List[str]):
    adj = {c: set() for w in words for c in w}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))
        if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
            return ""
        for j in range(min_len):
            if w1[j] != w2[j]:
                adj[w1[j]].add(w2[j])
                break

    visited = {}  # False = visited, True = current path
    res = []

    def dfs(c):
        if c in visited:
            return visited[c]

        visited[c] = True
        for nei in adj[c]:
            if dfs(nei):
                return True
        visited[c] = False
        res.append(c)

    for c in adj:
        if dfs(c):
            return ""
    res.reverse()
    return "".join(res)


print(alien_order(["wrt", "wrf", "er", "ett", "rftt"]))
