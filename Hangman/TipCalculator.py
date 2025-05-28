import random

print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
""")

# Reversed ASCII art stages: full hangman to empty
stages = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''']

# Word list and game setup
word_list = ["america", "africa", "india"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
correct_letters = []
game_over = False

# Display setup
display = ["_" for _ in range(word_length)]
print(" ".join(display))

# Game loop
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You already guessed '{guess}'. Try a new letter.")
    elif guess in chosen_word:
        for idx, letter in enumerate(chosen_word):
            if letter == guess:
                display[idx] = guess
        correct_letters.append(guess)
    else:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")
        correct_letters.append(guess)

    print(" ".join(display))
    print(stages[6 - lives])  # Shows correct stage by lives lost

    if "_" not in display:
        print("🎉 You win!")
        game_over = True
    elif lives == 0:
        print("💀 You lose! The word was:", chosen_word)
        game_over = True
