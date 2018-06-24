from gmail import *

def test_word_tokenizer():
    input='python is so fun i love python and i love pythoning with python so lets go python'
    word_tokenizer(input)
    assert bucket_of_words==['python','fun','love','python','love','pythoning','python','lets','python']


def test_most_common_words():
    bucket_of_words==['python','fun','love','python','love','pythoning','python','lets','python']
    assert (Counter(bucket_of_words).most_common(2))==[('python',4),('love',2)]
