import random

level1 = ["china", "egypt", "greece", "canada"]
level2 = ["brazil", "japan", "romania", "sweden"]
level3 = ["barbados", "cyprus", "uganda", "venezuela"]

name = input("Jak masz na imię? ")
print ( "Cześć! " + name + ". Czas na grę!")

alphabet = 'abcdefghijklmnopqrstuvwxyz'

gameMode = input('Wybierz poziom - 1 (łatwy), 2 (średni) lub 3 (trudny) ').lower()
if gameMode == '1':
    live = 3
    theWord = random.choice(level1)

elif gameMode == '2':
    live = 6
    theWord = random.choice(level2)

elif gameMode == '3':
    live = 8
    theWord = random.choice(level3)

else:
    print("Zły wybór")


blanks = ['_'] * len(theWord)

used_letters = []

print ("")


while live > 0:
    print ("Ilość pozostałych żyć: ", live)
    print (' '.join(blanks))

    
    guess = input("Zgaduj! ").lower()

  
    if not guess in alphabet:
        print("Wpisz litere...")

    elif guess in used_letters:
        print("To już było....")

    else:
        used_letters.append(guess)
        if (guess in theWord):
            print ("Trafiony!")
           
            for x in range(0, len(theWord)):
                if theWord[x] == guess:
                   
                    blanks[x] = guess
          
            if not '_' in blanks:
                print("Brawo", name, "!", "Wygrałeś!")
    
                break
        else:
            print ("Źle. Spróbuj ponownie!")
            live -= 1

print ("Koniec gry,", name, "!")
