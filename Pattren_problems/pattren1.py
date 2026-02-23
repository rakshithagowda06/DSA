# Dictionary and set pattrens

""" Count ocuurence of elements"""
# Pattern 1: Frequency Counter

def freq_counter(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    return freq

# Pattern 2: Seen/Visited Tracker

"""Track what you've already processed"""
items = []
seen = set()
for item in items:
    if item in seen:
        continue
    seen.add(item)

# Pattern 3: Two Sum Pattern

"""Use complement lookup"""
lookup = {}
nums = []
target = 0
for i in range(len(nums)):
    compliment = target - nums[i]
    if compliment in lookup:
        print([lookup[i],i])
    lookup[nums[i]] = i

# Pattern 4: Finding the signature of word
"""use a word to join"""
words = []
for word in words:
    "".join(sorted(word))

# Pattern 5: Two pointers
# Opposite Direction (Left & Right)
arr = []
left = arr[0]
right = len(arr)-1
while left<right:
    # Do somehting with arr[left] and arr[right]
    # Move pointers based on condiition
    left += 1
    right -= 1

# Use cases: Palindrome check, Two Sum in sorted array, Container with most water

# Pattern 6: Same Direction (Slow & Fast)

slow = 0
right = 0

for fast in range(len(arr)):
    # Do something
    # Move slow only when condiiton is set
    if "condition":
        slow +=1

# Use cases: Remove duplicates, Move zeros

# Pattern 3: Sliding Window

left = 0

for right in range(len(arr)):
    # Expand window by adding arr[right]
    while "window_condition_violated":
        # Shrink window from left
        left +=1

# Stack(LIFO = Last in First out)

stack = []
stack.append(5)
stack.append(10)
stack.append(15)
#stack = [5,10,15]
top = stack.pop()
# returns 15
top = stack[-1] # wil get top without removing

# check if stack is empty
if stack:
    print("stack is not empty")
# to get a size

size = len(stack)

# CONCEPT: Queue (FIFO - First In, First Out)
# Think of a line at a store - first person in line is served first.

from collections import deque

queue = deque()

queue.append(5)
queue.append(10)
queue.append(15)

# queue = [5,10,15]
front = queue.popleft()
# returns 5

# Peek front
front = queue[0]  # Returns 10


# Check if empty
if queue:
    print("Not empty")

# Size
size = len(queue)


""" Key points to remember while solving the question"""
# if it is a close brace pop from stack
# if it is open brace add it stack



"""key points to remember while solving the temprature problem"""
# Instead of looking forward tempreature for each day,we use a stack to remember past days that are still waiting for warmer day


""" Leetcode questions to understand """
# Definig the Node

class ListNode:
    def __init__(self,val,next=None):
        val = self.val
        next = self.next

# Creating 1 -> 2 -> 3 -> None

node3 = ListNode(3)
node2 = ListNode(2,node3)
node1 = ListNode(1,node2)
head = node1

# Traversing

curr = head

while curr:
    print(curr.val)
    curr = curr.next

# Common Patterns 

# Pattern 1 : Two pointers(Slow and Fast)

slow = head
fast = head

while fast and fast.next:
    slow = slow.next  # Move one step
    fast = fast.next.next # Move 2 steps

# Use acses : Find middle,detect cycle


# Pattern 2 : Dummy Node
dummy =ListNode(0)
dummy.next = head

# Work with dummy to avoid edge case
# Use case : When you might modify head

# Pattern 3 : Reversing

prev = None
current = head

while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
    

""" A tree where each node has atmost two children(left and right)"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left    # Left child
        self.right = right  # Right child


## 💡 **Common Tree Traversals:**

### **1. Inorder (Left → Root → Right)**

   #    1
   #   / \
   #   2   3
     
Inorder: [2, 1, 3]

### **2. Preorder (Root → Left → Right)**
Preorder: [1, 2, 3]

### **3. Postorder (Left → Right → Root)**
Postorder: [2, 3, 1]

### **4. Level Order (BFS - layer by layer)**
LevelOrder: [1, 2, 3]


    