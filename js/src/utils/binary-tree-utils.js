// 获取父节点index（根节点为自身）
const getParentIndex = index => index == 0 ? 0 : (index - (Math.floor(index / 2) + 1))

// 获取左节点index（无则返回false）
const getLeftIndex = index => 2 * index + 1

// 获取最左节点index
const getLeftestIndex = (tree, index = 0) => {
    const left = tree[getLeftIndex(index)]
    if (left == 0 || left) {
        return getLeftestIndex(tree, getLeftIndex(index))
    } else {
        return index
    }
}

// 获取右节点index（无则返回false）
const getRightIndex = index => 2 * index + 2

// 是否有子节点
const hasChilds = (tree, index = 0) => {
    const left = tree[getLeftIndex(index)]
    const right = tree[getRightIndex(index)]
    if ((left == 0 || left) || (right == 0 || right)) {
        return true
    } else {
        return false
    }
}

// 获取层级深度
const getDeep = (index, deep = 0) => {
    if ((2 ** deep < index) && (index <= 2 ** (deep + 1))) {
        return deep
    } else {
        getDeep(index, deep + 1)
    }
}