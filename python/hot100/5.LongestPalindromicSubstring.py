#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'


# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

class LongestPalindromicSubstring:

    # 解法 5: Manacher's Algorithm 马拉车算法。
    # https://www.cnblogs.com/grandyang/p/4475985.html   概念讲得很好
    # TODO

    # 方法四 中心拓展法
    #  每次循环选择一个中心，进行左右扩展，判断左右字符是否相等即可。
    # Runtime: 952 ms, faster than 75.47% of Python3 online submissions for Longest Palindromic Substring.
    # Memory Usage: 13.9 MB, less than 22.69% of Python3 online submissions for Longest Palindromic Substring.
    def longestPalindrome5(self, s: str) -> str:
        # 空串情况
        if s == "": return ""
        length = len(s)
        # 长度为1情况
        if length == 1: return s
        start, end = 0, 0
        for i in range(length):
            maxS = self.__expand_around(s, i, i)
            maxD = self.__expand_around(s, i, i + 1)
            maxLen = max(maxS, maxD)
            if maxLen > end - start:
                start = i - ((maxLen - 1) // 2)
                end = i + (maxLen // 2)
        return s[start:end + 1]

    def __expand_around(self, s, l, r):
        # 这里要包含边界情况
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return r - l - 1

    # 方法3优化 DP
    # i,j 都从大到小倒推   p[i,j] = p[i+1,j-1]
    # i 需 知道 i+1  j 需知道 j-1
    # 执行用时 :6680 ms, 在所有 Python3 提交中击败了11.07%的用户
    # 内存消耗 :13.6 MB, 在所有 Python3 提交中击败了 9.26% 的用户
    def longestPalindrome4(self, s: str) -> str:
        # 空串情况
        if s == "": return ""
        length = len(s)
        # 长度为1情况
        if length == 1: return s
        p = [False for _ in range(length)]
        res = ""
        for i in range(length - 1, -1, -1):
            for j in range(length - 1, -1, -1):
                p[j] = s[i] == s[j] and (j - i < 3 or p[j - 1])
                # print("i %s j %s p[%s] %s" % (i, j, j, p[j]))
                if p[j] and len(s[i:j + 1]) > len(res):
                    res = s[i: j + 1]
        return res

    # https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/
    # 使用DP 优化暴利求解
    # 执行用时 :7724 ms , 在所有 Python3 提交中击败了 5.19% 的用户
    # 内存消耗 :22.1 MB , 在所有 Python3 提交中击败了 5.55% 的用户
    def longestPalindrome3(self, s: str) -> str:
        # 空串情况
        if s == "": return ""
        length = len(s)
        # 长度为1情况
        if length == 1: return s
        dp = [[False for _ in range(0, length)] for _ in range(0, length)]
        maxLen = 0
        maxPal = ""
        # 遍历所有可能的回串长度 从长度1开始，到length结束
        for l in range(1, length + 1):
            for start in range(0, length):
                # 从0开始
                end = start + l - 1
                if end >= length:
                    continue
                # print("l %s start %s end %s" % (l, start, end))
                dp[start][end] = (l == 1 or l == 2 or dp[start + 1][end - 1]) and s[start] == s[end]
                if dp[start][end] and l > maxLen:
                    maxLen = l
                    maxPal = s[start:end + 1]
        return maxPal

    # 使用倒转会有bug，如 abfghdba  这种倒转后就会出现 ab是回串的现象
    # 2.最长公共子串，动态规划
    def longestPalindrome2(self, s: str) -> str:
        if s == "": return ""
        length = len(s)
        s2 = s[::-1]
        # 记录最长公共串
        maxLen = 0
        # 记录最长结尾位置
        maxEnd = 0
        dp = [[0 for _ in range(0, length)] for _ in range(0, length)]
        for i in range(0, length):
            for j in range(0, length):
                if s[i] == s2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                    if dp[i][j] > maxLen:
                        maxLen = dp[i][j]
                        maxEnd = i
        return s[(maxEnd - maxLen + 1):maxEnd + 1]

    # https://leetcode-cn.com/problems/longest-palindromic-substring/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-bao-gu/
    # 1.暴力求解法
    def longestPalindrome1(self, s: str) -> str:
        if s == "": return ""
        length = len(s)
        if length == 1: return s
        ans = ""
        maxLen = 0
        for i in range(length):
            for j in range(i, length):
                testStr = s[i:j + 1]
                # print("i %s j %s testStr %s" % (i, j, testStr))
                strLength = len(testStr)
                if self.__is_palindrome(testStr) and strLength > maxLen:
                    maxLen = strLength
                    ans = testStr
        return ans

    def __is_palindrome(self, s):
        length = len(s)
        for i in range(0, length // 2):
            if s[i] != s[length - i - 1]:
                return False
        return True


if __name__ == "__main__":
    s = "babad"
    s1 = "cbbd"
    s2 = "aacdefcaa"
    s3 = 'a'
    s4 = "ac"
    s5 = "bb"
    test = LongestPalindromicSubstring()
    # print(test.longestPalindrome1(s1))
    # print(test.longestPalindrome2(s1))
    # print(test.longestPalindrome2(s2))
    # print(test.longestPalindrome1(s2))
    # print(test.longestPalindrome3(s2))
    # print(test.longestPalindrome1(s3))
    # print(test.longestPalindrome3(s3))
    # print(test.longestPalindrome1(s4))
    # print(test.longestPalindrome3(s4))
    # print(test.longestPalindrome1(s5))
    # print(test.longestPalindrome1(s))
    # print(test.longestPalindrome4(s))
    print(test.longestPalindrome3(s5))
    print(test.longestPalindrome4(s5))
    print(test.longestPalindrome5(s5))
