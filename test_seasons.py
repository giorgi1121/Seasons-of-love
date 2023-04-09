from seasons import minutes, minutes_with_words, valid_format

def main():
    test_minutes()
    test_minutes_with_words()
    test_valid_foramt()

#test minutes function
def test_minutes():
    assert minutes("2001-06-06") == 11486880
    assert minutes("2017-09-25") == 2911680
    assert minutes("2023-04-08") == 1440

#test minutes to words function
def test_minutes_with_words():
    assert minutes_with_words(1) == "One minutes"
    assert minutes_with_words(100) == "One hundred minutes"
    assert minutes_with_words(150) == "One hundred fifty minutes"
    assert minutes_with_words(1002050) == "One million, two thousand fifty minutes"
#test valid format function
def test_valid_foramt():
    assert valid_format("2001-06-06") == True
    assert valid_format("2001/06/06") == False


if __name__ == '__main__':
    main()
