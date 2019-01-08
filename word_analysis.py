import re
import operator
import sys


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


def print_usage():
    '''
    Prints command line program usage information.
    :return:
    '''

    print('Usage : "python word_analysis.py function [word] file')
    print('function: either "common" or "occur"')
    print(' -common : return the 3 most common words in the file')
    print(' -occur : return the number of occurrences of the word in the file')


if __name__ == '__main__':
    # exit program if incorrect number of arguments are given
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print_usage()
        sys.exit(2)

    if sys.argv[1] == "common" and len(sys.argv) == 3:
        words = three_most_common_words(sys.argv[2])
        print("Three most common words:")
        print(", ".join(words))
    elif sys.argv[1] == "occur" and len(sys.argv) == 4:
        number = word_occurrences(sys.argv[2], sys.argv[3])
        print(str(number) + " occurrences of the word '" + sys.argv[2] + "'")
    else:
        print_usage()
        sys.exit(2)
