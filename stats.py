import matplotlib.pyplot as plt
import numpy as np


def max_words_board(content):
    entry = ["None", "0", "-"]
    for i in range(len(content)):
        if int(content[i][1]) > int(entry[1]):
            entry = content[i]
    print(f"Board with most words\n - Board: {entry[0]}\n - Nos words: {entry[1]}\n - Longest word: {entry[2]}")


def longest_word_board(content):
    entry = ["None", "0", "-"]
    for i in range(len(content)):
        if len(content[i][2]) > len(entry[2]):
            entry = content[i]
    print(f"Board with longest word\n - Board: {entry[0]}\n - Nos words: {entry[1]}\n - Longest word: {entry[2]}")


def averages(content):
    tot_words = 0
    for i in range(len(content)):
        tot_words += int(content[i][1])
    av_words = tot_words / len(content)
    print(f"Average nos words: {round(av_words, 1)}")


# nos vowel against nos words
def plot(content):
    # for entry in content:
    #     for i in range(16):
    #         if entry[0][i] in ("a", "e", "i", "o", "u"):
    #             i
    #
    nos_vowels = [len([entry[0][i] for i in range(16) if entry[0][i] in ("a", "e", "i", "o", "u")])
                  for entry in content]
    nos_words = [int(i[1]) for i in content]
    m, b = np.polyfit(nos_vowels, nos_words, 1)
    plt.scatter(nos_vowels, nos_words)
    plt.plot(np.array(nos_vowels), m * np.array(nos_vowels) + b)
    plt.show()


contents = []
with open("FakeBoards.txt", "r") as B_file:
    for line in B_file:
        contents.append(line.split(","))
max_words_board(contents)
longest_word_board(contents)
averages(contents)
plot(contents)
