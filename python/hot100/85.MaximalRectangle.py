#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 85.MaximalRectangle.py
# DATE : 2021/3/4 09:39

__author__ = 'Jae'

from typing import List

# https://leetcode.com/problems/maximal-rectangle/
# https://leetcode.wang/leetCode-85-Maximal-Rectangle.html
class MaximalRectangle:

    # 同方法2
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not len(matrix) or not len(matrix[0]):
            return 0

        n = len(matrix[0])
        height = [0] * (n + 1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i] + 1 if row[i] == '1' else 0
            stack = [-1]
            for i in range(n + 1):
                while height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i - 1 - stack[-1]
                    ans = max(ans, h * w)
                stack.append(i)
        return ans

    # Runtime: 200 ms, faster than 78.77% of Python3 online submissions for Maximal Rectangle.
    # Memory Usage: 15.7 MB, less than 19.07% of Python3 online submissions for Maximal Rectangle.
    # 求每一个格子左边最小和右边最小
    # 下一层等于上一层最小和下一层0出现位置
    def maximalRectangle3(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        cols = len(matrix[0])
        maxArea = 0
        leftMin = [-1 for _ in range(cols + 1)]
        rightMin = [cols for _ in range(cols + 1)]
        heights = [0 for _ in range(cols)]
        for row in range(len(matrix)):
            # 求出高度和 leftMin
            minLeft = -1
            for col in range(cols):
                if matrix[row][col] == "1":
                    heights[col] += 1
                    leftMin[col] = max(leftMin[col], minLeft)
                else:
                    heights[col] = 0
                    leftMin[col] = -1
                    minLeft = col
            minRight = cols
            for col in range(cols - 1, -1, -1):
                if matrix[row][col] == "1":
                    rightMin[col] = min(rightMin[col], minRight)
                else:
                    rightMin[col] = minRight
                    minRight = col
                maxArea = max(maxArea, (rightMin[col] - leftMin[col] - 1) * heights[col])
        return maxArea

    # Runtime: 180 ms, faster than 99.49% of Python3 online submissions for Maximal Rectangle.
    # Memory Usage: 15.5 MB, less than 68.71% of Python3 online submissions for Maximal Rectangle.
    # 利用84题,求出每层最大面积,就是矩形最大面积
    def maximalRectangle2(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0: return 0
        heghts = [0 for _ in range(len(matrix[0]))]
        maxArea = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "1":
                    heghts[col] += 1
                else:
                    heghts[col] = 0
            maxArea = max(maxArea, self.largestRectangleArea6(heghts))
        return maxArea

    def largestRectangleArea6(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        heights.pop()
        return ans

    # 暴力求解
    # 遍历每个点,记录每个点最大宽度  ,向上遍历得到高度 * 最小宽度 求出最大面积
    # Time Limit Exceeded
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        maxArea = 0
        widths = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # 求row,col 最大宽度
                if matrix[row][col] != "1":
                    widths[row][col] = 0
                elif col == 0:
                    widths[row][col] = 1
                else:
                    widths[row][col] = widths[row][col - 1] + 1
                # 向上取高 乘以 最小宽度  求面积
                minWidth = widths[row][col]
                for up_row in range(row, -1, -1):
                    height = row - up_row + 1
                    minWidth = min(minWidth, widths[up_row][col])
                    maxArea = max(maxArea, minWidth * height)
        return maxArea


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    check = MaximalRectangle()
    # Output: 6
    print(check.maximalRectangle(matrix))
    print(check.maximalRectangle2(matrix))
    print(check.maximalRectangle3(matrix))

    # matrix2 = []
    # Output: 0

    # matrix3 = [["0"]]
    # Output: 0
