#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 62.UniquePaths.py
# DATE : 2020/12/7 09:11

__author__ = 'Jae'


# https://leetcode.com/problems/unique-paths/
class UniquePaths:

    # 同下面
    # 乘阶
    def uniquePaths4(self, m: int, n: int) -> int:
        from math import factorial
        N = n + m - 2
        k = m - 1
        return factorial(N) // (factorial(N - k) * factorial(k))

    # Runtime: 24 ms, faster than 95.00% of Python3 online submissions for Unique Paths.
    # Memory Usage: 14.1 MB, less than 51.27% of Python3 online submissions for Unique Paths.
    # 公式求解
    # 从左上角，到右下角，总会是 3 个 R，2 个 D，只是出现的顺序不一样。所以求解法，本质上是求了组合数，
    # N = m + n - 2，也就是总共走的步数。
    # k = m - 1，也就是向下的步数，D 的个数。
    # 所以总共的解就是 C^k_n = n!/(k!(n-k)!) = (n*(n-1)*(n-2)*...(n-k+1))/k!C
    def uniquePaths3(self, m: int, n: int) -> int:
        N = m + n - 2
        k = m - 1
        res = 1
        for i in range(1, k + 1):
            res = res * (N - k + i) / i
        return int(res)

    # Runtime: 32 ms, faster than 55.70% of Python3 online submissions for Unique Paths.
    # Memory Usage: 14.2 MB, less than 26.71% of Python3 online submissions for Unique Paths.
    # DP     dp [ i ] [ j ] = dp [ i + 1 ] [ j ] + dp [ i ] [ j +1 ]。
    # 可以一列一列的推进  初始化第一列为1 dp[j] = dp[j]+dp[j-1]
    def uniquePaths2(self, m: int, n: int) -> int:
        dp = [1 for _ in range(0, m)]
        for i in range(n - 2, -1, -1):
            for j in range(m - 2, -1, -1):
                dp[j] = dp[j + 1] + dp[j]
        return dp[0]

    # 递归
    # Runtime: 40 ms, faster than 6.50% of Python3 online submissions for Unique Paths.
    # Memory Usage: 14.3 MB, less than 13.25% of Python3 online submissions for Unique Paths.
    def uniquePaths1(self, m: int, n: int) -> int:
        # 终点
        self.targetM = m
        self.targetN = n
        key = f'{m}_{n}'
        self.hasFind = {key: 1}
        return self.__find_path(1, 1)

    def __find_path(self, x: int, y: int) -> int:
        key = f'{x}_{y}'
        if key in self.hasFind:
            return self.hasFind[key]
        n1 = 0
        if x < self.targetM:
            n1 = self.__find_path(x + 1, y)
        # 下移
        n2 = 0
        if y < self.targetN:
            n2 = self.__find_path(x, y + 1)
        sum = n1 + n2
        self.hasFind[key] = sum
        return sum


if __name__ == "__main__":
    # m = 3
    # n = 7
    m = 3
    n = 2
    check = UniquePaths()
    print(check.uniquePaths1(m, n))
    print(check.uniquePaths2(m, n))
    print(check.uniquePaths3(m, n))
