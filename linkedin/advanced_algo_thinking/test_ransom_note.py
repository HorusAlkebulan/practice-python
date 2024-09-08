# test_ransom_note.py

from ransom_note import ransom_note


def test_true():
    magazine_words = "give me one grand today night".split()
    note_words = "give one grand today".split()
    assert ransom_note(magazine_words, note_words) == True


def test_false():
    magazine_words = "two times three is not four".split()
    note_words = "two times two is four".split()
    assert ransom_note(magazine_words, note_words) == False
