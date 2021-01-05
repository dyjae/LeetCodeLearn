#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 76.MinimumWindowSubstring.py
# DATE : 2020/12/17 10:15

__author__ = 'Jae'

# https://leetcode.com/problems/minimum-window-substring/
import collections
import sys

maxInt = sys.maxsize


class MinimumWindowSubstring:

    # collections.Counter(t) 计数器
    # enumerate(s, 1) 从第一位开始遍历
    def minWindow2(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    # Runtime: 96 ms, faster than 88.01% of Python3 online submissions for Minimum Window Substring.
    # Memory Usage: 15 MB, less than 24.81% of Python3 online submissions for Minimum Window Substring.
    # 窗口, 左右指针圈定窗口
    def minWindow(self, s: str, t: str) -> str:
        tArray = [0 for _ in range(58)]
        for c in t:
            cLow = ord(c) - 65
            tArray[cLow] = tArray[cLow] + 1
        left = 0
        right = 0
        ans_left = 0
        ans_right = -1
        ans_len = maxInt
        count = len(t)
        while right < len(s):
            rightC = ord(s[right]) - 65
            tArray[rightC] -= 1
            # 当前字符包含在需要字符中
            if tArray[rightC] >= 0: count -= 1
            # 移动左边指针
            while count == 0:
                temp_len = right - left + 1
                if temp_len < ans_len:
                    ans_left = left
                    ans_right = right
                    ans_len = temp_len
                # 这里是进行左边移动
                leftC = ord(s[left]) - 65
                # 前面已经减过,这里再加上,大于0的话代表着这个是t中包含的
                tArray[leftC] += 1
                if tArray[leftC] > 0: count += 1
                left += 1
            right += 1
        return s[ans_left: ans_right + 1]


if __name__ == "__main__":
    # s = "ADOBECODEBANC"
    # t = "ABC"
    # s = "ab"
    # t="A"
    s = "cgklivwehljxrdzpfdqsapogwvjtvbzahjnsejwnuhmomlfsrvmrnczjzjevkdvroiluthhpqtffhlzyglrvorgnalk"
    t = "mqfff"
    checker = MinimumWindowSubstring()
    print(checker.minWindow(s, t))
    print(checker.minWindow2(s, t))
