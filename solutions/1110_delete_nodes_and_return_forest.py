'''
Given the root of a binary tree, each node in the tree has a distinct value.

After deleting all nodes with a value in to_delete, we are left with a forest (a disjoint union of trees).

Return the roots of the trees in the remaining forest.  You may return the result in any order.

 

Example 1:



Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
Output: [[1,2,null,4],[6],[7]]
 

Constraints:

The number of nodes in the given tree is at most 1000.
Each node has a distinct value between 1 and 1000.
to_delete.length <= 1000
to_delete contains distinct values between 1 and 1000.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        def recurse(node, is_root):
            if not node:
                return
            node_deleted = node.val in to_delete
            if is_root and not node_deleted:
                trees.append(node)
            node.left = recurse(node.left, node_deleted)
            node.right = recurse(node.right, node_deleted)
            
            return None if node_deleted else node
            
        trees = []
        to_delete = set(to_delete)
        recurse(root, True)
        
        return trees
        
