/**
 * 给定一个二叉搜索树, 先序遍历（根节点最先）
 *  [a, b, c]
 *      ->
 *  [a, b, c]
 */

var tree = [3, 5, 1, 6, 2, 0, 8, undefined, undefined, 7, 4]
// 3 5 6 2 7 4 1 0 8

const traverseAnteriorOrder = (tree, index = 0) => {
    const cur = tree[index]
    console.log(cur)
    const left = getLeftIndex(index)
    const right = getRightIndex(index)
    if (tree[left] == 0 || tree[left]) {
        traverseAnteriorOrder(tree, left)
    }
    if (tree[right] == 0 || tree[right]) {
        traverseAnteriorOrder(tree, right)
    }
}
// traverseAnteriorOrder(tree)

var root = binaryTreeInit(tree) // 二叉树
root.traverseAnteriorOrder()