package com.jae.leetcode.tree

/**
 * @Description: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 * @Author yj
 * @Date 2019-08-07 09:43
 **/

fun main(args: Array<String>) {
    val root3 = TreeNode(null, null, 3)
    val root5 = TreeNode(null, null, 5)
    val root1 = TreeNode(null, null, 1)
    root3.left = root5
    root3.right = root1

    val root6 = TreeNode(null, null, 6)
    val root2 = TreeNode(null, null, 2)
    root5.left = root6
    root5.right = root2

    val root0 = TreeNode(null, null, 0)
    val root8 = TreeNode(null, null, 8)
    root1.left = root0
    root1.right = root8

    val root7 = TreeNode(null, null, 7)
    val root4 = TreeNode(null, null, 4)
    root2.left = root7
    root2.right = root4

    val treeNode = lowestCommonAncestor(root3, root5, root1)
    println(treeNode)
}

fun lowestCommonAncestor(root: TreeNode?, p: TreeNode, q: TreeNode): Int? {
    if (root == null || root == p || root == q) return root?.value
    val left = lowestCommonAncestor(root.left, p, q)
    val right = lowestCommonAncestor(root.right, p, q)
    return if (left != null && right != null) {
        root.value
    } else if (left == null) {
        right
    } else if (right == null) {
        left
    } else {
        null
    }
}