# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        '''
        def rec(node,depth):
            appennd cur val to res[depth]

        '''

        def rec(curr, depth):
            if not curr:
                return None
            
            if len(res) == depth:
                res.append([])

            res[depth].append(curr.val)

            rec(curr.left,depth+1)
            rec(curr.right,depth+1)

        rec(root,0)

        return res