import random

print('''H A N G M A N''')

list_word = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(list_word)
secret_word = ["-"] * len(word)
lives = 8
use_letters = []

def start():
    start = input('Type "play" to play the game, "exit" to quit: ')
    if start == "play":
        start = 1
    elif start == "exit":
        start = 0
    return start

menu = start()

while menu == 1:
    if "".join(secret_word) == word or lives == 0:
        word = random.choice(list_word)
        secret_word = ["-"] * len(word)
        lives = 8
        use_letters = []
    print()
    print("".join(secret_word))
    letter = input("Input a letter: ")   

    if len(letter) != 1:
        print("You should input a single letter")
        continue
    
    if letter in use_letters:
        print("You already typed this letter")
        continue
        
    if not letter.isalpha() or not letter.islower():
        print("It is not an ASCII lowercase letter")
        continue
    
    if letter not in word:
        use_letters.append(letter)
        lives -= 1
        print("No such letter in the word")
        if lives == 0:
            print("You are hanged!")
            print()
            menu = start()
    else:
        use_letters.append(letter)
        for i in range(len(word)):
            if letter == word[i]:
                secret_word[i] = letter
    if "".join(secret_word) == word:
        print("""You guessed the word!
        You survived!""")
        menu = start()
