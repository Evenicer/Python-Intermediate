def run():
    word = "Holo"
    new_word = word[:3] + 'a'
    wordS = list(word)
    print(len(wordS))
    wordS[3] = "a"

    word_ui = list(len(word)*"_")

    word_ui[3] = 'i'

    print(word_ui)

if __name__ == '__main__':
    run()