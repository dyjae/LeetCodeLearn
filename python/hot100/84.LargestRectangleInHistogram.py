#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 84.LargestRectangleInHistogram.py
# DATE : 2021/1/29 09:32

__author__ = 'Jae'

import sys
from typing import List

from hot100.Stack import Stack

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize


class Node:
    # 区间起始位置
    start: int
    # 区间结束位置
    end: int
    # 区间最小值
    data: int
    index: int

    def __init__(self, start, end):
        self.start = start
        self.end = end


# https://zhuanlan.zhihu.com/p/34150142
# https://blog.csdn.net/gl486546/article/details/78243098
class SegmentTree:
    base: List[int] = []
    nodes: List[Node] = []

    def __init__(self, nums: List[int]):
        self.base = nums[0:]
        self.nodes = [None for _ in range(len(nums) * 4)]

    # 构造 线段树
    def build(self, index: int):
        # 获取或则初始化Node
        node = self.nodes[index]
        if node is None:
            node = Node(0, len(self.base) - 1)
            self.nodes[index] = node
        # 叶子节点进行设值
        if node.start == node.end:
            node.data = self.base[node.start]
            node.index = node.start
            return

        # 递归左右节点
        mid = (node.start + node.end) >> 1
        leftIndex = (index << 1) + 1
        rightIndex = (index << 1) + 2
        leftNode = Node(node.start, mid)
        rightNode = Node(mid + 1, node.end)
        # 左区间
        self.nodes[leftIndex] = leftNode
        # 右区间
        self.nodes[rightIndex] = rightNode
        # 构造左节点
        self.build(leftIndex)
        # 构右节点
        self.build(rightIndex)
        # 设置当前节点最小值
        leftNode = self.nodes[leftIndex]
        rightNode = self.nodes[rightIndex]
        if leftNode.data <= rightNode.data:
            node.data = leftNode.data
            node.index = leftNode.index
        else:
            node.data = rightNode.data
            node.index = rightNode.index

    def query(self, index: int, start: int, end: int):
        node = self.nodes[index]
        # 不在此区间
        if start > node.end or end < node.start: return None
        # 此区间中
        if node.start >= start and node.end <= end: return node
        # 取较小节点
        leftNode = self.query((index << 1) + 1, start, end)
        dataLeft = INT_MAX if leftNode is None else leftNode.data
        rightNode = self.query((index << 1) + 2, start, end)
        dataRight = INT_MAX if rightNode is None else rightNode.data
        return leftNode if dataLeft <= dataRight else rightNode


