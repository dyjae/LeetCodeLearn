package com.jae.leetcode.tree

/**
 * @Description: 二叉树的前序，中序，后序遍历
 * @Author yj
 * @Date 2019-08-09 09:49
 **/
fun main(args: Array<String>) {
    val root0 = TreeNode(null, null, 0)
    val root1 = TreeNode(null, null, 1)
    val root2 = TreeNode(null, null, 2)
    val root3 = TreeNode(null, null, 3)
    val root4 = TreeNode(null, null, 4)
    val root5 = TreeNode(null, null, 5)
    val root6 = TreeNode(null, null, 6)

    root0.left = root1
    root0.right = root2

    root1.left = root3
    root1.right = root4

    root2.left = root5
    root2.right = root6

//    preOrder(root0).forEach(::println)
//    inOrder(root0).forEach(::println)
    postOrder(root0).forEach(::println)
}

//前序
fun preOrder(treeNode: TreeNode): List<Int> {
    val rsList = emptyList<Int>().toMutableList()
    rsList.add(treeNode.value)
    treeNode.left?.let { rsList.addAll(preOrder(it)) }
    treeNode.right?.let { rsList.addAll(preOrder(it)) }
    return rsList
}

//中序
fun inOrder(treeNode: TreeNode): List<Int> {
    val rsList = emptyList<Int>().toMutableList()
    treeNode.left?.let { rsList.addAll(inOrder(it)) }
    rsList.add(treeNode.value)
    treeNode.right?.let { rsList.addAll(inOrder(it)) }
    return rsList
}

//后序
fun postOrder(treeNode: TreeNode): List<Int> {
    val rsList = emptyList<Int>().toMutableList()
    treeNode.left?.let { rsList.addAll(postOrder(it)) }
    treeNode.right?.let { rsList.addAll(postOrder(it)) }
    rsList.add(treeNode.value)
    return rsList
}