#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 101.SymmetricTree.py
# DATE : 2021/4/14 09:47

__author__ = 'Jae'

from hot100.Stack import Stack
from hot100.TreeNode import TreeNode


# https://leetcode.com/problems/symmetric-tree/
class SymmetricTree:

    # BFS
    # Runtime: 36 ms, faster than 58.94% of Python3 online submissions for Symmetric Tree.
    # Memory Usage: 14.3 MB, less than 80.58% of Python3 online submissions for Symmetric Tree.
    def isSymmetric2(self, root: TreeNode) -> bool:
        rightList = []
        leftList = []
        rightList.append(root.right)
        leftList.append(root.left)
        while len(rightList) > 0 and len(leftList) > 0:
            right = rightList.pop()
            left = leftList.pop()
            if self.__checkNotNone(right, left) is False:
                return False
            if right is not None and left is not None:
                if right.val != left.val:
                    return False
                rightList.append(right.right)
                rightList.append(right.left)
                leftList.append(left.left)
                leftList.append(left.right)
        if len(rightList) > 0 or len(leftList) > 0:
            return False
        return True

    # Runtime: 36 ms, faster than 59.06% of Python3 online submissions for Symmetric Tree.
    # Memory Usage: 14.2 MB, less than 80.57% of Python3 online submissions for Symmetric Tree.
    # DFS
    def isSymmetric1(self, root: TreeNode) -> bool:
        stackRight = Stack()
        stackLeft = Stack()
        curRight = root.right
        curLeft = root.left
        while curRight is not None or stackRight.isNotEmpty() or curLeft is not None or stackLeft.isNotEmpty():
            while curLeft is not None:
                stackLeft.append(curLeft)
                curLeft = curLeft.left
            while curRight is not None:
                stackRight.append(curRight)
                curRight = curRight.right
            if len(stackRight) != len(stackLeft):
                return False

            curLeft = stackLeft.pop()
            curRight = stackRight.pop()

            if curLeft.val != curRight.val:
                return False

            curLeft = curLeft.right
            curRight = curRight.left

        return True

    # Runtime: 36 ms, faster than 50.48% of Python3 online submissions for Symmetric Tree.
    # Memory Usage: 14.5 MB, less than 10.70% of Python3 online submissions for Symmetric Tree.
    # 递归
    def isSymmetric(self, root: TreeNode) -> bool:
        if root.left is None and root.right is None: return True
        return self.__checkNode(root.left, root.right)

    def __checkNode(self, leftNode: TreeNode, rightNode: TreeNode):
        if self.__checkNotNone(leftNode, rightNode) is False: return False
        if leftNode.val != rightNode.val: return False
        if leftNode.right is not None or rightNode.left is not None:
            if self.__checkNode(leftNode.right, rightNode.left) is False: return False
        if leftNode.left is not None or rightNode.right is not None:
            if self.__checkNode(leftNode.left, rightNode.right) is False: return False
        return True

    def __checkNotNone(self, node1: TreeNode, node2: TreeNode):
        if node1 is not None and node2 is None: return False
        if node1 is None and node2 is not None: return False
        return True


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2_1 = TreeNode(2)
    node2_2 = TreeNode(2)
    node3_1 = TreeNode(3)
    node3_2 = TreeNode(3)
    node4_1 = TreeNode(4)
    node4_2 = TreeNode(4)
    check = SymmetricTree()

    node1.right = node2_1
    node1.left = node2_2

    # node2_1.right = node3_1
    # node2_2.left = node3_2
    # node2_1.left = node4_1
    # node2_2.right = node4_2

    node2_1.right = node3_1
    node2_2.right = node3_2

    print(check.isSymmetric(node1))
    print(check.isSymmetric1(node1))
    print(check.isSymmetric2(node1))
