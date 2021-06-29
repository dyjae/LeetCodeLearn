#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 105.ConstructBinaryTreeFromPreorderAndInorderTraversal
# DATE : 2021/06/24 09:22

__author__ = 'Jae'

import sys
from typing import List

from hot100.Stack import Stack
from hot100.TreeNode import TreeNode

maxInt = sys.maxsize


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class ConstructBinaryTreeFromPreorderAndInorderTraversal:

    # DFS
    def buildTree3(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        ans = {}
        for i, v in enumerate(inorder):
            ans[v] = i

        # print(ans)
        def dfs(low, high):
            if low > high:
                return None
            root = TreeNode(preorder.pop(0))
            mid = ans[root.val]
            root.left = dfs(low, mid - 1)
            root.right = dfs(mid + 1, high)

            return root

        return dfs(0, len(inorder) - 1)


    # Runtime: 56 ms, faster than 90.00% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    # Memory Usage: 17.8 MB, less than 99.39% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    # 前序遍历  中 左右  中序遍历  左中右
    # stack + 中 左  左     左== 中序左  前中=中中   +中右
    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        treeStack = Stack()
        preIndex = 0
        inIndex = 0
        curTree = TreeNode(preorder[preIndex])
        root = curTree
        preIndex += 1
        treeStack.append(curTree)
        while preIndex < len(preorder):
            if inorder[inIndex] == curTree.val:
                while treeStack.isNotEmpty() and inorder[inIndex] == treeStack.peek().val:
                    curTree = treeStack.pop()
                    inIndex += 1
                curTree.right = TreeNode(preorder[preIndex])
                curTree = curTree.right
                treeStack.append(curTree)
                preIndex += 1
            else:
                curTree.left = TreeNode(preorder[preIndex])
                curTree = curTree.left
                treeStack.append(curTree)
                preIndex += 1
        return root

    preIndex = 0
    inIndex = 0

    # Runtime: 52 ms, faster than 95.99% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    # Memory Usage: 18.1 MB, less than 96.67% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
    # 递归
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.__createTree(preorder, inorder, maxInt)

    def __createTree(self, preorder: List[int], inorder: List[int], stop: int) -> TreeNode or None:
        if self.preIndex == len(preorder): return None
        if inorder[self.inIndex] == stop:
            self.inIndex += 1
            return None
        root_val = preorder[self.preIndex]
        self.preIndex += 1
        tree = TreeNode(root_val)
        leftTree = self.__createTree(preorder, inorder, root_val)
        rightTree = self.__createTree(preorder, inorder, stop)
        tree.left = leftTree
        tree.right = rightTree
        return tree


if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]

    check = ConstructBinaryTreeFromPreorderAndInorderTraversal()
    print(check.buildTree(preorder, inorder))
    print(check.buildTree2(preorder, inorder))
