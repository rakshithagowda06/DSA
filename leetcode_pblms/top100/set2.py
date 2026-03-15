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

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
            

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            fixed = nums[i]

            while left < right:
                current_sum = nums[left] + nums[right]

                if current_sum > -fixed:
                    right -= 1
                elif current_sum < -fixed:
                    left +=1
                else:
                    result.append([fixed,nums[left],nums[right]])

                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -= 1
        return result

                    


class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for op in operations:
            if op!='C' and op!='D' and op!='+':
                stack.append(int(op))
            elif op=='C':
                stack.pop()
            elif op=='D':
                stack.append(stack[-1]*2)
            elif op=='+':
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
        
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []

        for token in tokens:
            if token not in ['+','-','/','*']:
               stack.append(int(token))
            elif token=='+':
                b=stack.pop()
                a=stack.pop()
                stack.append(a+b)
            elif token=='-':
                b=stack.pop()
                a=stack.pop()
                stack.append(a-b)
            elif token=='*':
                b=stack.pop()
                a=stack.pop()
                stack.append(a*b)
            elif token=='/':
                b=stack.pop()
                a=stack.pop()
                stack.append(int(float(a)/b))
        return stack[-1]    
            
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        n = len(temperatures)
        answers = [0] * n
        for i in range(n):
            current_sum = temperatures[i]
            while stack and current_sum > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answers[prev_index] = i - prev_index
            stack.append(i)
        return answers


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head

        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        curr = head
        prev = dummy

        while curr:
            if curr.next and curr.val == curr.next.val:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

def get_sum(a,b):
    return a+b

def get_diff(a,b):
    return a-b

def get_cube(a):
    return (a*a*a)

def get_square(a):
    return a*a

