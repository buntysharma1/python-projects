import os
import random
import time
def dice(n):
    for i in range(5):
        for j in range(13):
            if j == 0 :
                print("[",end="")
            if j == 12 :
                print("]")
            else:
                if ( i == 0 )or (i == 4 ) :
                    print("-",end="")
                else:
                    if( n == 1) :
                        if ( i == 2 ) and ( j == 6 ) :
                            print("0",end="")
                        else:
                            print(" ",end="")
                    elif ( n == 2 ):
                        if ( i == 2 ) and (( j == 4 ) or ( j == 8)) :
                            print("0",end="")
                        else:
                            print(" ",end="")
                    elif ( n == 3 ):
                        if( j == 6 ) :
                            print("0",end="")
                        else:
                            print(" ",end="")
                    elif ( n == 4 ):
                        if (( i == 1 ) or ( i == 3 ) ) and ( ( j == 4 ) or ( j == 8 )):
                            print("0",end="")
                        else:
                            print(" ",end="")
                    elif( n == 5 ):
                        if (( i == 1 ) or ( i == 3 ) ) and ( ( j == 4 ) or ( j == 8 )):
                            print("0",end="")
                        elif ( i == 2 ) and ( j == 6 ):
                            print("0",end="") 
                        else:
                            print(" ",end="")
                    elif( n == 6 ):
                        if( j == 4 ) or ( j == 8 ):
                            print("0",end="")
                        else:
                            print(" ",end="")
                    else:
                        print("\n\nSomething went wong!")


def random_number():
    player1=input("Enter Player1 Name : ")
    player2=input("Enter Player2 Name : ")
    player3=input("Enter Player3 Name : ")
    player4=input("Enter Player4 Name : ")
    p1=p2=p3=p4=0
    while p1 <= 25 and p2 <= 25 and p3 <= 25 and p4 <= 25 :
        os.system("cls")
        print("\n\t\tYour Scores")
        print(f"{player1}\t{player2}\t{player3}\t{player4}") 
        print(f"   {p1}\t{p2}\t{p3}\t{p4} ")
        for i in range(1,5):
            if i == 1:
                input(f" {player1}, Press Enter to roll the Dice... ")
                rand=random.randint(1,6)
                dice(rand)
                time.sleep(1)
                p1+=rand
            elif i == 2:
                input(f" {player2}, Press Enter to roll the Dice... ")
                rand=random.randint(1,6)
                dice(rand)
                time.sleep(1)
                p2+=rand
            elif i == 3:
                input(f" {player3}, Press Enter to roll the Dice... ")
                rand=random.randint(1,6)
                dice(rand)
                time.sleep(1)
                p3+=rand
            elif i == 4 :
                input(f" {player4}, Press Enter to roll the Dice... ")
                rand=random.randint(1,6)
                dice(rand)
                time.sleep(1)
                p4+=rand
            else:
                print("Something went Wrong...")
    list1=[p1,p2,p3,p4]
    a=0
    for i in list1:
        if a < i:
            a=i
    if p1==a:
        print(f"\n\t\t Great {player1}, You Won the Match... ")
    elif p2==a:
        print(f"\n\t\t Great {player2}, You Won the Match... ")
    elif p3==a:
        print(f"\n\t\t Great {player3}, You Won the Match... ")
    elif p4==a:
        print(f"\n\t\t Great {player4}, You Won the Match... ")
    print(f"{player1}\t{player2}\t{player3}\t{player4}") 
    print(f"   {p1}\t{p2}\t{p3}\t{p4}\n")
        

random_number()