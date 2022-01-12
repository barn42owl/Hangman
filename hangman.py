import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


end_of_game= False
lives=6

word_list=["ardvark", "baboon", "camel"]
chosen_word= random.choice(word_list)
print(chosen_word)


word_length=len(chosen_word) 
display=' _ '*word_length
display=display.split()
print(display)


while not end_of_game:
    guess= input("Guess a letter: ")
    guess=guess.lower()
    
    def split(chosen_word):
        return [char for char in chosen_word]
        chosen_word=split(chosen_word)
        
    for position in range(word_length):
        letter= chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    print(display)
        
    if guess not in chosen_word:
        lives=lives-1
        print(stages[lives])
        if lives==0:
            end_of_game= True
            print("You lose!")
            
            
    if "_" not in display:
        end_of_game= True
        print("You win!")
        print(stages[lives])
