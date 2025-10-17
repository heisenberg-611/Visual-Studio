class TreeNode {
    int value;
    TreeNode left;
    TreeNode right;
    
    public TreeNode(int val) {
        this.value = val;
        this.left = this.right = null;
    }
}

public class Solution {
    public static String findSequence(TreeNode root, int[] arr) {
        return check(root, arr, 0);
    }

    private static String check(TreeNode node, int[] arr, int index) {
        // Base case: if node is null, return "no"
        if (node == null) {
            return "no";
        }
        
        // If current node's value matches the current index in the array
        if (index < arr.length && node.value == arr[index]) {
            // Check if we've reached the end of the array (full match)
            if (index == arr.length - 1) {
                return "yes";
            }
            
            // Check left and right children
            String leftResult = check(node.left, arr, index + 1);
            String rightResult = check(node.right, arr, index + 1);
            
            // If either child returns "yes", we found a full match
            if (leftResult.equals("yes") || rightResult.equals("yes")) {
                return "yes";
            }
            
            // Check if we've reached the middle of the array (half way)
            int mid = arr.length / 2;
            if (index == mid) {
                return "trapped";
            }
            
            return "no";
        } else {
            return "no";
        }
    }

    public static void main(String[] args) {
        // Example tree: (0) -> (1, 1) -> (1, 0)
        TreeNode root = new TreeNode(0);
        root.left = new TreeNode(1);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(1);
        root.left.right = new TreeNode(0);
        
        int[] sequence = {0, 1, 0};
        System.out.println(findSequence(root, sequence)); // Should output "yes"
    }
}
