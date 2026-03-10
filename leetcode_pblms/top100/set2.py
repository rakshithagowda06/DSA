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


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        from collections import Counter

        ransomNoteFreq = Counter(ransomNote)
        magazineFreq = Counter(magazine)

        for char,count in ransomNoteFreq.items():
            if magazineFreq[char] < count:
                return False
        return True 


def longestConsecutive(nums):
    num_set = set(nums)  # O(n) time to create set
    max_length = 0

    for num in num_set:  # O(n) time to iterate through set
        if (num - 1) not in num_set:  # Only start counting if it's the start of a sequence
            current = num
            length = 1
            while (current + 1) in num_set:  # O(k) time where k is length of current sequence
                length += 1
                current += 1
                max_length = max(max_length, length)  # Update max length after counting the sequence
    return max_length


class Solution:
    def solveSudoku(self, board):
        def is_valid(board, r, c, num):
            # check row
            for i in range(9):
                if board[r][i] == num:
                    return False
            
            # check column
            for i in range(9):
                if board[i][c] == num:
                    return False
            
            # check 3x3 box
            start_row = (r // 3) * 3
            start_col = (c // 3) * 3
            
            for i in range(start_row, start_row + 3):
                for j in range(start_col, start_col + 3):
                    if board[i][j] == num:
                        return False
            
            return True

        def backtrack(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for num in map(str, range(1, 10)):
                            if is_valid(board, r, c, num):
                                board[r][c] = num
                                if backtrack(board):
                                    return True
                                board[r][c] = '.'
                        return False
            return True
        
        backtrack(board)

class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r-c) in diag1 or (r+c) in diag2:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)

                backtrack(r+1)

                board[r][c] = "."
                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)

        backtrack(0)
        return res


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = {}
        cols = {}
        boxes = {}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if i not in rows:
                    rows[i] = set()
                if val in rows[i]:
                    return False
                rows[i].add(val)

                if j not in cols:
                    cols[j] = set()
                if val in cols[j]:
                    return False
                cols[j].add(val)

                box_row = i // 3
                box_col = j // 3

                if (box_row,box_col) not in boxes:
                    boxes[(box_row,box_col)] = set()
                if val in boxes[(box_row,box_col)]:
                    return False
                boxes[(box_row,box_col)].add(val)
        return True

                
            
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        n = len(nums)
        for num in counts:
            if counts[num] > (n/2):
                return num
        
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []

        for num in nums:
            result.append(num*num)
        result.sort()
        return result
        