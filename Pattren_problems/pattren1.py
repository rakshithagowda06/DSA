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
words = []
for word in words:
    "".join(sorted(word))