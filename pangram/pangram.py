import string


def is_pangram(sentence):
    return set(sentence.lower()).issuperset(set(string.ascii_lowercase))
