arr = [1, 2, 3, 4, 5]

# Access array:
print(arr[3])
# O(1) Time complexity

# Append:
arr.append(7)
# O(n) Space complexity
# O(1) Time complexity
# Dynamic Arrays append most of the time in O(1), but when they reach their size limit they must move all the index values to a new array with more space, making that operation O(n)

# Insert and Delete:
arr.insert(0, 10)
# add to beginning of array --> O(n) Time complexity
# every index value needs to move over one space from where new one is inserted
arr.pop(4)
# O(n) because items need to shift over to fill empty spot

# Passing an integer (or other primitives--> string, float, boolean) does not change the original integer
# Pass by value
def double_integers(num):
    num *= 2
    return num
my_num = 5
new_num = double_integers(my_num)
print("new_num", new_num)
print("my_num", my_num)

# Passing in an array does change the original array
# Pass by reference
# In-Place algorithm
def double_nums_in_place(array):
    # take an array and double all the values
    for i in range(len(array)):
        array[i] *= 2
    return array
new_arr = double_nums_in_place(arr)
print("new_arr", new_arr)
print("arr", arr)

arr2 = [1, 2, 3, 4, 5]
# Out-of-Place algorithm
# doesn't mutate original array, creates and returns a copy
# More costly: Time - O(n), Space - O(n)
def double_nums_out_of_place(array):
    #create new array
    new_arr = []
    for item in array:
        new_arr.append(item * 2)
    return new_arr
new_arr2 = double_nums_out_of_place(arr2)
print("new_arr2", new_arr2)
print("arr2", arr2)
