def hangman(word):
  wrong = 0
  stages = ["",
            "________      ",
            "|      |      ",
            "|      0      ",
            "|     /|\     ",
            "|     / \     ",
            "|"]
  rletters = list(word)
  board = ["_"] * len(word)
  win = False

  print("Welcome to Hangman!")

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

    if "_" not in board:
      print("You win!")
      print(" ".join(board))

      win = True
      break
  
  if not win:
    print("\n".join(stages[0: wrong]))
    print("You lose grandpa! It was {}.".format(word))

hangman("deadwood")
    

# def hangman(word):
#     wrong_guesses = 0
#     stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
#     remaining_letters = list(word)
#     letter_board = ["__"] * len(word)
#     win = False
#     print("Welcome to Hangman")
#     while wrong_guesses < len(stages) - 1:
#         print('\n')
#         guess = input("Guess a letter")
#         if guess in remaining_letters:
#             character_index = remaining_letters.index(guess)
#             letter_board[character_index] = guess
#             remaining_letters[character_index] = '$'
#         else:
#             wrong_guesses += 1
#         print((' '.join(letter_board)))
#         print('\n'.join(stages[0: wrong_guesses + 1]))
#         if '__' not in letter_board:
#             print('You win! The word was:')
#             print(' '.join(letter_board))
#             win = True
#             break
#     if not win:
#         print('\n'.join(stages[0: wrong_guesses]))
#         print('You lose! The words was {}'.format(word))

# hangman("cat")