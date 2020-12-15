#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 64.MinimumPathSum.py
# DATE : 2020/12/9 09:48

__author__ = 'Jae'

# https://leetcode.com/problems/minimum-path-sum/
import sys
from typing import List

maxInt = sys.maxsize


class MinimumPathSum:

    # 覆盖原值
    def minPathSum2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] = grid[0][i] + grid[0][i - 1]
        for j in range(1, m):
            grid[j][0] = grid[j][0] + grid[j - 1][0]
        for x in range(1, m):
            for y in range(1, n):
                grid[x][y] = grid[x][y] + min(grid[x - 1][y], grid[x][y - 1])
        return grid[m - 1][n - 1]

    # dp
    # dp[i][j] = min(dp[i-1][j]+dp[i][j],dp[i][j-1])
    # Runtime: 136 ms, faster than 9.86% of Python3 online submissions for Minimum Path Sum.
    # Memory Usage: 19.8 MB, less than 5.66% of Python3 online submissions for Minimum Path Sum.
    def minPathSum1(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.minValMap = {f'{self.m - 1}_{self.n - 1}': grid[-1][-1]}
        return self.__find_min(0, 0)

    def __find_min(self, x, y):
        key = f'{x}_{y}'
        if key in self.minValMap:
            return self.minValMap[key]
        l1, l2 = maxInt, maxInt
        if x + 1 < self.m:
            l1 = self.__find_min(x + 1, y)
        if y + 1 < self.n:
            l2 = self.__find_min(x, y + 1)
        minPath = min(l1, l2) + self.grid[x][y]
        self.minValMap[key] = minPath
        return minPath


## TODO ERROR Expected 7
if __name__ == "__main__":
    # grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    # grid = [[1, 2, 3], [4, 5, 6]]
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    checker = MinimumPathSum()
    print(checker.minPathSum1(grid))
