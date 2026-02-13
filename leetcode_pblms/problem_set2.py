s = "abcd"
left = 0
right = 0
for right in range(len(s)):
    print(s[left:right+1])

def contains_duplicate(num):
    return len(num) != len(set(num))
