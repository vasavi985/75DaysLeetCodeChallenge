class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def preorder(node):
            if not node:
                return

            result.append(node.val)  # Root
            preorder(node.left)      # Left
            preorder(node.right)     # Right

        preorder(root)
        return result