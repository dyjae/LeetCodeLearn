#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
from hot100.TreeNode import TreeNode

__author__ = 'Jae'


class ValidateBinarySearchTree:
    # Runtime: 40 ms, faster than 85.42% of Python3 online submissions for Validate Binary Search Tree.
    # Memory Usage: 15.1 MB, less than 100.00% of Python3 online submissions for Validate Binary
    def isValidBST(self, root: TreeNode) -> bool:
        if root.val is None: return True
        return self.__validateTree(root.left, root.val, None) and self.__validateTree(root.right, None, root.val)

    def __validateTree(self, root: TreeNode, max, min):
        if root is None: return True
        if max is not None and root.val > max: return False
        if min is not None and root.val < min: return False
        return self.__validateTree(root.left, root.val, None) and self.__validateTree(root.right, None, root.val)

    def isValidBST2(self, root: TreeNode, upperLimit=float('inf'), lowerLimit=float('-inf')) -> bool:
        if root is None:
            return True
        if root is not None and upperLimit > root.val > lowerLimit:
            return self.isValidBST2(root.left, root.val, lowerLimit) and self.isValidBST2(root.right, upperLimit,root.val)
        else:
            return False

if __name__ == '__main__':
    validate = ValidateBinarySearchTree()
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    tree4 = TreeNode(4)
    tree5 = TreeNode(5)
    tree6 = TreeNode(6)

    # tree2.right = tree3
    # tree2.left = tree1
    #
    # print(validate.isValidBST(tree2))

    tree5.left = tree1
    tree5.right = tree4
    tree4.left = tree3
    tree4.right = tree6
    print(validate.isValidBST(tree5))
