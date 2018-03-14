# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 16:32:10 2018

@author: ron
"""


def trifecta(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """

    # Error handling
    if len(word) <= 1:
        return False

    identical_list = []
    prev_letter = word[0]
    # Check each letters identity to the previous letter
    for curr_letter in word[1:]:
        identical_list.append(curr_letter == prev_letter)
        prev_letter = curr_letter
        # A correct string should produce a sequence of True, *, True, *, True

    if sum(identical_list) >= 3:
        odd = identical_list[::2]
        even = identical_list[1::2]
        for sequence in (odd, even):
            if sum(sequence) >= 3:
                seq_str = str(sequence)
                search_str = 'True, True, True'
                if search_str in seq_str:
                    return True
        return False

    else:
        return False


if __name__ == '__main__':
    g_words = ['aabbcc', 'abccddee0123', 'aaaazz']
    b_words = ['bbcCdd', 'llkkbmm', '']
    good = [trifecta(w) for w in g_words]
    bad = [trifecta(w) for w in b_words]
