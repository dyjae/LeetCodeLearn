#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'


# https://leetcode.com/problems/longest-valid-parentheses/submissions/
class LongestValidParentheses:

    # Runtime: 44 ms, faster than 62.41% of Python3 online submissions for Longest Valid Parentheses.
    # Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Longest Valid Parentheses.
    # 方法4：不需要额外的空间
    def longestValidParenthesesDPNoSpace(self, s: str) -> int:
        leftSize = 0
        rightSize = 0
        maxSize = 0
        for c in s:
            if c == '(':
                leftSize += 1
            elif c == ')':
                rightSize += 1
            if leftSize == rightSize:
                maxSize = max(maxSize, leftSize * 2)
            elif rightSize > leftSize:
                leftSize = 0
                rightSize = 0
        leftSize = 0
        rightSize = 0
        for c in s[::-1]:
            if c == '(':
                leftSize += 1
            elif c == ')':
                rightSize += 1
            if leftSize == rightSize:
                maxSize = max(maxSize, rightSize * 2)
            elif rightSize < leftSize:
                leftSize = 0
                rightSize = 0
        return maxSize

    # Runtime: 52 ms, faster than 24.81% of Python3 online submissions for Longest Valid Parentheses.
    # Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Valid Parentheses.
    # dp
    def longestValidParenthesesDP(self, s: str) -> int:
        maxSize = 0
        dp = []
        for i in range(len(s)):
            dp.append(0)
            if s[i] == ')':
                if i > 0 and s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                elif i > 2 and s[i - 1] == ')' and i > dp[i - 1] and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] > 2:
                        dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                    else:
                        dp[i] = dp[i - 1] + 2
            maxSize = max(dp[i], maxSize)
        return maxSize


'''
与找到每个可能的子字符串后再判断它的有效性不同，我们可以用栈在遍历给定字符串的过程中去判断到目前为止扫描的子字符串的有效性，同时能的都最长有效字符串的长度。我们首先将 -1−1 放入栈顶。

对于遇到的每个 \text{‘(’}‘(’ ，我们将它的下标放入栈中。
对于遇到的每个 \text{‘)’}‘)’ ，我们弹出栈顶的元素并将当前元素的下标与弹出元素下标作差，得出当前有效括号字符串的长度。通过这种方法，我们继续计算有效子字符串的长度，并最终返回最长有效子字符串的长度。

'''


# 栈
def longestValidParenthesesStack(self, s: str) -> int:
    stack = [-1]
    ml = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                ml = max(ml, i - stack[-1])
    return ml


if __name__ == "__main__":
    lp = LongestValidParentheses()
    # print(lp.longestValidParentheses("(()"))
    # print(lp.longestValidParentheses(")()())"))
    # print(lp.longestValidParenthesesDP("()()"))
    # print(lp.longestValidParenthesesDP(")()())"))
    # print(lp.longestValidParenthesesDP("()(()"))
    print(lp.longestValidParenthesesDPNoSpace("(()"))
