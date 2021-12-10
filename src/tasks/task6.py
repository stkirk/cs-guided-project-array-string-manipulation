# Given a string, replace each letter with by the letter following it in the English alphabet
# i.e. replace "b" with "c"
# letter = chr(97)
# letter == "a"
# ord("h") => 104

def alphaPlusOne(inputString):
    # create new string to add on to
    new_str = ""
    # loop through inputString
    for letter in inputString:
        # if letter is z, add an a
        if letter == "z":
            new_str += "a"
        # otherwise add character value of ord("letter") + 1
        else:
            new_str += chr(ord(letter) + 1)
    return new_str


print(alphaPlusOne("crazy")) #--> "dsbaz"