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
    pos_random = random.randint(1,100)

    #palabra a buscar
    word = words[pos_random]
    return word
      


def play():
    os.system("cls")
    word = get_word()
    print(word)
    word_user = ""
    word_ui = len(word)*" _ "

    while len(word_user) != len(word):
        print("Your try: " + word_ui)
        word_user = word_user + input("Ingresa una letra: ")

        for i in range(len(word)):
            if word_user == word[i]:
                pass
                
                
        os.system("cls")        
        
    
    if word_user == word:
        print("Ganaste! La palabra era: "+word)



if __name__ == '__main__':
    play()