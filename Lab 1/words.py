

def letter_count(text, letter):
    """
    Count occurrences of letter in text
    :param text: a many letter string
    :param letter: a single letter string
    :return: an integer
    """

    my_text = text.lower()
    my_letter = letter.lower()

    for i in my_text:
        if i == my_letter:
            if my_text.count(i) > 0:
                return my_text.count(i)
            else:
                return 0


if __name__ == '__main__':

    print(letter_count('goofy', 'O'))
    print(letter_count('goofy', 'g'))
    print(letter_count('gOofy', 'o'))
    print(letter_count('gooFy', 'l'))
