/**
 * 给定一个二叉搜索树, 中序遍历（根节点中间）
 *  [a, b, c]
 *      ->
 *  [b, a, c]
 */

var tree = [3, 5, 1, 6, 2, 0, 8, undefined, undefined, 7, 4]
// 6 5 7 2 4 3 0 1 8

const traverseMiddleOrder = (tree, index = 0) => {
    const leftestIndex = getLeftestIndex(tree, index) // 最左节点index
    if (leftestIndex) {
        console.log(tree[leftestIndex])
        const parentIndex = getParentIndex(leftestIndex) // 父节点
        console.log(tree[parentIndex])
        let rightIndex = getRightIndex(parentIndex) // 右节点
        // 右节点存在子节点
        if (hasChilds(tree, rightIndex)) {
            traverseMiddleOrder(tree, getRightIndex(parentIndex))
        } else {
            console.log(tree[rightIndex])
        }
    } else {
        if (leftestIndex == 0) {
            console.log(tree[0])
        }
    }
}

traverseMiddleOrder(tree)