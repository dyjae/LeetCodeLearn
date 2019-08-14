package com.jae.leetcode.dfsbfs

import com.jae.leetcode.tree.TreeNode
import java.util.*

/**
 * @Description: https://leetcode.com/problems/maximum-depth-of-binary-tree/
 * @Author yj
 * @Date 2019-08-14 09:47
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
    println(maxDepth(treeNode3))
}

//Runtime: 160 ms, faster than 91.04% of Kotlin online submissions for Maximum Depth of Binary Tree.
//Memory Usage: 34 MB, less than 100.00% of Kotlin online submissions for Maximum Depth of Binary Tree.
//DFS
fun maxDepth(root: TreeNode?): Int {
    root ?: return 0
    return 1 + maxOf(maxDepth(root.left), maxDepth(root.right))
}

//Runtime: 180 ms, faster than 28.36% of Kotlin online submissions for Maximum Depth of Binary Tree.
//Memory Usage: 34.1 MB, less than 100.00% of Kotlin online submissions for Maximum Depth of Binary Tree.
//BFS
//fun maxDepth(root: TreeNode?): Int {
//    root ?: return 0
//    val queue: Queue<TreeNode> = LinkedList<TreeNode>()
//    queue.add(root)
//    var max = 0
//    var index = 1
//    while (queue.isNotEmpty()) {
//        val size = queue.size
//        for (i in 0 until size) {
//            val tree = queue.poll()
//            if (tree.left == null && tree.right == null && index > max) max = index
//            tree.left?.let { queue.add(it) }
//            tree.right?.let { queue.add(it) }
//        }
//        index++
//    }
//    return max
//}

