
def is_tachycardic(word):
    # Make it all lower case
    word = word.lower()
    # Remove punctuation and spaces
    word = no_punct_spaces(word)
    if 'tachycardic' in word:
        presence = True
    else:
        is_it_close = close(word, 'tachycardic')
        print(is_it_close)
        if is_it_close:
            presence = True
        else:
            presence = False

    return presence


def no_punct_spaces(word):
    punct = '''.,!?-=(){}[]@#'$%^&*_+~`/ |:;"<>1234567890'''
    word_out = ""
    for letter in word:
        if letter not in punct:
            word_out = word_out + letter
    return word_out


def close(word, desired):
    word = no_punct_spaces(word)
    is_it_close = False
    word_list = list(word)
    desired_word_list = list(desired)
    error = 0
    ind_w = 0
    ind_d = 0
    done = False
    while done is False:
        if word_list[ind_w] != desired_word_list[ind_d]:
            if (word_list[ind_w] != desired_word_list[ind_d+1]):
                # this letter is a typo
                ind_w = ind_w + 1
                ind_d = ind_d + 1
                error = error + 1
            elif (word_list[ind_w] == desired_word_list[ind_d+1]):
                # this letter is missing
                ind_d = ind_d + 1
                error = error + 1
        else:
            ind_d = ind_d + 1
            ind_w = ind_w + 1
        if (ind_w >= len(word_list)) | (ind_d+1 >= len(desired)):
            error = error + len(desired) - (ind_d+1)
            done = True
    if error < 3:
        is_it_close = True
    return is_it_close
