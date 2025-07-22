# Create your Phrase class logic here.
class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f'{letter} ', end=" ")
            elif letter == " ":
                print(f' ', end=" ")
            else:
                print(f'_ ', end=" ")

    def check_guess(self, guess):
        if guess.lower() in self.phrase:
            return True
        else:
            return False

    def validate_guess(self, guess):
        if not guess.isalpha():
            print(f"'{guess}' is not a valid letter. Please try again.")
            return False
        elif len(guess) > 1:
            print(f"'{guess}' is more than 1 character long. Please try again.")
            return False
        else:
            return True

    def check_complete(self, guesses):
        for letter in self.phrase:
            if letter not in guesses:
                return False
        return True
