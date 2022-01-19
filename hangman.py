import random
import os


def read_Data():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.rstrip("\n"))        
    return words


def get_word():
    words = read_Data()
    pos_random = random.randint(1,len(words))

    #palabra a buscar
    word = words[pos_random]
    return word
      


def play():
    os.system("cls")

    word = get_word()
    print(word)

    word_user = []
    word2 = []
    word_ui = list(len(word)*"_")

    while len(word2) != len(word):
        print("Your try: ")
        print(word_ui)

        word_user = input("Enter a letter: ")

        for i in range(len(word)):
            if word_user == word[i]:
                word_ui[i] = word_user
                word2.append(word_user)
        os.system("cls")    

    print("Your try: ")
    print(word_ui)            
    print("You win! The word was: "+word)



if __name__ == '__main__':
    play()