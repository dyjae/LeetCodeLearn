#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 79.WordSearch.py
# DATE : 2021/1/21 09:47

__author__ = 'Jae'

# https://leetcode.com/problems/word-search/
from typing import List


class WordSearch:

    # dfs
    # 对于每一个数进行深度遍历,
    # 标记已经访问过的
    # 到达最后位置就可以返回
    # Runtime: 888 ms, faster than 5.01% of Python3 online submissions for Word Search.
    # Memory Usage: 15.3 MB, less than 98.28% of Python3 online submissions for Word Search.
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.row = len(board)
        if self.row == 0: return False
        self.col = len(board[0])
        for rowIndex in range(self.row):
            for colIndex in range(self.col):
                if self.__dfs(rowIndex, colIndex, 0): return True
        return False

    def __dfs(self, row, col, index) -> bool:
        if index >= len(self.word): return True
        if row < 0 or row >= self.row or col < 0 or col >= self.col: return False
        print("col:%s row%s index:%s" % (col, row, index))
        if self.word[index] != self.board[row][col]: return False
        # 当前位置标记为找过
        self.board[row][col] = chr(ord(self.board[row][col]) ^ 128)
        index += 1
        # 找上下左右
        if self.__dfs(row - 1, col, index): return True
        if self.__dfs(row + 1, col, index): return True
        if self.__dfs(row, col - 1, index): return True
        if self.__dfs(row, col + 1, index): return True
        self.board[row][col] = chr(ord(self.board[row][col]) ^ 128)
        return False


if __name__ == "__main__":
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCB"
    board = [["a", "a", "a", "a"], ["a", "a", "a", "a"], ["a", "a", "a", "a"]]
    word = "aaaaaaaaaaaa"
    check = WordSearch()
    print(check.exist(board, word))
