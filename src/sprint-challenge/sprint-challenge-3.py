# given a string of words separated by spaces, remove all duplicate words from the input_str.
# return string should only include the first occurence of each word

def noDupes(input_str):
    # create a list form input_str with words as index values
    word_lst = input_str.split()
    # create empty list to append to
    no_dupes = []
    # create a dictionary from word_list (built in elimination of dupes)
    word_dict = {word: i for (i, word) in enumerate(word_lst)}
    # loop through the word_lst
    for word in word_dict:
        # append to no_dupes
        no_dupes.append(word)
    #join no_dupes back into a string and return
    return ' '.join(no_dupes)



print(noDupes("alpha bravo bravo golf golf golf delta alpha bravo bravo golf golf golf delta")) #--> "alpha bravo golf delta"
print(noDupes("my dog is my dog is super smart")) #--> "my dog is super smart"


# refactor if time allows, to check in dictionary should be 
# if word in word_dict:
'''
# create a list from input_str with words as index values
    word_lst = input_str.split()
    # create an empty dictionary
    word_dict = {}
    # loop through the list
    for (i, word) in enumerate(word_lst):
        # check if the word exists in the dictionary
        if word in word_dict:
            # if it does remove it from the list
            
        # else add it to the dictionary
        if word in word_dict:
            # key/value "word": index
            word_dict[word] = i
    # join the list back into a string and return
    return word_dict
'''