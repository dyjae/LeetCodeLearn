/**

给定一个二叉树，找出其最大深度。
最小深度是从根节点到最远叶子节点的最长路径上的节点数量。
说明: 叶子节点是指没有子节点的节点。

示例:
    给定二叉树 [3,9,20,null,null,15,7],

        3
       / \
      9  20
        /  \
       15   7
    返回它的最大深度  3.

 */
var root = binaryTreeInit([3, 9, 20, undefined, undefined, 15, 7])

const maxDepth = root => {
    if (!root) return 0
    const leftDepth = maxDepth(root.left)
    const rightDepth = maxDepth(root.right)
    if (leftDepth > rightDepth) {
        return leftDepth + 1
    } else {
        return rightDepth + 1
    }
}

console.log(`最大深度 --> ${maxDepth(root)}`)