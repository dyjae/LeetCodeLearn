package com.jae.leetcode.tree;

/**
 * @Description:  https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
 * @Author yj
 * @Date 2019-08-07 09:43
 **/

class LowestCommonAncestorOfABinaryTreeJ {
    public static void main(String[] args) {
        TreeNode root3 = new TreeNode(null, null, 3);
        TreeNode root5 = new TreeNode(null, null, 5);
        TreeNode root1 = new TreeNode(null, null, 1);
        root3.setLeft(root5);
        root3.setRight(root1);

        TreeNode root6 = new TreeNode(null, null, 6);
        TreeNode root2 = new TreeNode(null, null, 2);
        root5.setLeft(root6);
        root5.setRight(root2);

        TreeNode root0 = new TreeNode(null, null, 0);
        TreeNode root8 = new TreeNode(null, null, 8);
        root1.setLeft(root0);
        root1.setRight(root8);

        TreeNode root7 = new TreeNode(null, null, 7);
        TreeNode root4 = new TreeNode(null, null, 4);
        root2.setLeft(root7);
        root2.setRight(root4);

        TreeNode treeNode = lowestCommonAncestor11(root3, root5, root4);
        System.out.println(treeNode.getValue());

    }

    //    Runtime: 6 ms, faster than 60.52% of Java online submissions for Lowest Common Ancestor of a Binary Tree.
    //    Memory Usage: 35.1 MB, less than 5.03% of Java online submissions for Lowest Common Ancestor of a Binary Tree.
    private static TreeNode lowestCommonAncestor11(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null || root.getValue() == p.getValue() || root.getValue() == q.getValue()) return root;
        TreeNode left = lowestCommonAncestor11(root.getLeft(), p, q);
        TreeNode right = lowestCommonAncestor11(root.getRight(), p, q);
        return left == null ? right : right == null ? left : root;
    }


    //和上面的思路一样
    private TreeNode lcs = null;

    public TreeNode lowestCommonAncestor2(TreeNode root, TreeNode p, TreeNode q) {
        searchTree(root, p, q);
        return lcs;
    }

    private boolean searchTree(TreeNode target, TreeNode p, TreeNode q) {
        if (target == null) {
            return false;
        }

        boolean isCurNode = target == p || target == q;
        boolean isLeft = searchTree(target.getLeft(), p, q);
        boolean isRight = searchTree(target.getRight(), p, q);

        if (isCurNode && (isLeft || isRight)) {
            lcs = target;
            return true;
        } else if (isLeft && isRight) {
            lcs = target;
            return true;
        }

        return isCurNode || isLeft || isRight;
    }
}