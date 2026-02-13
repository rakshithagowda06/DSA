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