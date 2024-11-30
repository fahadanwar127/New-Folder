import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self):
        self.the_word = "pizza"
        self.progress = ["?" for _ in self.the_word]
        self.guesses = 0
        self.letters_used = set()

    def make_guess(self, guess):
        if guess in self.letters_used:
            return "You've already used that letter. Try a different one!"

        if guess in self.the_word:
            self.letters_used.add(guess)
            self.progress_updater(guess)
            if "?" not in self.progress:
                return "Congratulations! You've guessed the word and survived!"
            return "As it turns out, your guess was RIGHT!"
        else:
            self.guesses += 1
            self.letters_used.add(guess)
            if self.guesses >= 6:
                return f"Game Over! The word was: {self.the_word}"
            return "Things aren't looking so good, that guess was WRONG!"

    def progress_updater(self, guess):
        for i, letter in enumerate(self.the_word):
            if letter == guess:
                self.progress[i] = guess

    def get_progress(self):
        return "".join(self.progress)

    def get_hangman_graphic(self):
        stages = [
            "________\n|      |\n|\n|\n|\n|\n",
            "________\n|      |\n|      0\n|\n|\n|\n",
            "________\n|      |\n|      0\n|     / \n|\n|\n",
            "________\n|      |\n|      0\n|     /| \n|\n|\n",
            "________\n|      |\n|      0\n|     /|\\\n|\n|\n",
            "________\n|      |\n|      0\n|     /|\\\n|     / \n|\n",
            "________\n|      |\n|      0\n|     /|\\\n|     / \\\n|\nThe noose tightens around your neck, and you feel the\nsudden urge to urinate.\nGAME OVER!\n"
        ]
        return stages[self.guesses]

class HangmanGUI:
    def __init__(self, root):
        self.game = HangmanGame()

        self.root = root
        self.root.title("Hangman Game")

        self.info_label = tk.Label(root, text="Guess a letter:")
        self.info_label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.guess_button = tk.Button(root, text="Submit Guess", command=self.submit_guess)
        self.guess_button.pack()

        self.progress_label = tk.Label(root, text=self.game.get_progress())
        self.progress_label.pack()

        self.hangman_label = tk.Label(root, text=self.game.get_hangman_graphic())
        self.hangman_label.pack()

        self.message_label = tk.Label(root, text="")
        self.message_label.pack()

    def submit_guess(self):
        guess = self.entry.get().lower()
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        result = self.game.make_guess(guess)
        self.progress_label.config(text=self.game.get_progress())
        self.hangman_label.config(text=self.game.get_hangman_graphic())
        self.message_label.config(text=result)
        
        if "Congratulations" in result or "Game Over" in result:
            self.guess_button.config(state=tk.DISABLED)
            self.entry.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    game_gui = HangmanGUI(root)
    root.mainloop()



