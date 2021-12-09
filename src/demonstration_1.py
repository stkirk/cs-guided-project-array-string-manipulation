"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3 (value 6)
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
# Plan: we're going to have to iterate through the list and at each element figure out the sum of the indicies to the left and right of it. If those sums match we will return that index, and if we don't find one we will return -1
def pivot_index(nums):
    # loop through the array, could also use enumerate
    for i in range(len(nums)): #--> O(n)

        # is the current item the pivot index?
        # sum stuff on the left (from 0 to the index)
        left_sum = sum(nums[:i]) #--> O(n/2)

        # sum stuff on the right (from index + 1 to the end)
        right_sum = sum(nums[i + 1:]) #--> O(n/2)

        # if sums are equal, return the index
        if left_sum == right_sum:
            return i
    # no match? return -1
    return -1
# This solution is O(n^2) quadratic time complexity

print("O(n^2-->", pivot_index([1,7,3,6,5,6])) # 3
print("O(n^2-->", pivot_index([1,2,3])) # -1
print("O(n^2-->", pivot_index([1])) # 0
print("O(n^2-->", pivot_index([0, 1, 0])) # 1
print("O(n^2-->", pivot_index([])) # -1

#Optimize: If you're going to loop through something, use space and memory to avoid
# O(n) operations within the loop
# try to write a mathematic expression to represent the calculation you're trying to do
    # sum(nums) == left_sum + right_sum + index_value
def pivot_index_opt(nums):
    #initialize the sums
    left_sum = 0 #--> O(1)
    right_sum = sum(nums) #--> O(n)
    
    # loop through the array
    for i in range(len(nums)): #--> O(n)
        # remove current index value from right_sum
        right_sum = right_sum - nums[i] #--> O(1)
        # check sums and return if they match
        if left_sum == right_sum: #--> O(1)
            return i
        # add current index value to left_sum
        # doing this after the check that way we already have the left_sum for the next index to check against right_sum the next time through
        left_sum = left_sum + nums[i] #--> O(1)
    # no match? return -1
    return -1
# This solution is O(n) linear time complexity

print("Optimized-->", pivot_index_opt([1,7,3,6,5,6])) # 3
print("Optimized-->", pivot_index_opt([1,2,3])) # -1
print("Optimized-->", pivot_index_opt([1])) # 0
print("Optimized-->", pivot_index_opt([0, 1, 0])) # 1
print("Optimized-->", pivot_index_opt([])) # -1

def pivot_index_josh(nums):
    # initialize the sums, will be same no matter what list is passed in:
    left_sum = 0
    total_sum = sum(nums)
    # loop through the list:
    for (i, num) in enumerate(nums):
        # each step through the loop subtract the current index value from the right_sum
        # sum(nums) == left_sum + right_sum + index_value --> solve for right_sum:
        right_sum = total_sum - left_sum - num
        # check if sums match
        if right_sum == left_sum:
            # if they match we found the pivot index, return it:
            return i
        # if they don't match, add the index value to left_sum for the next loop through
        left_sum = left_sum + num
    # no pivot index found...
    return -1

print("Josh's Version-->", pivot_index_josh([1,7,3,6,5,6])) # 3
print("Josh's Version-->", pivot_index_josh([1,2,3])) # -1
print("Josh's Version-->", pivot_index_josh([1])) # 0
print("Josh's Version-->", pivot_index_josh([0, 1, 0])) # 1
print("Josh's Version-->", pivot_index_josh([])) # -1
