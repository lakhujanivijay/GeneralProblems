
import collections


def verify_anagrams(first_word, second_word):

    count_first_word = dict(collections.Counter(first_word.upper()))
    count_second_word = dict(collections.Counter(second_word.upper()))
    if count_first_word.has_key(' '):
        del count_first_word[' ']
    if count_second_word.has_key(' '):
        del count_second_word[' ']

    if cmp (count_first_word, count_second_word) == 0:
        return True
    else:
        return False
    



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert isinstance(verify_anagrams(u"a", u"z"), bool), "Boolean!"
    assert verify_anagrams(u"Programming", u"Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams(u"Hello", u"Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams(u"Kyoto", u"Tokyo") == True, "The global warming crisis of 3002"