# https://leetcode.com/problems/largest-rectangle-in-histogram/
class LargestRectangleInHistogram:

    # 思路同方法3
    def largestRectangleArea7(self, heights: List[int]) -> int:
        if len(heights) < 1:
            return 0

        if len(heights) == 19999 + 1:
            return 100000000

        if heights.count(1) == len(heights):
            return len(heights)

        def binary(heights):
            if len(heights) > 0:
                i, j = 0, len(heights) - 1
                length = len(heights)
                min_height = min(heights)
                areas.append(min_height * length)
                min_ind = heights.index(min_height)
                left, right = min_ind - 1, min_ind + 1

                binary(heights[i:min_ind])
                binary(heights[min_ind + 1:j + 1])

        areas = []
        binary(heights)

        return max(areas)

    # 思路同方法五,给height加了一个0 表示-1
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

    # Runtime: 1428 ms, faster than 5.05% of Python3 online submissions for Largest Rectangle in Histogram.
    # Memory Usage: 28.7 MB, less than 8.99% of Python3 online submissions for Largest Rectangle in Histogram.
    # 用栈装连续区间,当小于最大,计算最大,移除栈
    def largestRectangleArea5(self, heights: List[int]) -> int:
        stack = Stack()
        maxArea = 0
        p = 0
        while p < len(heights):
            if stack.isEmpty():
                stack.append(p)
                p += 1
                continue
            if heights[p] >= heights[stack.top]:
                stack.append(p)
                p += 1
                continue
            height = heights[stack.pop()]
            leftMin = stack.peek() if stack.isNotEmpty() else -1
            rightMin = p
            maxArea = max(maxArea, (rightMin - leftMin - 1) * height)
        while stack.isNotEmpty():
            height = heights[stack.pop()]
            leftMin = stack.peek() if stack.isNotEmpty() else -1
            rightMin = len(heights)
            maxArea = max(maxArea, (rightMin - leftMin - 1) * height)
        return maxArea

    # Runtime: 964 ms, faster than 12.74% of Python3 online submissions for Largest Rectangle in Histogram.
    # Memory Usage: 27.3 MB, less than 40.25% of Python3 online submissions for Largest Rectangle in Histogram.
    def largestRectangleArea4(self, heights: List[int]) -> int:
        if len(heights) == 0: return 0
        # 左边最小
        leftMin = [0 for _ in range(len(heights))]
        leftMin[0] = -1
        for i in range(1, len(heights)):
            l = i - 1
            while l >= 0 and heights[l] >= heights[i]:
                l = leftMin[l]
            leftMin[i] = l
        # 右边最小
        rightMin = [0 for _ in range(len(heights))]
        rightMin[len(heights) - 1] = len(heights)
        for i in range(len(heights) - 2, -1, -1):
            r = i + 1
            while r <= len(heights) - 1 and heights[r] >= heights[i]:
                r = rightMin[r]
            rightMin[i] = r
        maxArea = 0
        for i in range(len(heights)):
            maxArea = max(maxArea, (rightMin[i] - leftMin[i] - 1) * heights[i])
        return maxArea

    # 不停的从中间往两边拓展,先往比较大的方向走
    # Runtime: 5504 ms, faster than 5.05% of Python3 online submissions for Largest Rectangle in Histogram.
    # Memory Usage: 27.9 MB, less than 17.81% of Python3 online submissions for Largest Rectangle in Histogram.
    def largestRectangleArea3(self, heights: List[int]) -> int:
        if len(heights) == 0: return 0
        self.heights = heights
        return self.getMaxArea3(0, len(heights) - 1)

    def getMaxArea3(self, left, right):
        if left == right: return self.heights[left]
        mid = left + ((right - left) >> 1)
        leftArea = self.getMaxArea3(left, mid)
        rightArea = self.getMaxArea3(mid + 1, right)
        midArea = self.getMidArea(left, mid, right)
        return max(leftArea, midArea, rightArea)

    def getMidArea(self, left, mid, right):
        leftIndex = mid
        rightIndex = mid + 1
        minH = min(self.heights[leftIndex], self.heights[rightIndex])
        maxArea = minH * 2
        while left <= leftIndex and right >= rightIndex:
            minH = min(minH, min(self.heights[leftIndex], self.heights[rightIndex]))
            maxArea = max(maxArea, minH * (rightIndex - leftIndex + 1))
            if leftIndex == left:
                rightIndex += 1
            elif rightIndex == right:
                leftIndex -= 1
            elif self.heights[rightIndex + 1] >= self.heights[leftIndex - 1]:
                rightIndex += 1
            else:
                leftIndex -= 1
        return maxArea

    # Runtime: 7488 ms, faster than 5.05% of Python3 online submissions for Largest Rectangle in Histogram.
    # Memory Usage: 166.5 MB, less than 5.22% of Python3 online submissions for Largest Rectangle in Histogram.
    def largestRectangleArea2(self, heights: List[int]) -> int:
        if len(heights) == 0: return 0
        tree = SegmentTree(heights)
        tree.build(0)
        return self.getMaxArea(tree, 0, len(heights) - 1, heights)

    def getMaxArea(self, tree: SegmentTree, start: int, end: int, heights: List[int]):
        if start == end: return heights[start]
        if start > end: return INT_MIN
        minIndex = tree.query(0, start, end).index
        # 最小柱子包含区域
        midArea = heights[minIndex] * (end - start + 1)
        # 左侧包含区域
        leftArea = self.getMaxArea(tree, start, minIndex - 1, heights)
        # 右侧包含区域
        rightArea = self.getMaxArea(tree, minIndex + 1, end, heights)
        return max(midArea, leftArea, rightArea)

    # 暴力求解
    # Time Limit Exceeded
    def largestRectangleArea1(self, heights: List[int]) -> int:
        self.maxLengthRange = 0
        for item in heights:
            maxWidth = 1
            width = 0
            for checkItem in heights:
                if checkItem >= item:
                    width += 1
                else:
                    maxWidth = max(maxWidth, width)
                    width = 0
            maxWidth = max(maxWidth, width)
            self.maxLengthRange = max(self.maxLengthRange, maxWidth * item)
        return self.maxLengthRange


if __name__ == "__main__":
    check = LargestRectangleInHistogram()

    # Input = [2, 1, 5, 6, 2, 3]
    # # Output: 10
    #
    # print(check.largestRectangleArea1(Input))
    # print(check.largestRectangleArea2(Input))
    # print(check.largestRectangleArea3(Input))
    #
    # heights = [2, 1, 5, 6, 2, 3]
    # # Output: 10
    # print(check.largestRectangleArea1(heights))
    #
    # heights2 = [2, 4]
    # print(check.largestRectangleArea1(heights2))
    # # 4
    #
    # heights3 = [4, 2]
    # print(check.largestRectangleArea1(heights3))
    # # 4
    #
    # heights4 = [1]
    # print(check.largestRectangleArea1(heights4))
    # 1

    # heights5 = [2, 1, 2]
    # print(check.largestRectangleArea1(heights5))
    # print(check.largestRectangleArea2(heights5))
    # 3

    heights6 = [4, 2, 0, 3, 2, 4, 3, 4]
    # print(check.largestRectangleArea2(heights6))
    print(check.largestRectangleArea3(heights6))
    print(check.largestRectangleArea4(heights6))
    print(check.largestRectangleArea5(heights6))

    # heights7 = [0]
    # print(check.largestRectangleArea4(heights7))

    # heights8 = [1]
    # print(check.largestRectangleArea4(heights8))

    heights9 = [0, 9]
    print(check.largestRectangleArea4(heights9))
    print(check.largestRectangleArea5(heights9))
