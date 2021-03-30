#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 95.UniqueBinarySearchTreesII.py
# DATE : 2021/3/15 09:34

__author__ = 'Jae'

from typing import List

from hot100.TreeNode import TreeNode


# https://leetcode.com/problems/unique-binary-search-trees-ii/
class UniqueBinarySearchTreesII:

    # Runtime: 68 ms, faster than 15.94% of Python3 online submissions for Unique Binary Search Trees II.
    # Memory Usage: 16.4 MB, less than 5.31% of Python3 online submissions for Unique Binary Search Trees II.
    # 新插入一个数,有两种情况: 1.当做根节点之前节点为当前节点左节点,  2.放到右节点
    def generateTrees3(self, n: int) -> List[TreeNode]:
        pre = []
        if n == 0: return pre
        pre.append(None)
        for i in range(1, n + 1):
            cur = []
            for tree in pre:
                insert = TreeNode(i)
                insert.left = tree
                cur.append(insert)
                for j in range(n + 1):
                    rootCopy = self.__treeCopy(tree)
                    right = rootCopy
                    k = 0
                    for _ in range(k, j):
                        if right is None: break
                        right = right.right
                    if right is None: break
                    rightTree = right.right
                    insert = TreeNode(i)
                    right.right = insert
                    insert.left = rightTree
                    cur.append(rootCopy)
            pre = cur
        return pre

    def __treeCopy(self, root: TreeNode):
        if root is None: return root
        newTree = TreeNode(root.val)
        newTree.left = self.__treeCopy(root.left)
        newTree.right = self.__treeCopy(root.right)
        return newTree

    # Runtime: 60 ms, faster than 60.41% of Python3 online submissions for Unique Binary Search Trees II.
    # Memory Usage: 16.1 MB, less than 17.99% of Python3 online submissions for Unique Binary Search Trees II.
    def generateTrees2(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        dp = [[] for _ in range(n + 1)]
        dp[0].append(None)
        for index in range(1, n + 1):
            for root in range(1, index + 1):
                left = root - 1  # 左树长度
                right = index - root  # 右树长度
                for leftTree in dp[left]:
                    for rightTree in dp[right]:
                        treeRoot = TreeNode(root)
                        treeRoot.left = leftTree
                        treeRoot.right = self.clone(rightTree, root)
                        dp[index].append(treeRoot)
        return dp[n]

    def clone(self, tree: TreeNode, offset: int):
        if tree is None: return None
        newTree = TreeNode(tree.val + offset)
        newTree.left = self.clone(tree.left, offset)
        newTree.right = self.clone(tree.right, offset)
        return newTree

    # Runtime: 60 ms, faster than 60.41% of Python3 online submissions for Unique Binary Search Trees II.
    # Memory Usage: 15.5 MB, less than 83.48% of Python3 online submissions for Unique Binary Search Trees II.
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: return []
        return self.__getTree(1, n)

    def __getTree(self, start: int, end: int) -> List[TreeNode]:
        if start > end:
            return [None]
        if start == end:
            return [TreeNode(start)]
        rs = []
        for index in range(start, end + 1):
            # 取所有可能的右节点
            rightTrees = self.__getTree(index + 1, end)
            # 取所有可能的左节点
            leftTrees = self.__getTree(start, index - 1)

            for rightTree in rightTrees:
                for leftTree in leftTrees:
                    rsTree = TreeNode(index)
                    rsTree.right = rightTree
                    rsTree.left = leftTree
                    rs.append(rsTree)
        return rs


if __name__ == "__main__":
    check = UniqueBinarySearchTreesII()
    trees = check.generateTrees(3)
    trees2 = check.generateTrees2(3)
    trees3 = check.generateTrees3(3)
    print("end")
