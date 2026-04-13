def most_common_word(filename):
    '''
    :param filename:
    :return: Most common word and number of occurences
    '''
    file = open(filename, "r")
    text = file.read().lower()
    file.close()

    clean_text = ""
    for char in text:
        if char.isalnum() or char.isspace(): #to remove punctuation
            clean_text += char

    words = clean_text.split()

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    most_word = ""
    most_count = 0

    for word in counts:
        if counts[word] > most_count:
            most_word = word #Sets the minimum conditions each tie a higher work is found
            most_count = counts[word]

    print("Most common word:", most_word)
    print("Count:", most_count)


most_common_word("sample.txt")