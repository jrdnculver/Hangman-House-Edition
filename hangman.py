from random import randint
import tkinter as tk
from tkinter import messagebox
from alphabet import Alphabet as let
from house import House as home


class Hangman():
    def __init__(self):
        self.window = tk.Tk()
        self.windowAccessories()
        self.rightSpacing = []
        self.wrongSpacing = [.75, .12, .78, .12, .81,
                             .12, .84, .12, .87, .12, .9, .12, .93, .12]
        self.homeSpacing = [.3, .3, .2, .12, .3, .2]
        self.words = []
        self.wrongGuesses = []
        self.rightGuesses = []
        self.selectedWord = ""
        self.center = "center"
        self.gameStatus = ""
        self.guess = tk.StringVar()
        self.houseInfo = tk.StringVar()
        self.duplicate = False

        self.One = let.chosenLetter(tk, "asterick")
        self.Two = let.chosenLetter(tk, "asterick")
        self.Three = let.chosenLetter(tk, "asterick")
        self.Four = let.chosenLetter(tk, "asterick")
        self.Five = let.chosenLetter(tk, "asterick")
        self.Six = let.chosenLetter(tk, "asterick")
        self.Seven = let.chosenLetter(tk, "asterick")
        self.Eight = let.chosenLetter(tk, "asterick")

    def windowAccessories(self):
        self.window.geometry("800x600")
        self.window.config()
        self.window.title("HANGMAN: HOUSE EDITION")
        self.center()

    def center(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        frm_width = self.window.winfo_rootx() - self.window.winfo_x()
        win_width = width + 2 * frm_width
        height = self.window.winfo_height()
        titlebar_height = self.window.winfo_rooty() - self.window.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.window.winfo_screenwidth() // 2 - win_width // 2
        y = self.window.winfo_screenheight() // 2 - win_height // 2
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.deiconify()

    def windowWidgets(self):
        option = tk.Label(self.window, text="PICK A LETTER:",
                          font=("Arial", 18, "bold"))
        option.place(relx=.5,
                     rely=.6, anchor=self.center)

        guess = tk.Entry(self.window, width=10, font=(
            "Arial", 18, "bold"), textvariable=self.guess)
        guess.place(relx=.45, rely=.67, anchor=self.center)

        confirmation = tk.Button(
            self.window, width=5, height=1, text="Guess", font=("Arial", 12, "bold"), bg="black", fg="white", command=lambda: [self.getGuess(), self.wrongLabels(), self.houseLabels(), self.assessGame()])
        confirmation.place(relx=.6, rely=.67, anchor=self.center)

        self.houseInfo.set("Don't Let The House BURN!!")
        self.house = tk.Label(
            self.window, textvariable=self.houseInfo, font=("Arial", 20, "bold"))
        self.house.place(
            relx=self.homeSpacing[0], rely=self.homeSpacing[1], anchor=self.center)

    def letterLabels(self):
        self.one = tk.Label(self.window, image=self.One)
        self.one.place(relx=self.rightSpacing[0],
                       rely=self.rightSpacing[1], anchor=self.center)

        self.two = tk.Label(self.window, image=self.Two)
        self.two.place(relx=self.rightSpacing[2],
                       rely=self.rightSpacing[3], anchor=self.center)

        self.three = tk.Label(self.window, image=self.Three)
        self.three.place(
            relx=self.rightSpacing[4], rely=self.rightSpacing[5], anchor=self.center)

        self.four = tk.Label(self.window, image=self.Four)
        self.four.place(
            relx=self.rightSpacing[6], rely=self.rightSpacing[7], anchor=self.center)

        if len(self.rightSpacing) >= 10:

            self.five = tk.Label(self.window, image=self.Five)
            self.five.place(
                relx=self.rightSpacing[8], rely=self.rightSpacing[9], anchor=self.center)

        if len(self.rightSpacing) >= 12:

            self.six = tk.Label(self.window, image=self.Six)
            self.six.place(
                relx=self.rightSpacing[10], rely=self.rightSpacing[11], anchor=self.center)

        if len(self.rightSpacing) >= 14:

            self.seven = tk.Label(self.window, image=self.Seven)
            self.seven.place(
                relx=self.rightSpacing[12], rely=self.rightSpacing[13], anchor=self.center)

        if len(self.rightSpacing) >= 16:

            self.eight = tk.Label(self.window, image=self.Eight)
            self.eight.place(
                relx=self.rightSpacing[14], rely=self.rightSpacing[15], anchor=self.center)

    def houseLabels(self):
        if self.duplicate == False:
            if len(self.wrongGuesses) == 1:
                self.houseInfo.set("")
                house = home.chosenHousePiece(tk, "house")
                self.house = tk.Label(self.window, font=(
                    "Arial", 15, "bold"))
                self.house.place(
                    relx=self.homeSpacing[0], rely=self.homeSpacing[1], anchor=self.center)
                self.house.configure(image=house)
                self.house.image = house
            elif len(self.wrongGuesses) == 2:
                roof = home.chosenHousePiece(tk, "roof")
                self.house.configure(image=roof)
                self.house.image = roof
            elif len(self.wrongGuesses) == 3:
                chimney = home.chosenHousePiece(tk, "chimney")
                self.house.configure(image=chimney)
                self.house.image = chimney
            elif len(self.wrongGuesses) == 4:
                door = home.chosenHousePiece(tk, "door")
                self.house.configure(image=door)
                self.house.image = door
            elif len(self.wrongGuesses) == 5:
                window1 = home.chosenHousePiece(tk, "window1")
                self.house.configure(image=window1)
                self.house.image = window1
            elif len(self.wrongGuesses) == 6:
                window2 = home.chosenHousePiece(tk, "window2")
                self.house.configure(image=window2)
                self.house.image = window2
            elif len(self.wrongGuesses) == 7:
                fire = home.chosenHousePiece(tk, "fire")
                self.house.configure(image=fire)
                self.house.image = fire
        else:
            pass

    def wrongLabels(self):
        if self.duplicate == False:
            try:
                missingLabel = tk.Label(
                    self.window, text="Wrong Letters", font=("Arial", 15, "bold"))
                missingLabel.place(relx=.75, rely=.05)

                self.missOne = tk.Label(
                    self.window, font=("Arial", 15, "bold"))
                self.missOne.place(
                    relx=self.wrongSpacing[0], rely=self.wrongSpacing[1], anchor=self.center)
                self.missOne.configure(text=self.wrongGuesses[0])
                self.missOne.image = self.wrongGuesses[0]

                self.missTwo = tk.Label(
                    self.window, font=("Arial", 15, "bold"))
                self.missTwo.place(
                    relx=self.wrongSpacing[2], rely=self.wrongSpacing[3], anchor=self.center)
                self.missTwo.configure(text=self.wrongGuesses[1])
                self.missTwo.image = self.wrongGuesses[1]

                self.missThree = tk.Label(
                    self.window, font=("Arial", 15, "bold"))
                self.missThree.place(
                    relx=self.wrongSpacing[4], rely=self.wrongSpacing[5], anchor=self.center)
                self.missThree.configure(text=self.wrongGuesses[2])
                self.missThree.image = self.wrongGuesses[2]

                self.missFour = tk.Label(
                    self.window, font=("Arial", 15, "bold"))
                self.missFour.place(
                    relx=self.wrongSpacing[6], rely=self.wrongSpacing[7], anchor=self.center)
                self.missFour.configure(text=self.wrongGuesses[3])
                self.missFour.image = self.wrongGuesses[3]

                self.missFive = tk.Label(
                    self.window, font=("Arial", 15, "bold"))
                self.missFive.place(
                    relx=self.wrongSpacing[8], rely=self.wrongSpacing[9], anchor=self.center)
                self.missFive.configure(text=self.wrongGuesses[4])
                self.missFive.image = self.wrongGuesses[4]

                self.missSix = tk.Label(
                    self.window, font=("Arial", 15, "bold"))
                self.missSix.place(
                    relx=self.wrongSpacing[10], rely=self.wrongSpacing[11], anchor=self.center)
                self.missSix.configure(text=self.wrongGuesses[5])
                self.missSix.image = self.wrongGuesses[5]

                self.missSeven = tk.Label(
                    self.window, font=("Arial", 15, "bold"))
                self.missSeven.place(
                    relx=self.wrongSpacing[12], rely=self.wrongSpacing[13], anchor=self.center)
                self.missSeven.configure(text=self.wrongGuesses[6])
                self.missSeven.image = self.wrongGuesses[6]

            except:
                pass
        else:
            pass

    def getWords(self):
        with open("words.txt", "r") as wordFile:
            lines = wordFile.readlines()
            for line in lines:
                self.words.append(line.replace("\n", ""))

    def chooseWord(self):
        randNum = randint(0, len(self.words) - 1)

        self.selectedWord = self.words[randNum]

    def getWordLength(self):
        return len(self.selectedWord)

    def rSpacing(self, letterCount):
        if letterCount == 4:
            self.rightSpacing = [.35, .8, .45, .8, .55, .8, .65, .8]
        elif letterCount == 5:
            self.rightSpacing = [.30, .8, .40, .8, .50, .8, .60, .8, .70, .8]
        elif letterCount == 6:
            self.rightSpacing = [.25, .8, .35, .8, .45,
                                 .8, .55, .8, .65, .8, .75, .8]
        elif letterCount == 7:
            self.rightSpacing = [.2, .8, .3, .8, .4, .8, .5,
                                 .8, .6, .8, .7, .8, .8, .8]
        elif letterCount == 8:
            self.rightSpacing = [.15, .8, .25, .8, .35, .8, .45,
                                 .8, .55, .8, .65, .8, .75, .8, .85, .8, .95, .8]

    def getGuess(self):
        found = False
        letterGuess = self.guess.get()
        self.duplicate = self.errorMessage()
        wordSpread = list(self.selectedWord.lower())

        if self.duplicate == False:
            i = 1
            for x in wordSpread:
                if x == letterGuess:
                    found = True
                    self.correctLetterGuess(letterGuess, i)
                    self.rightGuesses.append(x)
                    i += 1
                else:
                    i += 1

            if found == False:
                self.wrongGuesses.append(letterGuess)
            self.guess.set("")
        else:
            pass

    def correctLetterGuess(self, letterGuess, number):
        letter = let.chosenLetter(tk, letterGuess)
        if number == 1:
            self.one.configure(image=letter)
            self.one.image = letter
        if number == 2:
            self.two.configure(image=letter)
            self.two.image = letter
        if number == 3:
            self.three.configure(image=letter)
            self.three.image = letter
        if number == 4:
            self.four.configure(image=letter)
            self.four.image = letter
        try:
            if number == 5:
                self.five.configure(image=letter)
                self.five.image = letter
            if number == 6:
                self.six.configure(image=letter)
                self.six.image = letter
            if number == 7:
                self.seven.configure(image=letter)
                self.seven.image = letter
            if number == 8:
                self.eight.configure(image=letter)
                self.eight.image = letter
        except:
            pass

    def assessGame(self):
        if len(self.wrongGuesses) == 7:
            self.gameStatus = f"You Lose!  The word was {self.selectedWord.upper()}"
            self.playAgain()
        elif len(self.rightGuesses) == len(self.selectedWord):
            self.gameStatus = "Winner Winner!"
            self.playAgain()
        else:
            self.duplicate = False

    def playAgain(self):
        MsgBox = tk.messagebox.askyesno(
            'Play Again', f'{self.gameStatus}.\nDo you want to play again?', icon='question')
        if MsgBox == True:
            self.window.destroy()
            hang = Hangman()
            hang.runGame()

        else:
            self.window.destroy()

    def errorMessage(self):
        guess = self.guess.get()
        if guess == "":
            tk.messagebox.showinfo(
                'Empty Entry', f'A guess is required to proceed!', icon='warning')
            self.guess.set("")
            return True
        elif guess.isdigit():
            tk.messagebox.showinfo(
                'Number Entry', f'Numbers can\'t be used!', icon='warning')
            self.guess.set("")
            return True
        elif len(guess) >= 2:
            tk.messagebox.showinfo(
                'Too Many Letters', f'Enter a single letter!', icon='warning')
            self.guess.set("")
            return True

        for x in self.wrongGuesses:
            if x == guess:
                tk.messagebox.showinfo(
                    'Letter Duplicate', f'You have already guessed this letter', icon='warning')
                self.guess.set("")
                return True

        for x in self.rightGuesses:
            if x == guess:
                tk.messagebox.showinfo(
                    'Letter Duplicate', f'You have already guessed this letter', icon='warning')
                self.guess.set("")
                return True
        return False

    def runGame(self):
        self.getWords()
        self.chooseWord()
        letterCount = self.getWordLength()
        self.rSpacing(letterCount)
        self.letterLabels()
        self.wrongLabels()
        self.windowWidgets()
        self.window.mainloop()


if __name__ == "__main__":
    hang = Hangman()
    hang.runGame()
