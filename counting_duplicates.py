#Count the number of Duplicates

#Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

#Example

#"abcde" -> 0 # no characters repeats more than once
#"aabbcde" -> 2 # 'a' and 'b'
#"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
#"indivisibility" -> 1 # 'i' occurs six times
#"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
#"aA11" -> 2 # 'a' and '1'
#"ABBA" -> 2 # 'A' and 'B' each occur twice

import numpy as np

def duplicate_count(text):
    text_arr = [text[i].lower() for i in range(0,len(text))]
    char_count = [text_arr.count(i) for i in np.unique(text_arr)]
    duplicates = 0
    for i in char_count:
        if i > 1:
            duplicates = duplicates +1
    return(duplicates)
