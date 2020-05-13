#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'Jae'

from typing import List


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 求按键字母组合
class LetterCombinationsOfAPhoneNumber:

    def letterCombinations1(self, digits: str) -> List[str]:
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(mapping[digits[0]])

        prev = self.letterCombinations(digits[:-1])
        suffix = list(mapping[digits[-1]])

        return [j + i for j in prev for i in suffix]

    def __init__(self):
        self.keyMap = {
            "2": ('a', 'b', 'c'),
            "3": ('d', 'e', 'f'),
            "4": ('g', 'h', 'i'),
            "5": ('j', 'k', 'l'),
            "6": ('m', 'n', 'o'),
            "7": ('p', 'q', 'r', 's'),
            "8": ('t', 'u', 'v'),
            "9": ('w', 'x', 'y', 'z')
        }

    # Runtime: 20 ms, faster than 98.28% of Python3 online submissions for Letter Combinations of a Phone Number.
    # Memory Usage: 13.8 MB, less than 5.88% of Python3 online submissions for Letter Combinations of a Phone Number.
    # 回溯
    def letterCombinations(self, digits: str) -> List[str]:
        outPut = []
        length = len(digits)
        if length == 0: return outPut
        self.__back_num(outPut, "", digits)
        return outPut

    def __back_num(self, outPut, combin, digits):
        if len(digits) <= 0:
            outPut.append(combin)
            return
        for c in self.keyMap[digits[0]]:
            self.__back_num(outPut, combin + c, digits[1:])


if __name__ == "__main__":
    num = "23"
    check = LetterCombinationsOfAPhoneNumber()
    print(check.letterCombinations(num))
