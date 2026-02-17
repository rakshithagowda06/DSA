# Dictionary and set pattrens

""" Count ocuurence of elements"""
# Frequency counter


def freq_counter(nums):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) + 1
    return freq