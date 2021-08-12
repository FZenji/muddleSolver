def max_words_board():
    content = []
    with open("Boards.txt", "r") as B_file:
        for line in B_file:
            content.append(line.split(","))
    entry = ["None", "0", "-"]
    for i in range(len(content)):
        if int(content[i][1]) > int(entry[1]):
            entry = content[i]
    print(f"Board with most words\n - Board: {entry[0]}\n - Nos words: {entry[1]}\n - Longest word: {entry[2]}")


def longest_word_board():
    content = []
    with open("Boards.txt", "r") as B_file:
        for line in B_file:
            content.append(line.split(","))
    entry = ["None", "0", "-"]
    for i in range(len(content)):
        if len(content[i][2]) > len(entry[2]):
            entry = content[i]
    print(f"Board with longest word\n - Board: {entry[0]}\n - Nos words: {entry[1]}\n - Longest word: {entry[2]}")


max_words_board()
longest_word_board()
