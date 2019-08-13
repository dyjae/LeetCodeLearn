package com.jae.leetcode.dfsbfs

import com.jae.leetcode.tree.TreeNode
import java.util.*

/**
 * @Description:https://leetcode.com/problems/binary-tree-level-order-traversal/
 * @Author yj
 * @Date 2019-08-13 09:44
 **/

fun main(args: Array<String>) {
    val treeNode3 = TreeNode(value = 3)
    val treeNode9 = TreeNode(value = 9)
    val treeNode20 = TreeNode(value = 20)
    val treeNode15 = TreeNode(value = 15)
    val treeNode7 = TreeNode(value = 7)
    treeNode3.left = treeNode9
    treeNode3.right = treeNode20
    treeNode20.left = treeNode15
    treeNode20.right = treeNode7

    levelOrder(treeNode3).forEach { list ->
        list.forEach(::print)
        println()
    }
}

//BFS
//Runtime: 172 ms, faster than 95.00% of Kotlin online submissions for Binary Tree Level Order Traversal.
//Memory Usage: 36 MB, less than 100.00% of Kotlin online submissions for Binary Tree Level Order Traversal.
fun levelOrder(root: TreeNode?): List<List<Int>> {
    val rs = emptyList<List<Int>>().toMutableList()
    root ?: return rs
    val queue: Queue<TreeNode> = LinkedList<TreeNode>()
    queue.add(root)
    rs.add(arrayListOf(root.value))
    while (queue.isNotEmpty()) {
        val levelList = emptyList<Int>().toMutableList()
        for (i in 0 until queue.size) {
            val tree = queue.remove()
            tree.left?.also {
                levelList.add(it.value)
                queue.add(it)
            }
            tree.right?.also {
                levelList.add(it.value)
                queue.add(it)
            }
        }
        if (levelList.isNotEmpty()) rs.add(levelList)
    }
    return rs
}


//DFS
//Runtime: 176 ms, faster than 92.00% of Kotlin online submissions for Binary Tree Level Order Traversal.
//Memory Usage: 33.9 MB, less than 100.00% of Kotlin online submissions for Binary Tree Level Order Traversal.
//fun levelOrder(root: TreeNode?): List<List<Int>> {
//    val rs = ArrayList<ArrayList<Int>>()
//    dfsOrder(root, rs, 0)
//    return rs
//}
//
//fun dfsOrder(root: TreeNode?, rs: ArrayList<ArrayList<Int>>, level: Int) {
//    root?.also {
//        val list = if (level >= rs.size) {
//            val inList = ArrayList<Int>()
//            rs.add(inList)
//            inList
//        } else {
//            rs[level]
//        }
//        list.add(it.value)
//        rs[level] = list
//        root.left?.let { left -> dfsOrder(left, rs, level + 1) }
//        root.right?.let { right -> dfsOrder(right, rs, level + 1) }
//    } ?: return
//}
