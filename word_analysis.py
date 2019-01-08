import re
import operator


def three_most_common_words(path):
    '''
    Given the path to a text file, will return the 3 most common words in the file.

    A word consists of alphabetic characters and is separated on both sides
    by space characters (space, newline, tab) or the beginning or end of the
    file. Hyphens may be part of a word, but other punctuation should is ignored.

    Note: According to this definition "forebodings." would not be counted as a word
    since it has a period at its end and is thus not separated on both sides by space characters.

    Assumes words are not distinguished by case. So "At" and "at" are treated as the same word.

    :param path: file path to text file
    :return: list of the three most common words in the file (ordered most common to least common)
    '''

    # regex pattern : (?<=\s)([a-zA-Z]+[-]?[a-zA-Z]*)(?=\s)
    # (?<=\s) : Positive Lookbehind for space characters
    # ([a-zA-Z]+ : Match 1 or more alphabetic characters
    #   [-]? : Match 0 or 1 hyphens
    #   [a-zA-Z]*) - Match 0 or more alphabetic characters
    # (?=\s) - Positive Lookahead for space characters
    word_pattern = re.compile("(?<=\s)([a-zA-Z]+[-]?[a-zA-Z]*)(?=\s)")
    word_occurences = {}

    with open(path) as file:
        for line in file:
            # find matching words and convert to lowercase
            words = [word.lower() for word in word_pattern.findall(line)]

            # increment word count for each word
            for word in words:
                if word in word_occurences:
                    word_occurences[word] += 1
                else:
                    word_occurences[word] = 1

    # sort dictionary values and take top three
    three_tuples = sorted(word_occurences.items(), key=operator.itemgetter(1), reverse=True)[:3]
    three_words = [i[0] for i in three_tuples]

    return three_words


def word_occurrences(word, path):
    '''
    Given a word and the path to a text file, return the number of occurrences
    of the word in the file.

    A word consists of alphabetic characters and is separated on both sides
    by space characters (space, newline, tab) or the beginning or end of the
    file. Hyphens may be part of a word, but other punctuation should is ignored.

    Ignores case when counting occurrences.  Counts only occurrences of word
    preceded and followed by space characters.

    :param word: word in which to search for occurrences in file
    :param path: file path to text file
    :return: number of occurrences of word in the file
    '''

    # strip any extra whitespace
    stripped_word = word.strip()

    # the regex pattern makes sure the word has space characters before and after
    # the pattern matches any occurrences of the word, regardless of case
    word_pattern = re.compile("(?<=\s)(" + stripped_word + ")(?=\s)", re.IGNORECASE)
    word_occurences = 0

    with open(path) as file:
        for line in file:
            # find number of matching words and update occurrence total
            word_occurences += len(word_pattern.findall(line))

    return word_occurences


if __name__ == '__main__':
    # Given the path to a text file, return the 3 most common words in the file.
    file_path = "/Users/callisto/Downloads/84-0.txt"
    words = three_most_common_words(file_path)
    print(words)

    # Given a word and the path to a text file, return the number of occurrences
    # of the word in the file.
    for word in words:
        occurrences = word_occurrences(word, file_path)
        print(word + ": " + str(occurrences))
