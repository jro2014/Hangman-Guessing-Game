# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 10:14:58 2021

@author: JRO20
"""

from Hangman_Words import WordList
import random 


# Create a list of words from which to randomly choose

# Define a function to randomly select a word from the WordList

# Define a play function
    ## Show blanks (_) as unguessed letters
    ## Display guessed letters
    ## Ask the user for input either letter or word
    ## Check to see if they guessed a letter or a word by len(guess) > 1
    ## Check to see if they only guessed letters and not numbers (don't count it if they guessed numbers)
        ## Two variables for guessed letters and guesses words
    ## 7 guesses according to Wikipedia ('https://en.wikipedia.org/wiki/Hangman_(game)')
    ## Need a loop that will run until the word is guessed or the player runs out of tries (while not guessed(which will be set to False) and tries > 0) 
        ### User input for letter or word
        ### Check if they guess a letter or a word by len(guess) == 1 and is a letter
        ### Check to see if they guessed a letter that has already been guessed: if yes print an error message
        ### Check to see if the guessed letter is not in the word: if it is not in the word then print a fail message and append the guessed letter to the guessed list and subtract a try
        ### Check to see if the guess is in the word: if yes print a success message then append the guessed letter to the guessed list and
            #### Then we will need to replace the (_) with the guessed letter if it is in the word
        
        
# Define a function to return the little visuals will need to have the first be the full image with the full guy as a list which will be indexed with tries 

# Define a main function to put everything together
    ## Call get_word and play functions
    ## Increment a scoreboard based on result of the game 
    ## Ask if the user wants to play again
        ### Call get word and check if that word has already been used
        ### Call play
        ### Increment scoreboard 


def get_word():
    word = random.choice(WordList)
    return word.upper()


def play(word):
    # Setup:
    WordStatus = '_' * len(word)
    WordGuessed = False
    GuessedLetters = []
    GuessedWords = []
    tries = 6
    print("You ready for some hangman? ")
    print(HangmanPic(tries))
    print(WordStatus)
    print('\n')
    # While Loop
    while not WordGuessed and tries > 0:
        guess = input('Please guess a letter or a word: ').upper()
        # Guess a letter 
        if len(guess) == 1 and guess.isalpha():
            ## If the guess has already been guessed
            if guess in GuessedLetters:
                print("You have already guessed {guess}, dummass.".format(guess = guess)) # Print a failure message
            ## If the guess is in the word
            elif guess in word:
                print("Whoopdedoo, you got a letter.") # Print a success message
                GuessedLetters.append(guess) # put the guess in the guessed letters list
                WordAsList = list(WordStatus) # list the WordStatus string so that we can change the '_' to the guess
                indices = [i for i, letter in enumerate(word) if letter == guess] # grab indices for the guessed letters in the word
                for index in indices: # Iterate over the values in indices
                    WordAsList[index] = guess # replace the '_' in the WordStatus list to the correct guess
                WordStatus = ''.join(WordAsList) # Unlist the WordStatus joining with nothing
                ## Check to see if the guess completes the word
                if '_' not in WordStatus: # If no more '_' then word is complete
                    print('Hell yeah! You nailed it! Let\'s drink! The word was {word}.'.format(word = word)) # Print winning message
                    WordGuessed = True # Change WordGuessed to True breaking the loop
                    return(1) # Return 1 for scoreboard
            # Guess is not in the word
            else:
                print("NOPE. {guess} isn't in this word lol.". format(guess = guess)) ## Start the psychological warfare. Get into their heads. Make them feel small
                tries -= 1 # subtract one from the tries variable
                GuessedLetters.append(guess) # Add incorrect guess to the guessed letters list
                print(HangmanPic(tries)) # print out the current hangman pic 
        # Guess is a word
        elif len(guess) > 1 and guess.isalpha():
            ## If they have already guessed that word
            if guess in GuessedWords: # check to see if guess is in GuessedWords
                print('\'Cmon, you already guessed {guess}? Not even close Baby.'.format(guess = guess)) # print a failure message
                print(HangmanPic(tries)) # print out the current hangman pic 
            ## If they guess a word that is not in GuessedWords but wrong
            elif guess != word:
                print('Getting Ballsy, I see. Didn\'t pay off this time. {guess} is not the right word.'.format(guess = guess)) # print out a failure message
                tries -= 1 # reduce tries by 1
                GuessedWords.append(guess) # append the guessed word to GuessedWords
                print(HangmanPic(tries)) # print out the current hangman pic 
            ## If they guess the word
            else:
                WordStatus = guess # Update
                WordGuessed = True # Update status to terminate loop and move to the next section
                return(1)
        # Guess is not a word or letter or contains non alphanumeric
        else:
            print("Do you really think {guess} is in this word? What, are you stupid?.".format(guess = guess)) # Print a failure message
        print(HangmanPic(tries)) # print out the current hangman pic 
        print(WordStatus) # Display the WordStatus
        print('\n') # new line
    if WordGuessed: # print the winning statement if they guessed the word
        print('Hell yeah! You nailed it! Let\'s drink! The word was {word}.'.format(word = word)) # Print winning messate
        return(1) # output 1 indicating a win
    else:
        print('Good lord you are stupid. The word was {word}.'.format(word = word)) # print losing message 
        
  
    
  
# Function to print out the images after each turn
def HangmanPic(tries):
        stages =[ """
                 ----------
                 |        |
                 |        O
                 |       \\|/
                 |        |
                 |       / \\
                 |     
            ------------
            """,
            """
                 ----------
                 |        |
                 |        O
                 |       \\|/
                 |        |
                 |       /  
                 |     
            ------------   
            """,
            """
                 ----------
                 |        |
                 |        O
                 |       \\|/
                 |        |
                 |        
                 |     
            ------------ 
            """,
            """
                 ----------
                 |        |
                 |        O
                 |       \\|
                 |        |
                 |        
                 |     
            ------------ 
            """,
            """
                 ----------
                 |        |
                 |        O
                 |        |
                 |        |
                 |        
                 |     
            ------------ 
            """,
            """
                 ----------
                 |        |
                 |        O
                 |      
                 |        
                 |       
                 |     
            ------------ 
            """,
            """
                 ----------
                 |        |
                 |        
                 |      
                 |        
                 |       
                 |     
            ------------ 
            """]
        return stages[tries]
    
        
# Main function that will run everything
def hangman():
    UsedWords = [] # Used Words list to keep track of the words that have been used
    Wins = 0 # wins counter for scoreboard
    Losses = 0 # losses counter for scoreboard
    word = get_word() # Call the get_word function
    result = play(word) # Call the play function and store the output into result 
    if result == 1: # If statement to increment scoreboard for the first round
        Wins += 1
    else:
        Losses += 1
    UsedWords.append(word) # append the first word to the used words list 
    while input("Man enough to play again? (Y/N): ").upper() == "Y": # While loop to see if the player is brave enough to play again
        print('Wins: ', Wins, ' | Losses: ', Losses) # Print the scoreboard
        word = get_word() # Call the get_word function
        while word in UsedWords: # Check to see the word has already been used 
            word = get_word() # choose a new word until the word is not found in the usedwords list
        UsedWords.append(word) # Append the new word to the usedwords list
        result = play(word) # call the game function and store the output as result
        if result == 1: # increment the scoreboard for each iteration of the game
            Wins += 1
        else:
            Losses += 1
    print("FINAL SCORE: WINS {w} | LOSSES: {l}".format(w = Wins, l = Losses)) # Print final scoreboard when loop is broken


# Command Line capability  -- run the main function from the command line 
if __name__ == "__main__":
    hangman()










    