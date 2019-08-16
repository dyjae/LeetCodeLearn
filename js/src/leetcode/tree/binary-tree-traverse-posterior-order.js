/**
 * 给定一个二叉搜索树, 后序遍历（根节点最后）
 *  [a, b, c]
 *      ->
 *  [b, c, a]
 */

var tree = [3, 5, 1, 6, 2, 0, 8, undefined, undefined, 7, 4]
// 6 7 4 2 5 0 8 1 3

var root = binaryTreeInit(tree) // 二叉树
root.traversePosteriorOrder()