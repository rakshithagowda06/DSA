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


def count_unique(s):
    seen = set()

    for ch in s:
        if ch not in seen:
            seen.add(ch)
    return len(seen)


def print_duplicate(s):
    seen = set()
    for ch in s:
        if ch in seen:
            print(f"duplicate found at {ch}")

        seen.add(ch)



def print_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            s[left].remove()
            left +=1
        
        seen.add(s[right])
        max_length = max(max_length,right-left+1)
    return max_length



def count_unique(s):
    seen = set()
    duplicate = set()
    for ch in s:
        if ch in seen:
            duplicate.add(ch)
        seen.add(ch)
    return len(seen)
        


from collections import Counter

def first_unique(s):
    Count = Counter(s)
    for ch in s:
        if Count[ch] == 1:
            return ch
    return None
    