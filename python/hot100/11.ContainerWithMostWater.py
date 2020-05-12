#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

# https://leetcode.com/problems/container-with-most-water/
# 水桶最多放多少水
from typing import List


class ContainerWithMostWater:

    def maxArea(self, height: List[int]) -> int:
        # 2. two pointers
        result = 0
        i, j = 0, len(height) - 1
        while i < j:
            if height[i] < height[j]:
                result = max(result, height[i] * (j - i))
                i += 1
            else:
                result = max(result, height[j] * (j - i))
                j -= 1
        return result

    # 双指针法
    # Runtime: 132 ms, faster than 61.60% of Python3 online submissions for Container With Most Water.
    # Memory Usage: 15.4 MB, less than 5.26% of Python3 online submissions for Container With Most Water.
    def maxArea1(self, height: List[int]) -> int:
        rightPoint, leftPoint = len(height) - 1, 0
        maxWater = 0
        while rightPoint > leftPoint:
            rightVal = height[rightPoint]
            leftVal = height[leftPoint]
            nowWater = min(rightVal, leftVal) * (rightPoint - leftPoint)
            maxWater = max(maxWater, nowWater)
            if rightVal < leftVal:
                rightPoint -= 1
            else:
                leftPoint += 1
        return maxWater

    # 暴力法 遍历求出最多水位  TimeOut
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        maxRs = 0
        for i in range(length):
            for j in range(i + 1, length):
                maxWater = (j - i) * min(height[i], height[j])
                maxRs = max(maxRs, maxWater)
        return maxRs


if __name__ == "__main__":
    container = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    check = ContainerWithMostWater()
    print(check.maxArea1(container))
