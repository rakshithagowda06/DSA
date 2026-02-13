s = "abcd"
left = 0
right = 0
for right in range(len(s)):
    print(s[left:right+1])

def contains_duplicate(num):
    return len(num) != len(set(num))



nums = [1,2,3,4,1]
print(contains_duplicate(nums))


def first_duplicate(s):
    seen = set()
    for i in s:
        if i in seen:
             return i
        seen.add(i)
    return None