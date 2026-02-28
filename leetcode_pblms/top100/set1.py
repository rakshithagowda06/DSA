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
        