class Solution(object):
    def spiralOrder(self,matrix):
        if not matrix:
            return []

        res = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while left <= right and top <= bottom:

            # left -> right
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # top -> bottom
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                # right -> left
                for col in range(right, left - 1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1

            if left <= right:
                # bottom -> top
                for row in range(bottom, top - 1, -1):
                    res.append(matrix[row][left])
                left += 1

        return res



class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        # Step 1: Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()


class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0

        for i in stones:
            if i in jewels:
                count += 1
        return count
        

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False