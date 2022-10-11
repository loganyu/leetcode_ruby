/*
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
*/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func findTarget(root *TreeNode, k int) bool {
    set := make(map[int]int)
    return find(root, k, set)
}

func find(root *TreeNode, k int, set map[int]int) bool {
    if root == nil {
        return false
    }
    if _, ok := set[k - root.Val]; ok {
        return ok
    }
    set[root.Val]++
    return find(root.Left, k, set) || find(root.Right, k, set)
}

