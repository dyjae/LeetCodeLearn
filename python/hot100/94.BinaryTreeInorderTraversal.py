#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# CONTACT : dyjae@vip.qq.com
# FILE : 94.BinaryTreeInorderTraversal.py
# DATE : 2021/3/9 10:04

__author__ = 'Jae'

from typing import List

from hot100.Stack import Stack
from hot100.TreeNode import TreeNode


# https://leetcode.com/problems/binary-tree-inorder-traversal/
class BinaryTreeInorderTraversal:

    # 同方法一
    def inorderTraversal4(self, root: TreeNode) -> List[int]:
        if root is None: return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

    # Runtime: 32 ms, faster than 62.66% of Python3 online submissions for Binary Tree Inorder Traversal.
    # Memory Usage: 14.2 MB, less than 78.00% of Python3 online submissions for Binary Tree Inorder Traversal.
    # 将最后一个右节点的右节点放在下一个要遍历的节点
    def inorderTraversal3(self, root: TreeNode) -> List[int]:
        rs = []
        cur = root
        while cur is not None:
            if cur.left is None:
                rs.append(cur.val)
                cur = cur.right
                continue
            pre = cur.left
            # 找到左子节点的最右节点
            while pre.right is not None and pre.right is not cur:
                pre = pre.right
            if pre.right is None:
                pre.right = cur
                cur = cur.left
            if pre.right == cur:
                pre.right = None
                rs.append(cur.val)
                cur = cur.right
        return rs

    # Runtime: 28 ms, faster than 85.77% of Python3 online submissions for Binary Tree Inorder Traversal.
    # Memory Usage: 14.3 MB, less than 15.95% of Python3 online submissions for Binary Tree Inorder Traversal.
    # 压栈方式
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        rs = []
        stack = Stack()
        cur = root
        while cur is not None or stack.isNotEmpty():
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            rs.append(cur.val)
            cur = cur.right
        return rs

    # Runtime: 32 ms, faster than 62.66% of Python3 online submissions for Binary Tree Inorder Traversal.
    # Memory Usage: 14.3 MB, less than 15.95% of Python3 online submissions for Binary Tree Inorder Traversal.
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None: return []
        rs = []
        if root.left is not None:
            rs += self.inorderTraversal(root.left)
        rs.append(root.val)
        if root.right is not None:
            rs += self.inorderTraversal(root.right)
        return rs


if __name__ == "__main__":
    tree1 = TreeNode(1)
    tree2 = TreeNode(2)
    tree3 = TreeNode(3)
    check = BinaryTreeInorderTraversal()

    tree1.right = tree2
    tree2.left = tree3
    print(check.inorderTraversal(tree1))
    print(check.inorderTraversal2(tree1))
    print(check.inorderTraversal3(tree1))
    print(check.inorderTraversal4(tree1))

    # tree1.left = tree2
    # print(check.inorderTraversal(tree1))

    # tree1.right = tree2
    # print(check.inorderTraversal(tree1))
