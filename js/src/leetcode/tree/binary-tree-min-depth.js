/**

给定一个二叉树，找出其最小深度。
最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
    给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回它的最小深度  2.

 */
// var root = binaryTreeInit([3, 9, 20, undefined, undefined, 15, 7])
var root = binaryTreeInit([1, 2])

const minDepth = root => {
    if (!root) return 0
    const leftDepth = minDepth(root.left)
    const rightDepth = minDepth(root.right)
    if (leftDepth == 0 || rightDepth == 0) {
        return leftDepth + rightDepth + 1
    } else if (leftDepth < rightDepth) {
        return leftDepth + 1
    } else {
        return rightDepth + 1
    }
}

console.log(`最小深度 --> ${minDepth(root)}`)