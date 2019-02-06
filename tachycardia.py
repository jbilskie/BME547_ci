
def is_tachycardic(word):
    # Make it all lower case
    word = word.lower()
    # Remove punctuation and spaces
    word = no_punct_spaces(word)
    if 'tachycardic' in word:
        presence = True
    else:
        presence = False

    return presence


def no_punct_spaces(word):
    punct = '''.,!?-=/\(){}[]@#'$%^&*_+~` |:;"<>1234567890'''
    word_out = ""
    for letter in word:
        if letter not in punct:
            word_out = word_out + letter
    return word_out
