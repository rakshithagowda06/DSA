def get_max_length(nums):
    if not nums:
        return 0
        
    num_set = set(nums)
    max_length = 0  # Track maximum!
    
    for num in num_set:
        if num - 1 not in num_set:  # Found a start
            length = 1
            current = num  # Use a different variable!
            
            while (current + 1) in num_set:
                length += 1
                current += 1
            
            max_length = max(max_length, length)  # Update max!
    
    return max_length



def maxSubArray(nums):
    
    # keep track of current sum and maximum sum
    current_sum = nums[0]
    max_sum = nums[0]
    
    # start from index 1 (we already used index 0)
    for i in range(1, len(nums)):
        
        # if current sum is negative, start fresh from current number
        # otherwise, add current number to current sum
        current_sum = max(nums[i], current_sum + nums[i])
        
        # update max sum if current sum is greater
        max_sum = max(max_sum, current_sum)
    
    return max_sum



def max_sum(nums):
    max_sum = float('-inf')
    current_sum = 0 
    n = len(nums)

    for i in range(n):
        current_sum = max(num[i],current_sum + nums[i])
        max_sum = max(max_sum,current_sum)
    return max_sum

        

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        n = len(t)
        i = 0

        for j in range(n):
            if i < len(s) and s[i] == t[j]:
                i+=1
        return i == len(s)
        

def longestCommonPrefix(strs):
    # Edge case : empty string

    if not strs:
        return ""
    
    prefix = ""
    
    # Check each character posiiton in first string
    for i in range(len(strs[0])):
        char1 = str[0][i]  # Current character from first string

        # Check if All other strings have same char at position i
        for string in strs[1:]:  # Check from second string onwards
            # If string is too short OR Character doesn't match
            if i >= len(string) or string[i] != char1:
                return prefix
            
        # All strings matched this character

        prefix += char1
    
    return prefix


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_profit = 0

        for i in prices:
            min_price = min(i,min_price)
            profit = i - min_price
            max_profit = max(profit,max_profit)
        return max_profit
        
class Solution(object):
    def summaryRanges(self, nums):
        if not nums:
            return []
        
        result = []
        start = nums[0]   # start of current range
        
        for i in range(1, len(nums)):
            # if sequence breaks
            if nums[i] != nums[i - 1] + 1:
                # single number range
                if start == nums[i - 1]:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(nums[i - 1]))
                
                # start new range
                start = nums[i]
        
        # handle last range after loop ends
        if start == nums[-1]:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(nums[-1]))
        
        return result


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        
        for current in intervals[1:]:
            prev = merged[-1]
            
            # If overlapping
            if current[0] <= prev[1]:
                prev[1] = max(prev[1], current[1])
            else:
                merged.append(current)
        
        return merged