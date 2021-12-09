"""
You are given a non-empty array that represents the digits of a non-negative integer.

Write a function that increments the number by 1.

The digits are stored so that the digit representing the most significant place value is at the beginning of the array. Each element in the array only contains a single digit.

You will not receive a leading 0 in your input array (except for the number 0 itself).

Example 1:

Input: [1,3,2]
Output: [1,3,3]
Explanation: The input array represents the integer 132. 132 + 1 = 133.

Example 2:

Input: [3,2,1,9]
Output: [3,2,2,0]
Explanation: The input array represents the integer 3219. 3219 + 1 = 3220.

Example 3:

Input: [9,9,9]
Output: [1,0,0,0]
Explanation: The input array represents the integer 999. 999 + 1 = 1000.
"""
def plus_one(digits):
    # make a copy of digits
    digits = digits[:] #--> O(n)
    # loop from the end of the array
    # range(start at the end of the array, go to the upper bound of -1, get there by moving -1 index at a time)
    for i in range((len(digits) - 1), -1, -1): #--> O(n)
        # add one to the current digit
        digits[i] += 1
        if digits[i] < 10:
            return digits
        else:
        # if the sum is 10, set current digit to zero and repeat
            digits[i] = 0

    return [1] + digits #--> O(n)
# Time complexity O(n)


print("O(n) operation-->", plus_one([1,3,2])) # [1, 3, 3]
print("O(n) operation-->", plus_one([3,2,1,9])) # [3, 2, 2, 0]
print("O(n) operation-->", plus_one([9,9,9])) # [1, 0, 0, 0]

def plus_one_hacked(digits):
    for (i, num) in enumerate(digits):
        digits[i] = str(num)
    str_digits = ''.join(digits)
    plus_one = str(int(str_digits) + 1)
    solution = list(plus_one)
    return solution


print("hacked version-->", plus_one_hacked([1,3,2]))
print("hacked version-->", plus_one_hacked([3,2,1,9]))
print("hacked version-->", plus_one_hacked([9,9,9]))

# In-Place version, mutates original, saves space
original_digits = [3, 2, 1, 9]
original_digits2 = [9, 9, 9]

def plus_one_in_place(digits):
    for backwards_index in range(len(digits)):
        # start at the back, and subtract one more index than the previous iteration
        i = len(digits) - 1 - backwards_index
        # do our operations in relation to i
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    # if the first index (last iteration) is a 9, we haven't returned out in the loop and land here:
    [1] + digits

plus_one_in_place(original_digits)
plus_one_in_place(original_digits2)
print("in_place version-->", original_digits)
print("in_place version-->", original_digits2)
