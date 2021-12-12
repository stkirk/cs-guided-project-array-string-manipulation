def strReverse_1(chars):
    # instantiate reference to start of list
    start_pointer = 0
    # instantiate reference to end of list
    end_pointer = len(chars) -1
    # loop through range of chars indicies
    while start_pointer < end_pointer:
        # store start before swap:
        store = chars[start_pointer]
        # swap elements
        chars[start_pointer] = chars[end_pointer]
        chars[end_pointer] = store
        #update pointers:
        start_pointer += 1
        end_pointer -= 1
    return chars