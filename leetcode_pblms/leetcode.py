# solution with O(n)**2
from jedi.plugins.django import mapping


def find_a_target(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == target:
                return [i,j]
nums = [2,7,11,15]
target = 9

# s = find_a_target(nums,target)
# print(s)


# solution with O(n)

def find_a_target1(arr,target):
    seen = {}
    for idx,num in enumerate(arr):
        ele = target-num
        if ele in seen:
            return [seen[ele],idx]
        seen[num] = idx

# s = find_a_target1(nums,target)
# print(s)

def is_valid(s):
     mapping = {")":"(","]":"[","}":"{"}
     stack = []
     for char in s:
         if char in mapping:
             if not stack:
                 return False
             top = stack.pop()
             if mapping[char] != top:
                 return False
         else:
             stack.append(char)
     return  not stack

s = "](()))"
print(is_valid(s))

def longest_substring(s):
    s1=""
    for i in s:
        if i not in s1:
            s1+=i
        return s1

def print_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left +=1
        
        seen.add(s[right])
        max_length = max(max_length,right-left+1)
    return max_length

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in lookup:
                return [lookup[compliment],i]
            lookup[nums[i]] = i
        

def is_anagram(s1, s2):
    # Quick check: different lengths can't be anagrams
    if len(s1) != len(s2):
        return False
    
    s1_freq = {}
    s2_freq = {}
    
    for char in s1:
        s1_freq[char] = s1_freq.get(char, 0) + 1
    
    for char in s2:
        s2_freq[char] = s2_freq.get(char, 0) + 1
    
    return s1_freq == s2_freq



class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        close = nums[0]
        for num in nums:
            if abs(num) < abs(close):
                close = num
            elif abs(close) == abs(num) and num > close:
                close = num
        return close
    

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        nums = []
        i = 0

        while i < len(word1) and i < len(word2):
            nums.append(word1[i])
            nums.append(word2[i])
            i+=1
        nums.append(word1[i:])
        nums.append(word2[i:])
        return "".join(nums)


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
        total = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman[s[i]] < roman[s[i+1]]:
                total -= roman[s[i]]
            else:
                total += roman[s[i]]
        return total

        
# Top K Frequent Elements

def get_top_k_elements(nums,k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num,0) + 1
    get_sorted_list = sorted(freq.items(),lambda x:x[1], reverse=True)
    result = []

    for i in range(k):
        result.append(get_sorted_list[i][0])
    return result

# get longestConsecutive number
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num-1) not in num_set:
                start=num
                length = 1
                while (start+1) in num_set:
                    length +=1
                    start +=1
                longest = max(length,longest)
        return longest
    
#Product of Array Except Self


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1]*n
        right = [1]*n
        result = [1] * n

        left_product = 1
        
        
        for i in range(n):
            left[i] = left_product
            left_product *= nums[i]

        right_product = 1

        for j in range(n-1,-1,-1):
            right[j] = right_product
            right_product *= nums[j]

        for k in range(n):
            result[k] = left[k] * right[k]
        return result


         
# Check palindrome or not

def check_palindrome(s):
    cleaned = ""
    for char in s:
        if char.isalnum():
            cleaned += char.lower()
    left = 0
    right = len(cleaned)-1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left +=1
        right -=1

    return True

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1

        while left<right:
            curr_sum = numbers[left] + numbers[right]
            if curr_sum == target:
                return [left+1,right+1]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
                

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water =0

        while left<right:
            width = right - left
            height1 = min(height[left],height[right])
            area = height1 * width
            max_water = max(max_water,area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
    
 # check its a valid parantesis

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mapping = {'}' :'{',']':'[',')':'('}
        stack = []
        for i in s:
            # check its a closed brace
            if i in mapping:
                # check if stack is empty or top doesn't match 
                if not stack or stack[-1] != mapping[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)
        return len(stack)==0


class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            curr_min = self.min_stack[-1]
            self.min_stack.append(min(val,curr_min))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()