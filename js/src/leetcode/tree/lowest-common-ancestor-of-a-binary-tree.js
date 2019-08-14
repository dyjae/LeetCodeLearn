/**
 * 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
 */

var tree = [3, 5, 1, 6, 2, 0, 8, undefined, undefined, 7, 4]

const lowestCommonAncestor = (tree, p, q) => {
    let pIndex = 0 // p节点下标
    let qIndex = 0 // q节点下标
    let common = 0
    pIndex = tree.findIndex(v => v == p)
    qIndex = tree.findIndex(v => v == q)

    let pParents = [pIndex] // p节点父级index数组
    let qParents = [qIndex] // q节点父级index数组
    const getParents = (index, parents) => {
        while (0 != (index = getParentIndex(index))) {
            parents.push(index)
        }
        parents.push(0) // root
    }
    getParents(pIndex, pParents)
    getParents(qIndex, qParents)

    console.log(pParents, qParents)

    let long, short
    if (pParents.length >= qParents.length) {
        long = pParents
        short = qParents
    } else {
        long = qParents
        short = pParents
    }
    for (let i = 0; i < long.length; i++) {
        if (short.indexOf(long[i]) > -1) {
            common = long[i]
            break
        }
    }

    return tree[common]
}

console.log(lowestCommonAncestor(tree, 5, 1))

console.log(lowestCommonAncestor(tree, 5, 4))