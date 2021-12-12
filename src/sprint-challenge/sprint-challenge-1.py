# given a list of characters (each index is a single char), represent the list as a string and return it in reverse
# solutions must be in-place (change the list being passed in)
# O(1) space complexity
# return the modified input
# no built in reverse methods

lst_1 = ["l", "a", "m", "b", "d", "a"]
lambd = ["0", "1", "2", "3", "4", "5"]
lst_2 = ["I", "'", "m", " ", "a", "w", "e", "s", "o", "m", "e"]

def strReverse(chars):
    # instantiate start pointer
    start_pointer = 0
    # instantiate reference to end of list
    end_pointer = len(chars) -1
    # loop through range of chars indicies
    for i in range(len(chars)//2):
        #temporarily save char[i] before swap
        store = chars[i]
        # swap values
        chars[i] = chars[end_pointer]
        chars[end_pointer] = store
        end_pointer -= 1
    return chars

strReverse(lst_1)
strReverse(lst_2)

print(lst_1) #--> ["a", "d", "b", "m", "a", "l"]
# print(lst_2) #--> #--> ["e", "m", "o", "s", "e", "w", "a", " ", "m", "'", "I"]
