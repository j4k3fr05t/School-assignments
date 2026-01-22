import random

class HangmanGame:
    def __init__(self):
        self.word_list = [
            "python", "hangman", "computer", "programming", "algorithm",
            "developer", "keyboard", "monitor", "internet", "software",
            "database", "network", "security", "function", "variable"
        ]
        self.word = random.choice(self.word_list).upper()
        self.guessed_letters = set()
        self.attempts_left = 7

    def display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)

    def display_status(self):
        print("\n" + "="*40)
        print(f"Word:     {self.display_word()}")
        print(f"Attempts left: {self.attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(self.guessed_letters)) if self.guessed_letters else 'None'}")
        print("="*40)

    def guess_letter(self, letter):
        letter = letter.upper()

        if len(letter) != 1 or not letter.isalpha():
            print("→ Please enter a single letter.")
            return False

        if letter in self.guessed_letters:
            print("→ You already guessed that letter.")
            return False

        self.guessed_letters.add(letter)

        if letter in self.word:
            print(f"→ Good guess! '{letter}' is in the word.")
            return True
        else:
            self.attempts_left -= 1
            print(f"→ Wrong! '{letter}' is not in the word.")
            return False

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        return self.attempts_left <= 0

    def play(self):
        print("Welcome to Hangman!")
        print("Guess the word. You have 7 attempts.\n")

        while True:
            self.display_status()

            if self.is_won():
                print(f"\nCongratulations! You guessed the word: {self.word}")
                break
            if self.is_lost():
                print(f"\nGame Over! The word was: {self.word}")
                break

            guess = input("Guess a letter: ").strip()
            self.guess_letter(guess)

        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again == 'y':
            print("\n" + "-"*40 + "\n")
            new_game = HangmanGame()
            new_game.play()


if __name__ == "__main__":
    game = HangmanGame()
    game.play()
