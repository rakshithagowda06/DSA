""" Tree problems"""

# maxdepth of a tree 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if not root:
        return 0
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    return 1+max(left_depth,right_depth)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(10)
print(maxDepth(root))

# Invert a tree


def invertTree(root):
    if not root:
        return None
    
    # Swap using tuple unpacking (more Pythonic!)
    root.left, root.right = root.right, root.left
    
    # Recursively invert
    invertTree(root.left)
    invertTree(root.right)
    
    return root



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)



# Grapgh Problem

from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def bfs(r,c):
            queue = deque()
            queue.append((r,c))
            grid[r][c] = '0'
            while queue:
                row ,col = queue.popleft()
                directions = [(1,0),(-1,0),(0,1),(0,-1)]
                for dr,dc in directions:
                    new_row = row + dr
                    new_col = col + dc
                    if (new_row >= 0 and new_row < rows 
                        and new_col >=0 and new_col < cols
                        and grid[new_row][new_col] == '1'):

                        queue.append((new_row,new_col))
                        grid[new_row][new_col] = '0'

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r,c)
        return islands            
        

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i] = max(nums[i]+dp[i-2],dp[i-1])
        return dp[n-1]

def firstBadversion(n):
    left = 1
    right = n

    while left <= right:
        mid = (left+right)//2

        if isBadVersion(mid):
            right = mid - 1
        else:
            left = mid + 1
    return left


from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        elements = set()
        for number in arr:
            if 2 * number in elements or (number % 2 == 0 and number // 2 in elements):
                return True
            elements.add(number)
        return False
    


from typing import List


class Solution:
    def duplicateZeros(self, array: List[int]) -> None:
        removals, k, i = 0, len(array) - 1, 0
        while i < len(array) - removals:
            if array[i] is 0:
                if i == len(array) - removals - 1:
                    array[k] = 0
                    k -= 1
                removals += 1
            i += 1

        i = len(array) - removals - 1
        while i >= 0:
            if array[i] is 0:
                array[k], array[k - 1] = 0, 0
                k -= 1
            else:
                array[k] = array[i]
            k -= 1
            i -= 1
