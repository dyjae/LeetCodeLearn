package com.jae.leetcode.tree


/**
 * @Description:https://leetcode.com/problems/validate-binary-search-tree/
 * @Author yj
 * @Date 2019-07-31 09:53
 **/
fun main(args: Array<String>) {
//    val top = TreeNode(value = 2)
//    val second1 = TreeNode(value = 1)
//    val second2 = TreeNode(value = 3)
//    top.right = second2
//    top.left = second1
//    println(isValidBST(top))

    val top = TreeNode(value = 5)
    val s1 = TreeNode(value = 1)
    val s2 = TreeNode(value = 4)
    val t1 = TreeNode(value = 3)
    val t2 = TreeNode(value = 6)
    s2.left = t1
    s2.right = t2
    top.right = s2
    top.left = s1
    println(isValidBST(top))
}



//Runtime: 180 ms, faster than 82.43% of Kotlin online submissions for Validate Binary Search Tree.
//Memory Usage: 37.5 MB, less than 100.00% of Kotlin online submissions for Validate Binary Search Tree.
fun isValidBST(root: TreeNode): Boolean {
    return validate(root.left, null, root.value) && validate(root.right, root.value, null)
}

fun validate(root: TreeNode?, min: Int?, max: Int?): Boolean {
    root ?: return true
    if (min != null && root.value <= min) return false
    if (max != null && root.value >= max) return false
    return validate(root.left, min, root.value) && validate(root.right, root.value, max)
}

data class TreeNode(var left: TreeNode? = null, var right: TreeNode? = null, val value: Int)
