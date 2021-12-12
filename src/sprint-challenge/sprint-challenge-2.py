# given a string, check if the string is a palindrome
# reads the same forwards and backwards
# use a loop to iterate through the string and make nexessary comparisions

def palindromeCheck(input_str):
    # instantiate reversed_str by slicing input_str
    reversed_str = input_str[::-1]
    # loop through input_str
    for i in range(len(input_str)):
        # compare input_str[i] to reversed_str[i]
        if input_str[i] != reversed_str[i]:
            # if false return false
            return False
    # loop runs all the way through, return True
    return True

print(palindromeCheck("racecar")) #--> True
print(palindromeCheck("anna")) #--> True
print(palindromeCheck("12345")) #--> False
print(palindromeCheck("12321")) #--> True