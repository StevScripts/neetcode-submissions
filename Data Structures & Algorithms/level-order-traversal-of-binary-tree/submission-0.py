# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        queue = []

        curr = 1
        """
        if not root:
            return []
        queue = deque()
        queue.appendleft((root,0))

        toRet = []
        templist = []

        prevLev = 0

        while queue:
            curr,level = queue.pop()

            if prevLev != level:
                toRet.append(templist)
                templist = []
                prevLev = level

            if curr.left:
                queue.appendleft((curr.left,level+1))
            if curr.right:
                queue.appendleft((curr.right,level+1))   

            templist.append(curr.val)
        
        if templist:
            toRet.append(templist)

        return toRet
        

                 