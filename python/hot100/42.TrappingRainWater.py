#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

# https://leetcode.com/problems/trapping-rain-water/
from typing import List

from hot100.Stack import Stack


class TrappingRainWater:

    # 和动态规划做法相同，利用了python的zip特性 (将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组)
    # Runtime: 80 ms, faster than 28.83% of Python3 online submissions for Trapping Rain Water.
    # Memory Usage: 14.7 MB, less than 22.82% of Python3 online submissions for Trapping Rain Water.
    def trap3(self, height: List[int]) -> int:
        if not height: return 0
        max_left, max_right = [height[0]], [height[-1]]

        for i in range(1, len(height)):
            max_left.append(max(max_left[-1], height[i]))
            max_right.append(max(max_right[-1], height[-1 - i]))

        return sum(min(l, r) - h for l, r, h in zip(max_left, reversed(max_right), height))

    # 没有可以 peek 的stack
    # 使用栈来操作
    # https://leetcode.wang/leetCode-42-Trapping-Rain-Water.html
    # Runtime: 140 ms, faster than 7.22% of Python3 online submissions for Trapping Rain Water.
    # Memory Usage: 14.6 MB, less than 52.05% of Python3 online submissions for Trapping Rain Water.
    def trap2(self, height: List[int]) -> int:
        stack = Stack()
        current = 0
        sumVal = 0
        while current < len(height):
            while len(stack) > 0 and height[current] > height[stack.peek()]:
                h = height[stack.peek()]
                stack.pop()
                if stack.isEmpty(): continue
                distance = current - stack.peek() - 1
                minVal = min(height[current], height[stack.peek()])
                sumVal += distance * (minVal - h)
            stack.append(current)
            current += 1
        return sumVal

    # 动态规划
    # 求法和前面一样，通过存储最高墙，来优化时间
    # maxLeft[i] = max(maxLeft[i-1],height[i-1])
    # maxRight[i] = max(maxRight[i+1],height[i+1])
    # Runtime: 60 ms, faster than 57.34% of Python3 online submissions for Trapping Rain Water.
    # Memory Usage: 14.5 MB, less than 77.58% of Python3 online submissions for Trapping Rain Water.
    # O(n)
    def trap1(self, height: List[int]) -> int:
        totalWater = 0
        maxLeft = [0 for _ in range(len(height))]
        maxRight = maxLeft.copy()

        # 求出所有左边最高
        for index in range(1, len(height)):
            maxLeft[index] = max(maxLeft[index - 1], height[index - 1])

        # 求所有右边最高
        for index in range(len(height) - 2, 0, -1):
            maxRight[index] = max(maxRight[index + 1], height[index + 1])

        # 遍历求水
        for index, num in enumerate(height):
            max_left = maxLeft[index]
            max_right = maxRight[index]
            if num < max_left and num < max_right:
                totalWater += min(max_left, max_right) - num
        return totalWater

    # 按列求
    # 当前列高度与左右最高做比较
    # 1.比左右最高都小，水的高度就等于两边较小高度减去当前高度
    # 2.一样高度，没有水
    # 3.中间高度，也没有水
    # Runtime: 2904 ms, faster than 5.00% of Python3 online submissions for Trapping Rain Water.
    # Memory Usage: 14.7 MB, less than 14.78% of Python3 online submissions for Trapping Rain Water.
    def trap(self, height: List[int]) -> int:
        self.leftMax = 0
        totalWater = 0
        for index, num in enumerate(height):
            leftMax = self.__findLeftMax(height, index)
            rightMax = self.__findRightMax(height, index)
            if num < leftMax and num < rightMax:
                totalWater += min(leftMax, rightMax) - num
        return totalWater

    def __findLeftMax(self, height: List[int], index: int) -> int:
        if height[index] > self.leftMax:
            self.leftMax = height[index]
        return self.leftMax

    def __findRightMax(self, height: List[int], index: int):
        if index == len(height) - 1: return height[index]
        rightMax = 0
        for i in range(index + 1, len(height)):
            if rightMax < height[i]:
                rightMax = height[i]
        return rightMax


if __name__ == "__main__":
    list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    check = TrappingRainWater()
    print(check.trap(list))
    print(check.trap1(list))
    print(check.trap2(list))
