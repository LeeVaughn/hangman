import random

def hangman(word):
  wrong = 0
  stages = ["",
            " ________     ",
            "|      |      ",
            "|      0      ",
            "|     /|\     ",
            "|     / \     ",
            "|___________  "]
  rletters = list(word)
  board = ["__"] * len(word)
  win = False

  print("Welcome to Hangman!")
  print("The word is a food that Lee likes...")
  print(" ".join(board))

  # continues the game until wrong is no longer less than the length of stages - 1
  while wrong < len(stages) - 1:
    print('\n')

    msg = "Guess a letter: "
    guess = input(msg)

    # checks to see if the players guess is in the word
    # if yes, update board but if not, increment wrong
    if guess in rletters:
      cind = rletters.index(guess)
      board[cind] = guess
      # replaces correctly guessed letter with $
      rletters[cind] = "$"
    else:
      wrong += 1
    
    # displays board
    print((" ".join(board)))

    e = wrong + 1

    # uses e to slice up to the current stage of the game
    print("\n".join(stages[0: e]))

    if "__" not in board:
      print("You win!")
      print(" ".join(board))

      win = True
      break
  
  if not win:
    # print("\n".join(stages[0: wrong + 1]))
    print("You lose grandpa! It was {}.".format(word))

words = ["pizza", "chinese", "tacos", "pistachios", "burgers", "pockets"]
hangman(random.choice(words))
