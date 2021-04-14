#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 96.UniqueBinarySearchTrees.py
# DATE : 2021/3/12 09:33

__author__ = 'Jae'

import collections


# https://leetcode.com/problems/unique-binary-search-trees/
class UniqueBinarySearchTrees:

    # Runtime: 28 ms, faster than 80.41% of Python3 online submissions for Unique Binary Search Trees.
    # Memory Usage: 14.2 MB, less than 48.17% of Python3 online submissions for Unique Binary Search Trees.
    # 卡塔兰数列  h(n) = h(0)*h(n-1) + h(1)*h(n-2) +....... + h(n-1)*h(0)  n>=1
    # 卡塔兰数列 https://baike.baidu.com/item/%E5%8D%A1%E7%89%B9%E5%85%B0%E6%95%B0/6125746
    # 乘阶 https://baike.baidu.com/item/%E9%98%B6%E4%B9%98/4437932?fr=aladdin
    # 组合数 https://baike.baidu.com/item/%E7%BB%84%E5%90%88%E6%95%B0
    def numTrees3(self, n: int) -> int:
        ans = 1
        for i in range(1, n + 1):
            ans = ans * (i + n) / i
        return int(ans // (n + 1))

    # Runtime: 32 ms, faster than 50.38% of Python3 online submissions for Unique Binary Search Trees.
    # Memory Usage: 14.2 MB, less than 48.17% of Python3 online submissions for Unique Binary Search Trees.
    # 因为是对称结构,因此只用算出一边 *2 就是两边长度,  偶数个数的再加上中间节点就可以了
    def numTrees2(self, n: int) -> int:
        if n == 0: return 0
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for len in range(2, n + 1):
            for root in range(1, len // 2 + 1):
                left = root - 1
                right = len - root
                dp[len] += dp[left] * dp[right]
            # 对称
            dp[len] = dp[len] * 2
            # 奇数时
            if len & 1 == 1:
                root = len // 2 + 1
                left = root - 1
                right = len - root
                dp[len] += dp[left] * dp[right]
        return dp[n]

    # Runtime: 32 ms, faster than 50.40% of Python3 online submissions for Unique Binary Search Trees.
    # Memory Usage: 14.2 MB, less than 76.52% of Python3 online submissions for Unique Binary Search Trees.
    def numTrees1(self, n: int) -> int:
        self.temp = collections.defaultdict()
        return self.__getAns(n)

    def __getAns(self, n) -> int:
        if self.temp.__contains__(n): return self.temp[n]
        if n <= 1: return 1
        ans = 0
        for i in range(1, n + 1):
            left = self.__getAns(i - 1)
            right = self.__getAns(n - i)
            ans += left * right
        self.temp[n] = ans
        return ans


if __name__ == "__main__":
    check = UniqueBinarySearchTrees()

    n = 3
    # Output: 5
    # print(check.numTrees1(n))
    # print(check.numTrees2(n))

    n1 = 1
    # Output: 1
    # print(check.numTrees1(n1))
    # print(check.numTrees2(n1))

    n2 = 4
    # 14
    print(check.numTrees1(n2))
    print(check.numTrees2(n2))
    print(check.numTrees3(n2))
