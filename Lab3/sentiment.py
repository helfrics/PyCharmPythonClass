import string


def load_score_dict(score_dict='sentiment.txt'):
    """
    Return dictionary with words as keys and corresponding scores as values.
    :param score_dict: A score dictionary file name (default to sentiment.txt)
    :return: A dictionary with keys in words and values in floats
    """
    with open(score_dict, 'r') as f:
        dictionary = {}

        # Remove empty lines from file.
        lines = (line.strip() for line in f)
        lines = (line for line in lines if line)

        for line in lines:
            if line.startswith('#'):
                pass
            else:
                (word, score) = line.split()
                dictionary[str(word)] = float(score)
    return dictionary


def get_words(sentence):
    """
    Retrieve unique words from within sentence.
    :param sentence: A string
    :return: An iterable
    """

    # Remove punctuation and make all letters lowercase.
    # Autograder didn't like translate: almost_clean_sentence = sentence.translate(None, string.punctuation)
    exclude = set(string.punctuation)
    almost_clean_sentence = ''.join(jot for jot in sentence if jot not in exclude)
    clean_sentence = almost_clean_sentence.lower()

    if not clean_sentence.strip():
        raise ValueError
    else:
        unique_words = set(clean_sentence.split())
        return list(unique_words)


def score_sentence(sentence, score_dict):
    """
    Compute sentence score as the sum of the word scores.
    :param sentence: A string
    :param score_dict: A score dictionary file name
    :return: A score as a float
    """

    word_set = get_words(sentence)
    score = 0

    for unique_word in word_set:
        for word in score_dict:
            if unique_word == word:
                score += score_dict[word]
            else:
                pass
    return score


if __name__ == '__main__':

    test_dict = load_score_dict()
    # print(test_dict)
    # print(len(test_dict))
    #
    # try:
    #     test_sentence = "Go home, Shirley!     Goodbye, Shirley. 4.Pete's sake! HOME."
    #     print(get_words(test_sentence))
    # except ValueError:
    #     print('The sentence is empty.')
    #
    # test_score_sentence = 'Abe abandoned ability, George!'
    # test_score = score_sentence(test_score_sentence, test_dict)
    # print(test_score)
    # print(type(test_score))

    import sys

    if len(sys.argv) <= 1:
        print('Please enter a file name.')
        print('Example: python sentiment.py filename.txt')
        sys.exit(0)
    else:
        some_sentence = sys.argv[1]
        file_score = score_sentence(some_sentence, test_dict)
        if file_score > 0:
            print('Positive')
        elif file_score < 0:
            print('Negative')
        else:
            print('Neutral')
