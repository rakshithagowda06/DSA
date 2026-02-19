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


