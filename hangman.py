from english_words import get_english_words_set
import random

words = get_english_words_set(['web2'], lower=True)
see_chances = [
    """
     +----+     
     |    |     
          |     
          |     
          |     
          |     
    =========
    """,
    """
     +----+     
     |    |     
     o    |     
          |     
          |     
          |     
    =========
    """,
    """
     +----+     
     |    |     
     o    |     
     |    |     
          |     
          |     
    =========
    """,
    """
     +----+     
     |    |     
     o    |     
    /|    |     
          |     
          |     
    =========
    """,
    """
     +----+     
     |    |     
     o    |     
    /|\\  |     
          |     
          |     
    =========
    """,
    """
     +----+     
     |    |     
     o    |     
    /|\\  |     
    /     |     
          |     
    =========
    """,
    """
     +----+     
     |    |     
     o    |     
    /|\\  |     
    / \\  |     
          |     
    =========
    """
]

computer_guess = random.choice(list(words))
word_list = list(computer_guess)
chances, count = 7, 0
hide_word = ['_ '] * len(word_list)

print(hide_word)

print(computer_guess)

while chances > count:
  letter = input("guess a letter: ")
  if letter in hide_word:
    print(f"you are already choose {letter}")
    continue
  if letter in word_list:
    for i in range(len(word_list)):
      if word_list[i] == letter:
        hide_word[i] = letter

    print(hide_word)
    
    if hide_word == word_list:
      print("Congratilation!")
      break
  
        
  else:
    if count == 6:
      print(see_chances[count])
      print("Game Over! The word was:", computer_guess)
      break

    print(see_chances[count])
    count += 1

    





        

  






      