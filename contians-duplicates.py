# Your function should return true if any value appears at least twice in the array,
# and it should return false if every element is distinct.
nums = [0]


# class Solution:
# def containsDuplicate(self, nums):
# initialize a dict to hold all items
# iterate through dict
# nums_copy.sort(self.nums)
duplicates = []
nums_2_set = set(nums)
if nums and not duplicates:
    for number in nums:
        if number in nums_2_set:
            duplicates.append(number)
    print(True)
else:
    print(False)
    # containsDuplicate()
    # # Binary search is O(log n)
    # from bisect import bisect_left

    # def binary_search(a, x):
    #     'Locate the leftmost value exactly equal to x'
    #     i = bisect_left(a, x)
    #     if i != len(a) and a[i] == x:
    #         return i
    #     return None

    # # Running binary search n times is O(n log n)
    # duplicates = []
    # while not duplicates:
    #     for number in self.nums:
    #         if binary_search(nums_copy, number) is not None:
    #             duplicates.append(number)
