# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).
#
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

import string
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cap_alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def is_pangram(s):
    sentence_list = list(map(str,s))
    default_pangram_belief = True
    for i in range(0,26):
        if (alphabet[i] in sentence_list) or (cap_alphabet[i] in sentence_list):
            pass
        else:
            default_pangram_belief = False
    return default_pangram_belief
