/**
 * 二叉树节点
 */
class TreeNode {
    constructor(val) {
        this.val = val
        this.left = this.right = undefined
    }

    // 先序遍历
    traverseAnteriorOrder() {
        console.log(this.val)
        this.left && this.left.traverseAnteriorOrder()
        this.right && this.right.traverseAnteriorOrder()
    }

    // 中序遍历
    traverseMiddleOrder() {
        this.left && this.left.traverseMiddleOrder()
        console.log(this.val)
        this.right && this.right.traverseMiddleOrder()
    }

    // 后序遍历
    traversePosteriorOrder() {
        this.left && this.left.traversePosteriorOrder()
        this.right && this.right.traversePosteriorOrder()
        console.log(this.val)
    }

    // 层次遍历
    traverseLevelOrder(result = [], level = 0) {
        result[level] ? result[level].push(this.val) : result.push([this.val])
        this.left && this.left.traverseLevelOrder(result, level + 1)
        this.right && this.right.traverseLevelOrder(result, level + 1)
        return result
    }
}

/**
 * 二叉树初始化
 * @param [*]       tree
 * @param number    当前根节点在数组中的下标
 */
const binaryTreeInit = (tree, index = 0) => {
    const val = tree[index]
    if (val === 0 || val) {
        const root = new TreeNode(val)
        const leftVal = tree[getLeftIndex(index)]
        if (leftVal === 0 || leftVal) {
            root.left = binaryTreeInit(tree, getLeftIndex(index)) || undefined
        }
        const rightVal = tree[getRightIndex(index)]
        if (rightVal === 0 || rightVal) {
            root.right = binaryTreeInit(tree, getRightIndex(index)) || undefined
        }
        return root
    } else {
        return
    }
}