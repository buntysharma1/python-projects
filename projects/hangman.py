import os
import random
import time

Name=['bunty',
      'sharma',
      'aarush',
      'ashok',
      'joy',
      'akash',
      'pritam',
      'deepshikha',
      'vandana',
      'baby',
      'abhijeet',
      'ekta']
Fruits=['apple',
        'banana',
        'mango',
        'pineapple',
        'watermelon',
        'papaya',
        'pears',
        'maskmelon']
Vegetables=['ladzfinger',
            'brinjal',
            'broccoli',
            'corn',
            'lettuce',
            'cucumber',
            'beetroot',
            'pumpkin']
Superheroes=['superman',
             'spiderman',
             'batman',
             'ironman',
             'caption america',
             'black widow',
             'hluk',
             'thor',
             'antman',
             'wolverin']
Random_words=['hello',
              'somaiya',
              'kvains',
              'backbanchers',
              'football',
              'alone',
              'ronaldo',
              'messi',
              'father']
Transports=['cars',
            'auto',
            'truces',
            'suv',
            'train',
            'airoplane',
            'ship',
            'bycycle',
            'bike']

def word_chooser( name ):
    os.system('cls')
    print("\n\n\t\tWelcome to Hangman game <( \"-\" )>")
    print(f"\n\tWhich Types of Words Want to guess { name } ")
    print('\t\t1.Names')
    print('\t\t2.Fruits')
    print('\t\t3.Vegetables')
    print('\t\t4.Superheroes')
    print('\t\t5.Random Word')
    print('\t\t6.Transports')
    choice=int(input('\n\tChoose From Above (1-6) : '))
    if choice == 1:
        rand=random.randint(1,len(Name))
        word=Name[rand]
    elif choice == 2 : 
        rand=random.randint(1,len(Fruits))
        word=Fruits[rand]
    elif choice == 3 :
        rand=random.randint(1,len(Vegetables))
        word=Vegetables[rand]
    elif choice == 4:
        rand= random.randint(1,len(Superheroes))
        word=Superheroes[rand]
    elif choice == 5:
        rand= random.randint(1,len(Random_words))
        word=Random_words[rand]
    elif choice == 6 : 
        rand=random.randint(1,len(Transports))
        word=Transports[rand]
    else:
        print("Please choose between 1 and 6 only...\n")
        time.sleep(2)
        return word_chooser(name)
    return word

def Hangman_logic(incomplete_word,word,name):
    wrong=0
    while wrong != 11 :
        os.system('cls')
        person(wrong)
        print(f'guess the word : {incomplete_word} ')
        letter=str(input('Enter Letter : '))
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    x=list(incomplete_word)
                    incomplete_word=""
                    x[i]=letter
                    for l in x:
                        incomplete_word+=l
        else:
            wrong+=1
            print('\n Its a Wrong letter \nTry Again...')
        if incomplete_word == word:
            os.system('cls')
            print(f"\n\n\t\t\tGreat {name}, You Saved Him (\"-\") !")
            person(11)
            time.sleep(2)
            exit()

def main():
    print("\n\n\t\t\tWelcome to Hangman Game <(\"_\")>")
    name = input("Enter Name : ")
    os.system('cls')
    word = word_chooser(name)
    incomplete_word=""
    for _ in range(len(word)):
        incomplete_word+="-"
    Hangman_logic(incomplete_word,word,name)


def person(n):
    print("\n=========")
    if (n==1):
        print(" 0 ")
    elif(n==2):
        print("  0")
        print("  |")
    elif(n==3):
        print("  0 ")
        print("  | ")
        print(" / ")
    elif(n==4):
        print("  0 ")
        print("  | ")
        print(" / \\ ")
    elif(n==5):
        print(" \\ 0 ")
        print("   | ")
        print("  / \\ ")
    elif(n==6):
        print(" \\ 0 / ")
        print("   |  ")
        print("  / \\ ")
    elif(n==7):
        print(" \\ 0 /  | ")
        print("   |  ")
        print("  / \\ ")
    elif(n==8):
        print(" \\ 0 / _| ")
        print("   |  ")
        print("  / \\ ")
    elif(n==9):
        print(" \\ 0 /_| ")
        print("   |  ")
        print("  / \\ ")
    elif(n==10):
        print("  0_| ")
        print(" /|\\  ")
        print(" / \\ ")
        print("\nYOU MAKE HIM HANG ")
        time.sleep(2)
        exit()
    elif(n==11):
        print(" \\ 0 / ")
        print("   |  ")
        print("  / \\ ")
    print("\n")
main()
