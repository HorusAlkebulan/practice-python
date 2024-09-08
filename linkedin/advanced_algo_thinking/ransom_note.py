# ransom_note.py


def ransom_note(magazine_words: list, note_words: list) -> bool:

    # initalize
    word_map = {}

    # iterate over magazine words
    # if in map, increment count
    # otherwise, add to map with count=1
    for magazine_word in magazine_words:
        if magazine_word in word_map:
            word_map[magazine_word] += 1
        else:
            word_map[magazine_word] = 1

    # iterate over note words
    # if in map AND count > 0, decrement count in map for word key
    # otherwise, return False
    for note_word in note_words:
        if note_word in word_map and word_map[note_word] > 0:
            word_map[note_word] -= 1
        else:
            return False

    # if get to end, we're ok, return True
    return True
