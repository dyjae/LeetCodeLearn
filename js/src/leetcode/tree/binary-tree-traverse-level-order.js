/**
 * 二叉树的层次遍历
 *  给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
 * 

        例如:
        给定二叉树: [3,9,20,null,null,15,7],

            3
           / \
          9  20
            /  \
           15   7
        返回其层次遍历结果：

        [
            [3],
            [9,20],
            [15,7]
        ]

 * 
 */

var tree = [3, 9, 20, undefined, undefined, 15, 7]

var root = binaryTreeInit(tree) // 二叉树
console.log(root.traverseLevelOrder())