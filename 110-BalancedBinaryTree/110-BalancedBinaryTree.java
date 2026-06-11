// Last updated: 6/12/2026, 12:45:06 AM

class Solution {
    public boolean isBalanced(TreeNode root) {
        return check(root) != -1;
        }
        private int check(TreeNode root){
            if (root == null) return 0;
            int left = check(root.left);
            int right = check(root.right);
            if(left == -1 || right == -1|| Math.abs(left - right)>1) return -1;
            return 1+Math.max(left, right);
        }
}