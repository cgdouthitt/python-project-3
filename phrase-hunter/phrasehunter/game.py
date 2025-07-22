from phrasehunter.phrase import Phrase
import random

# Create your Game class logic in here.


class Game:
    def __init__(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def welcome(self):
        print("Welcome to the phrase hunter game!!")

    def start(self):
        self.welcome()
        play = True
        while play == True:
            while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
                print(f'Number missed: {self.missed}')
                Phrase.display(self.active_phrase, self.guesses)
                user_guess = self.get_guess()
                self.guesses.append(user_guess)
                Phrase.check_guess(self.active_phrase, user_guess)
                if not self.active_phrase.validate_guess(user_guess):
                    print("False")
                elif not self.active_phrase.check_guess(user_guess):
                    self.missed += 1
            self.game_over(self.active_phrase.check_complete(self.guesses))
            new_game = input(f"\nWould you like to play again (y/n):  ")
            if not new_game.lower() == 'y':
                play = False
                print("Thank you for playing!!")
            else:
                self.reset_game()

    def reset_game(self):
        self.missed = 0
        self.phrases = self.create_phrases()
        self.active_phrase = self.get_random_phrase()
        self.guesses = [" "]

    def create_phrases(self):
        return [
            Phrase("hello world"),
            Phrase("there is no trying"),
            Phrase("may the force be with you"),
            Phrase("you have to see the matrix for yourself"),
            Phrase("life is like a box of chocolates"),
            Phrase("over the line mark it zero")
        ]

    def get_random_phrase(self):
        random_num = random.randint(0, 4)
        selected_phrase = self.phrases[random_num]
        return selected_phrase

    def get_guess(self):
        return input(f'\nPlease enter a letter: ')

    def game_over(self, outcome):
        if outcome == True:
            print(f'Number missed: {self.missed}')
            Phrase.display(self.active_phrase, self.guesses)
            print(f"\nYou won!!")
        else:
            print(f'Number missed: {self.missed}')
            Phrase.display(self.active_phrase, self.guesses)
            print(f"\nYou Lost!")
