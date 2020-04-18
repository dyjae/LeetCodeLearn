#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'


# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class LongestSubstringWithoutRepeatingCharacters:

    # 3.滑动窗口优化
    # 通过保存重复字符串位置，直接跳过该位置
    # Runtime: 76 ms, faster than 39.99% of Python3 online submissions for Longest Substring Without Repeating Characters.
    # Memory Usage: 14.1 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
    def lengthOfLongestSubstring3(self, s: str) -> int:
        cMap = dict()
        ans, i = 0, 0
        for j in range(len(s)):
            c = s[j]
            if cMap.keys().__contains__(c):
                index = cMap.get(c)
                i = max(i, index + 1)
            ans = max(ans, j - i + 1)
            cMap[c] = j
        return ans

    # 2.滑动窗口
    # 左右两个节点，有右边不停移动，直到右边在串中有重复，把左边移动到串位加1
    # 时间复杂度：O(2n) = O(n)O(2n)=O(n)，在最糟糕的情况下，每个字符将被 ii 和 jj 访问两次。
    # 空间复杂度：O(min(m, n))O(min(m,n))，与之前的方法相同。滑动窗口法需要 O(k)O(k) 的空间，其中 kk 表示 Set 的大小。而 Set 的大小取决于字符串 nn 的大小以及字符集 / 字母 mm 的大小。
    # Runtime: 72 ms, faster than 46.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
    # Memory Usage: 13.8 MB, less than 5.10% of Python3 online submissions for Longest Substring Without Repeating Characters.
    def lengthOfLongestSubstring2(self, s: str) -> int:
        cSet = set()
        length = len(s)
        ans, i, j = 0, 0, 0
        while i < length and j < length:
            if cSet.__contains__(s[j]):
                cSet.remove(s[i])
                i += 1
            else:
                cSet.add(s[j])
                j += 1
                ans = max(ans, j - i)
        return ans

    # 1.暴利求解 会出现超时
    # https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/wu-zhong-fu-zi-fu-de-zui-chang-zi-chuan-by-leetcod/
    # 时间复杂度： n^3
    # 空间复杂度： min(n,m)  m
    def lengthOfLongestSubstring1(self, s: str) -> int:
        length = len(s)
        maxLen = 0
        for i in range(length):
            for j in range(i, length):
                checkStr = s[i:j + 1]
                strLen = len(checkStr)
                if self.__checkWithoutRepeating(checkStr) and strLen > maxLen:
                    maxLen = strLen
        return maxLen

    # 监测字符串是否有重复
    def __checkWithoutRepeating(self, s):
        chartSet = set()
        for c in s:
            if chartSet.__contains__(c): return False
            chartSet.add(c)
        return True


if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = "tmmzuxt"
    checker = LongestSubstringWithoutRepeatingCharacters()
    # print(checker.lengthOfLongestSubstring1(s1))
    # print(checker.lengthOfLongestSubstring1(s2))
    # print(checker.lengthOfLongestSubstring1(s3))
    # print(checker.lengthOfLongestSubstring2(s1))
    # print(checker.lengthOfLongestSubstring2(s2))
    print(checker.lengthOfLongestSubstring2(s3))
    # print(checker.lengthOfLongestSubstring3(s1))
    # print(checker.lengthOfLongestSubstring3(s2))
    print(checker.lengthOfLongestSubstring3(s3))
    print(checker.lengthOfLongestSubstring2(s4))
    print(checker.lengthOfLongestSubstring3(s4))
