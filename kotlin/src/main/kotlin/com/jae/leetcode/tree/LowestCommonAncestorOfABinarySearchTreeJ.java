package com.jae.leetcode.tree;

/**
 * @Description:
 * @Author yj
 * @Date 2019-08-08 18:48
 **/
class LowestCommonAncestorOfABinarySearchTreeJ {
    public static void main(String[] args) {
        TreeNode root0 = new TreeNode(null, null, 0);
//        TreeNode root1 = new TreeNode(null, null, 1);
        TreeNode root2 = new TreeNode(null, null, 2);
        TreeNode root3 = new TreeNode(null, null, 3);
        TreeNode root4 = new TreeNode(null, null, 4);
        TreeNode root5 = new TreeNode(null, null, 5);
        TreeNode root6 = new TreeNode(null, null, 6);
        TreeNode root7 = new TreeNode(null, null, 7);
        TreeNode root8 = new TreeNode(null, null, 8);
        TreeNode root9 = new TreeNode(null, null, 9);
        root6.setLeft(root2);
        root6.setRight(root8);

        root2.setLeft(root0);
        root2.setRight(root4);

        root4.setLeft(root3);
        root4.setRight(root5);

        root8.setLeft(root7);
        root8.setRight(root9);

        TreeNode treeNode = lowestCommonAncestor(root6, root2, root8);
        System.out.println(treeNode.getValue());
    }

    //11 ms
    private static TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (root == null) return null;
        if (root.getValue() < p.getValue() && root.getValue() < q.getValue()) //大的都在右树
            return lowestCommonAncestor(root.getRight(), p, q);
        if (root.getValue() > p.getValue() && root.getValue() > q.getValue())//小的都在左树
            return lowestCommonAncestor(root.getLeft(), p, q);
        return root;
    }


    //4ms
    public TreeNode lowestCommonAncestor2(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode min = p.getValue() <= q.getValue() ? p : q;
        TreeNode max = p.getValue() <= q.getValue() ? q : p;
        return search(root, min, max);
    }

    public TreeNode search(TreeNode node, TreeNode p, TreeNode q) {
        if (p.getValue() <= node.getValue() && node.getValue() <= q.getValue()) return node;
        if (p.getValue() > node.getValue()) return search(node.getRight(), p, q);
        return search(node.getLeft(), p, q);
    }
}

