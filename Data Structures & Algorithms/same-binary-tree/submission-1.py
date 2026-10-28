# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        '''
        -Check if the item exists first, and also check value

        -DFS
        -Base case, if if both p and q None return True
        -Main Case, Check if p or q is not equal or the values of both are not equal ret false
        -Check the left and Right subtrees of each item

        return dfs()


        '''

        def dfs(newP,newQ):
            if newP is None and newQ is None:
                return True
            
            if newP is None or newQ is None or newP.val != newQ.val:
                return False

            left = dfs(newP.left,newQ.left)
            right = dfs(newP.right,newQ.right)

            return left and right
            
        return dfs(p,q)
        


        
        