# solution with O(n)**2


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

s = find_a_target1(nums,target)
print(s)
