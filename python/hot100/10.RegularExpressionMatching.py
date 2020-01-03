#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'


# https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode/

class RegularExpressionMatching:

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]

        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = i < len(s) and p[j] in {s[i], '.'}
                if j + 1 < len(p) and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

    # def isMatch(self, s: str, p: str) -> bool:
    #     # dp[i][j] 对应的是  p[i-1]  s[j-1]
    #     dp = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]
    #     # 空串与空匹配式是匹配的
    #     dp[0][0] = True
    #     # * 与 空串都是匹配的
    #     for i in range(1, len(p)):
    #         dp[i + 1][0] = dp[i - 1][0] and p[i] == '*'
    #     for i in range(len(p)):
    #         for j in range(len(s)):
    #             if p[i] == '*':
    #                 # https://blog.csdn.net/jackhell2/article/details/79424861
    #                 # 3. 当p[i] = ‘*’ 时 有几种情况可以将真值传递下去
    #                 #     1. dp[i + 1][j + 1] = dp[i - 1][j + 1]
    #                 #     2. dp[i + 1][j + 1] = dp[i][j + 1]
    #                 #     3. dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i + 1][j]
    #                 dp[i + 1][j + 1] = dp[i - 1][j + 1] or dp[i][j + 1]
    #                 if p[i - 1] == s[j] or p[i - 1] == '.':
    #                     dp[i + 1][j + 1] |= dp[i + 1][j]
    #             else:
    #                 # 当p[i]不为*时 是否匹配取决于  上一个是否匹配为和（当前是否匹配，或p[i]是否为*）
    #                 dp[i + 1][j + 1] = dp[i][j] and (p[i] == s[j] or p[i] == '.')
    #     return dp[-1][-1]

    # 带存储
    # def isMatch(self, s: str, p: str) -> bool:
    #     memo = dict()
    #
    #     def dp(i, j):
    #         if (i, j) in memo: return memo[(i, j)]
    #         if len(p) == 0: return len(s) == 0
    #         firstMatch = len(s) > 0 and p[0] in {s[0], '.'}
    #         if len(p) >= 2 and p[1] == '*':
    #             ans = self.isMatch(s, p[2:]) or \
    #                   firstMatch and self.isMatch(s[1:], p)
    #         else:
    #             ans = firstMatch and self.isMatch(s[1:], p[1:])
    #         memo[(i, j)] = ans
    #         return ans
    #
    #     return dp(0, 0)


# 递归法
# def isMatch(self, s: str, p: str) -> bool:
#     if len(p) == 0: return len(s) == 0
#     firstMatch = len(s) > 0 and p[0] in {s[0], '.'}
#     if len(p) >= 2 and p[1] == '*':
#         return self.isMatch(s, p[2:]) or \
#                firstMatch and self.isMatch(s[1:], p)
#     return firstMatch and self.isMatch(s[1:], p[1:])

s = "aaaaaaaaaaaaab"
p = "a*a*a*a*a*a*a*a*a*a*c"
reg = RegularExpressionMatching()
print(reg.isMatch(s, p))

s = "aa"
p = "a"
print(reg.isMatch(s, p))

p = "a*"
print(reg.isMatch(s, p))

s = "ab"
p = ".*"
print(reg.isMatch(s, p))

s = "aab"
p = "c*a*b"
print(reg.isMatch(s, p))

s = "mississippi"
p = "mis*is*p*."
print(reg.isMatch(s, p))

# https://www.cnblogs.com/forfreewill/articles/9406935.html
# class Queue(object):
#
#     def __init__(self, len):
#         self.data = []
#         self.len = len
#
#     def pop(self):
#         return self.data.pop(0)
#
#     def push(self, value):
#         if len(self.data) < self.len:
#             self.data.append(value)
#         else:
#             raise IOError("full")
#
#     def peek(self):
#         return self.data[0]
#
#     def empty(self):
#         return not bool(self.data)
#
#     def find(self, value):
#         return self.data.index(value)
#
#     def __str__(self):
#         return str(self.data)
