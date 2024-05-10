# Creating a list to hold the word bank
import random
from collections import Counter
person = ["Player #1","Player #2"]
word_bank = ["Australia", "Mexico", "Armenia", "Albania", "Belize", "Belgium", "Nepal", "Bulgaria", "Norway", "Canada","Cambodia", "Chile", "China", "Panama", "Poland", "Denmark","Russia","Egypt","Serbia","Singapore","Fiji","France", "Sweden","Greece","Ireland", "Israel","Yemen", "Liberia"]


# Welcoming message to players and giving them instructions of how to play
def guess_word(person, word_bank):
    print("Hello players! You are now a player of my mystery guessing game. Each time you pick a letter in our mystery word and the program will tell you if that letter is in the word or not. You get 3 tries to guess the word using only the clues from previous letter guesses. At the end of one player's turn, it becomes a second player's turn. Each time you guess a letter that's one point added to your score. Lowest score wins.")
   
    # Creating a loop where the program selects a word from the bank and loops from player to player to make a letter guess.
    for current_player in person: 
        chosen_word = random.choice(word_bank)
        tries_left = 3
        letter_guess = Counter()
        correct_guess = False
        # This keeps track of the number of guesses each player makes, also it allows the players to continue guessing until they run out of tries. This is when it prompts players for a letter input.
        while tries_left > 0:
            print("Number of tries left:",tries_left)
            counting_letter = input("Guess a letter that you think is in the word:").lower()
            times_used = chosen_word.lower().count(counting_letter)
            letter_guess[current_player] += 1
            # This tells the player if their guess is in the chosen word.
            if counting_letter in chosen_word.lower():
                print (f"Good job! You are right. The number of times that letter is in the word is '{times_used}' times")
            else:
                print("No. I'm sorry...that's not correct.")
            tries_left -=1
            word_guess = input("Enter the word you believe is our mystery word: ").lower() 
            # This is what happens when the player runs out of tries. Here they must guess the word and they are told if they are correct or not.      
            if word_guess == chosen_word.lower():
                print(f"Good job! You guessed the word '{chosen_word}' ")
                correct_guess = True
                break
            else:
                print("No I'm sorry... that is not correct.")
        # This prints the ending score if a player runs out of tries and guesses incorrectly.
        if not correct_guess:
            ending_game =  letter_guess[current_player]
            print(f"The ending score is {current_player}: {ending_game}")
        if correct_guess or tries_left ==0:
            break
guess_word(person, word_bank)

