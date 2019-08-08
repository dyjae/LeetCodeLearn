package com.jae.leetcode.tree

/**
 * @Description:
 * @Author yj
 * @Date 2019-08-08 18:48
 **/

fun main(args: Array<String>) {
    val root0 = TreeNode(null, null, 0)
//    val root1 = TreeNode(null, null, 1)
    val root2 = TreeNode(null, null, 2)
    val root3 = TreeNode(null, null, 3)
    val root4 = TreeNode(null, null, 4)
    val root5 = TreeNode(null, null, 5)
    val root6 = TreeNode(null, null, 6)
    val root7 = TreeNode(null, null, 7)
    val root8 = TreeNode(null, null, 8)
    val root9 = TreeNode(null, null, 9)

    root6.right = root8
    root6.left = root2

    root2.right = root4
    root2.left = root0

    root4.right = root5
    root4.left = root3

    root8.right = root9
    root8.left = root7

    val lowestCommonAncestor = lowestCommonAncestor(root6, root2, root4)
    println(lowestCommonAncestor?.value)
}

fun lowestCommonAncestor(root: TreeNode?, p: TreeNode, q: TreeNode): TreeNode? {
    root ?: return null
    if (root.value < p.value && root.value < q.value) //大的都在右树
        return lowestCommonAncestor(root.right, p, q)
    if (root.value > p.value && root.value > q.value)//小的都在左树
        return lowestCommonAncestor(root.left, p, q)
    return root
}

