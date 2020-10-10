#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 48.RotateImage.py
# DATE : 2020/9/28 9:38 上午

__author__ = 'Jae'

from typing import List


# https://leetcode.com/problems/rotate-image/
class RotateImage:

    # 旋转
    # 每个角的坐标 i,j   n-j-1,i   n-i-1,n-j-1   j,n-i-1
    # Runtime: 32 ms, faster than 84.49% of Python3 online submissions for Rotate Image.
    # Memory Usage: 14 MB, less than 99.98% of Python3 online submissions for Rotate Image.
    def rotate2(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp

    # 对角线翻转,中线翻转
    # 注意每层数为i,每一层里的元素是j
    # 时间复杂度 O(n^2)
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        # 对角线翻转
        for i in range(length):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # print(matrix)
        # 中线翻转
        # for i in range(length):
        #     for j in range(length // 2):
        #         matrix[i][j], matrix[i][length - j - 1] = matrix[i][length - j - 1], matrix[i][j]
        for y, row in enumerate(matrix):
            matrix[y].reverse()


if __name__ == "__main__":
    rotateImage = RotateImage()
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(matrix)
    rotateImage.rotate(matrix)
    print(matrix)
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(matrix2)
    rotateImage.rotate2(matrix2)
    print(matrix2)
