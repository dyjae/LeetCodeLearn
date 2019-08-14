package com.jae.leetcode.dfsbfs

import com.jae.leetcode.tree.TreeNode
import java.util.*

/**
 * @Description: https://leetcode.com/problems/minimum-depth-of-binary-tree
 * @Author yj
 * @Date 2019-08-14 10:02
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
    println(minDepth(treeNode3))
}

//Runtime: 168 ms, faster than 85.71% of Kotlin online submissions for Minimum Depth of Binary Tree.
//Memory Usage: 34.7 MB, less than 100.00% of Kotlin online submissions for Minimum Depth of Binary Tree.
//DFS
fun minDepth(root: TreeNode?): Int {
    root ?: return 0
    val left = minDepth(root.right)
    val right = minDepth(root.left)
    return if (left == 0 || right == 0) {
        right + left + 1
    } else {
        minOf(right, left) + 1
    }
}

//Runtime: 164 ms, faster than 92.06% of Kotlin online submissions for Minimum Depth of Binary Tree.
//Memory Usage: 34.9 MB, less than 100.00% of Kotlin online submissions for Minimum Depth of Binary Tree.
//BFS
//fun minDepth(root: TreeNode?): Int {
//    root ?: return 0
//    val queue: Queue<TreeNode> = LinkedList<TreeNode>()
//    queue.add(root)
//    var index = 1
//    while (queue.isNotEmpty()) {
//        val size = queue.size
//        for (i in 0 until size) {
//            val tree = queue.poll()
//            if (tree.left == null && tree.right == null) return index
//            tree.left?.let { queue.add(it) }
//            tree.right?.let { queue.add(it) }
//        }
//        index++
//    }
//    return 0
//}