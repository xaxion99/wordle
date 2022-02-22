########################################################################################################################
# Imports
########################################################################################################################
from tkinter import *
from processor import *
import matplotlib.pyplot as plt


class GUI:
    words = []
    letters = []
    letter_counts = []
    letter_percentages = []
    percentage_dict = {}
    slot_frequencies = []
    word_score_dict = {}

    arr_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    slots = ['Slot 1', 'Slot 2', 'Slot 3', 'Slot 4', 'Slot 5']

    def __init__(self, master, w, le, lc, pd, wsd):

        # Setup main window
        self.master = master
        master.title("Letter Frequencies of 5-Letter Words")
        # master.wm_iconbitmap('Icons/logo_large.ico')  # Add logo to top bar
        # master.resizable(height = None, width = None)
        master.resizable(0, 0)  # Make window not resizable (resizing is broken atm)

        self.words = w
        self.letters = le
        self.letter_counts = lc
        self.percentage_dict = pd
        self.word_score_dict = wsd

        # Setup frames containing widget subsets
        self.inputDataFrame = Frame(master, borderwidth=2, relief=SUNKEN)
        # self.inputDataFrame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.inputDataFrame.grid(row=0, column=0, columnspan=2, sticky=E + W, padx=5, pady=5)
        self.inputDataFrame.grid_columnconfigure(0, weight=1)
        self.inputDataFrame.grid_columnconfigure(1, weight=1)

        self.checkLetterFrame = Frame(master, borderwidth=2, relief=SUNKEN)
        # self.checkLetterFrame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.checkLetterFrame.grid(row=1, column=0, sticky=N + S + E + W, padx=5, pady=5)
        self.checkLetterFrame.grid_columnconfigure(0, weight=1)
        self.checkLetterFrame.grid_columnconfigure(1, weight=1)

        self.getScoreFrame = Frame(master, borderwidth=2, relief=SUNKEN)
        # self.getScoreFrame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.getScoreFrame.grid(row=2, column=0, sticky=N + S + E + W, padx=5, pady=5)
        self.getScoreFrame.grid_columnconfigure(0, weight=1)
        self.getScoreFrame.grid_columnconfigure(1, weight=1)

        self.getSecondWordFrame = Frame(master, borderwidth=2, relief=SUNKEN)
        # self.getSecondWordFrame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.getSecondWordFrame.grid(row=1, column=1, sticky=N + S + E + W, padx=5, pady=5)
        self.getSecondWordFrame.grid_columnconfigure(0, weight=1)
        self.getSecondWordFrame.grid_columnconfigure(1, weight=1)

        self.solverFrame = Frame(master, borderwidth=2, relief=SUNKEN)
        # self.solverFrame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.solverFrame.grid(row=2, column=1, sticky=N + S + E + W, padx=5, pady=5)
        self.solverFrame.grid_columnconfigure(0, weight=1)
        self.solverFrame.grid_columnconfigure(1, weight=1)

        self.buttonFrame = Frame(master, borderwidth=2, relief=SUNKEN)
        # self.buttonFrame.pack(fill=BOTH, expand=1, padx=5, pady=5)
        self.buttonFrame.grid(row=3, column=0, columnspan=2, sticky=N + S + E + W, padx=5, pady=5)
        self.buttonFrame.grid_columnconfigure(0, weight=1)
        self.buttonFrame.grid_columnconfigure(1, weight=1)

        # Setup labels
        self.words_label = Label(self.inputDataFrame, text="Number of Words: ", justify="center")
        self.words_count_label = Label(self.inputDataFrame, text=len(self.words), justify="center")
        self.letters_label = Label(self.inputDataFrame, text="Number of Letters: ", justify="center")
        self.letters_count_label = Label(self.inputDataFrame, text=len(self.letters), justify="center")

        self.checkLetter = Label(self.checkLetterFrame, text="Check the Slot Frequency of Inputted Letter",
                                 justify="center")
        self.slot1 = Label(self.checkLetterFrame, text="1: ", justify="center")
        self.slot2 = Label(self.checkLetterFrame, text="2: ", justify="center")
        self.slot3 = Label(self.checkLetterFrame, text="3: ", justify="center")
        self.slot4 = Label(self.checkLetterFrame, text="4: ", justify="center")
        self.slot5 = Label(self.checkLetterFrame, text="5: ", justify="center")
        self.slot1_result = Label(self.checkLetterFrame, text="0", justify="center")
        self.slot2_result = Label(self.checkLetterFrame, text="0", justify="center")
        self.slot3_result = Label(self.checkLetterFrame, text="0", justify="center")
        self.slot4_result = Label(self.checkLetterFrame, text="0", justify="center")
        self.slot5_result = Label(self.checkLetterFrame, text="0", justify="center")
        self.slot1_percentage = Label(self.checkLetterFrame, text="0%", justify="center")
        self.slot2_percentage = Label(self.checkLetterFrame, text="0%", justify="center")
        self.slot3_percentage = Label(self.checkLetterFrame, text="0%", justify="center")
        self.slot4_percentage = Label(self.checkLetterFrame, text="0%", justify="center")
        self.slot5_percentage = Label(self.checkLetterFrame, text="0%", justify="center")
        self.total_label = Label(self.checkLetterFrame, text="Total: ", justify="center")
        self.total_results = Label(self.checkLetterFrame, text="0", justify="center")
        self.total_percentage = Label(self.checkLetterFrame, text="0%", justify="center")
        self.letter_choice = Label(self.checkLetterFrame, text="Choose a letter: ", justify="center")

        self.getScore = Label(self.getScoreFrame, text="Check the Score of a Word", justify="center")
        self.word_label = Label(self.getScoreFrame, text="XXXXX", justify="center")
        self.word_score = Label(self.getScoreFrame, text="125", justify="center")
        self.word_choice = Label(self.getScoreFrame, text="Choose a word: ", justify="center")

        self.getSecondWord = Label(self.getSecondWordFrame, text="Get the Five Lowest Scoring Word that Shares No "
                                                                 "Letters", justify="center")
        self.second_word_label1 = Label(self.getSecondWordFrame, text="XXXXX", justify="center")
        self.second_word_score1 = Label(self.getSecondWordFrame, text="125", justify="center")
        self.second_word_label2 = Label(self.getSecondWordFrame, text="XXXXX", justify="center")
        self.second_word_score2 = Label(self.getSecondWordFrame, text="125", justify="center")
        self.second_word_label3 = Label(self.getSecondWordFrame, text="XXXXX", justify="center")
        self.second_word_score3 = Label(self.getSecondWordFrame, text="125", justify="center")
        self.second_word_label4 = Label(self.getSecondWordFrame, text="XXXXX", justify="center")
        self.second_word_score4 = Label(self.getSecondWordFrame, text="125", justify="center")
        self.second_word_label5 = Label(self.getSecondWordFrame, text="XXXXX", justify="center")
        self.second_word_score5 = Label(self.getSecondWordFrame, text="125", justify="center")
        self.second_word_label6 = Label(self.getSecondWordFrame, text="XXXXX", justify="center")
        self.second_word_score6 = Label(self.getSecondWordFrame, text="125", justify="center")
        self.first_word_choice = Label(self.getSecondWordFrame, text="Choose a word: ", justify="center")

        self.solver_label = Label(self.solverFrame, text="Retrieves List of Possible Words Left", justify="center")
        self.solver_guess1 = Label(self.solverFrame, text="First Guess: ", justify="center")
        self.solver_guess2 = Label(self.solverFrame, text="Second Guess: ", justify="center")
        self.solver_guess3 = Label(self.solverFrame, text="Third Guess: ", justify="center")
        self.solver_guess4 = Label(self.solverFrame, text="Fourth Guess: ", justify="center")
        self.solver_guess5 = Label(self.solverFrame, text="Fifth Guess: ", justify="center")

        # Setup entries
        self.letter_input = Entry(self.checkLetterFrame, justify="center")

        self.word_input = Entry(self.getScoreFrame, justify="center")

        self.first_word_input = Entry(self.getSecondWordFrame, justify="center")

        self.solver_word1 = Entry(self.solverFrame, justify="center")
        self.solver_word2 = Entry(self.solverFrame, justify="center")
        self.solver_word3 = Entry(self.solverFrame, justify="center")
        self.solver_word4 = Entry(self.solverFrame, justify="center")
        self.solver_word5 = Entry(self.solverFrame, justify="center")
        self.solver_info1 = Entry(self.solverFrame, justify="center")
        self.solver_info2 = Entry(self.solverFrame, justify="center")
        self.solver_info3 = Entry(self.solverFrame, justify="center")
        self.solver_info4 = Entry(self.solverFrame, justify="center")
        self.solver_info5 = Entry(self.solverFrame, justify="center")

        # Grid GUI elements
        self.words_label.grid(row=0, column=0, sticky=E + W, padx=5)
        self.words_count_label.grid(row=0, column=1, sticky=E + W, padx=5)
        self.letters_label.grid(row=1, column=0, sticky=E + W, padx=5)
        self.letters_count_label.grid(row=1, column=1, sticky=E + W, padx=5)

        self.checkLetter.grid(row=0, column=0, columnspan=3, sticky=E + W, padx=5)
        self.slot1.grid(row=1, column=0, sticky=E + W, padx=5)
        self.slot2.grid(row=2, column=0, sticky=E + W, padx=5)
        self.slot3.grid(row=3, column=0, sticky=E + W, padx=5)
        self.slot4.grid(row=4, column=0, sticky=E + W, padx=5)
        self.slot5.grid(row=5, column=0, sticky=E + W, padx=5)
        self.slot1_result.grid(row=1, column=1, sticky=E + W, padx=5)
        self.slot2_result.grid(row=2, column=1, sticky=E + W, padx=5)
        self.slot3_result.grid(row=3, column=1, sticky=E + W, padx=5)
        self.slot4_result.grid(row=4, column=1, sticky=E + W, padx=5)
        self.slot5_result.grid(row=5, column=1, sticky=E + W, padx=5)
        self.slot1_percentage.grid(row=1, column=2, sticky=E + W, padx=5)
        self.slot2_percentage.grid(row=2, column=2, sticky=E + W, padx=5)
        self.slot3_percentage.grid(row=3, column=2, sticky=E + W, padx=5)
        self.slot4_percentage.grid(row=4, column=2, sticky=E + W, padx=5)
        self.slot5_percentage.grid(row=5, column=2, sticky=E + W, padx=5)
        self.total_label.grid(row=6, column=0, sticky=E + W, padx=5)
        self.total_results.grid(row=6, column=1, sticky=E + W, padx=5)
        self.total_percentage.grid(row=6, column=2, sticky=E + W, padx=5)
        self.letter_choice.grid(row=7, column=0, sticky=E + W, padx=5)
        self.letter_input.grid(row=7, column=1, sticky=E + W, padx=5)

        self.getScore.grid(row=0, column=0, columnspan=3, sticky=E + W, padx=5)
        self.word_label.grid(row=1, column=0, sticky=E + W, padx=5)
        self.word_score.grid(row=1, column=1, sticky=E + W, padx=5)
        self.word_choice.grid(row=2, column=0, sticky=E + W, padx=5)
        self.word_input.grid(row=2, column=1, sticky=E + W, padx=5)

        self.getSecondWord.grid(row=0, column=0, columnspan=3, sticky=E + W, padx=5)
        self.second_word_label1.grid(row=1, column=0, sticky=E + W, padx=5)
        self.second_word_score1.grid(row=1, column=1, sticky=E + W, padx=5)
        self.second_word_label2.grid(row=2, column=0, sticky=E + W, padx=5)
        self.second_word_score2.grid(row=2, column=1, sticky=E + W, padx=5)
        self.second_word_label3.grid(row=3, column=0, sticky=E + W, padx=5)
        self.second_word_score3.grid(row=3, column=1, sticky=E + W, padx=5)
        self.second_word_label4.grid(row=4, column=0, sticky=E + W, padx=5)
        self.second_word_score4.grid(row=4, column=1, sticky=E + W, padx=5)
        self.second_word_label5.grid(row=5, column=0, sticky=E + W, padx=5)
        self.second_word_score5.grid(row=5, column=1, sticky=E + W, padx=5)
        self.second_word_label6.grid(row=6, column=0, sticky=E + W, padx=5)
        self.second_word_score6.grid(row=6, column=1, sticky=E + W, padx=5)
        self.first_word_choice.grid(row=7, column=0, sticky=E + W, padx=5)
        self.first_word_input.grid(row=7, column=1, sticky=E + W, padx=5)

        self.solver_label.grid(row=0, column=0, columnspan=3, sticky=E + W, padx=5)
        self.solver_guess1.grid(row=1, column=0, sticky=E + W, padx=5)
        self.solver_guess2.grid(row=2, column=0, sticky=E + W, padx=5)
        self.solver_guess3.grid(row=3, column=0, sticky=E + W, padx=5)
        self.solver_guess4.grid(row=4, column=0, sticky=E + W, padx=5)
        self.solver_guess5.grid(row=5, column=0, sticky=E + W, padx=5)
        self.solver_word1.grid(row=1, column=1, sticky=E + W, padx=5)
        self.solver_word2.grid(row=2, column=1, sticky=E + W, padx=5)
        self.solver_word3.grid(row=3, column=1, sticky=E + W, padx=5)
        self.solver_word4.grid(row=4, column=1, sticky=E + W, padx=5)
        self.solver_word5.grid(row=5, column=1, sticky=E + W, padx=5)
        self.solver_info1.grid(row=1, column=2, sticky=E + W, padx=5)
        self.solver_info2.grid(row=2, column=2, sticky=E + W, padx=5)
        self.solver_info3.grid(row=3, column=2, sticky=E + W, padx=5)
        self.solver_info4.grid(row=4, column=2, sticky=E + W, padx=5)
        self.solver_info5.grid(row=5, column=2, sticky=E + W, padx=5)

        # Setup and grid buttons
        Button(self.checkLetterFrame, text='Check Letter', command=self.check_letter_callback)\
            .grid(row=9, column=0, columnspan=3, pady=5, sticky=E + W)

        Button(self.getScoreFrame, text='Get Word Score', command=self.get_word_score_callback)\
            .grid(row=3, column=0, columnspan=3, pady=5, sticky=E + W)

        Button(self.getSecondWordFrame, text='Get Best Second Word', command=self.get_second_word_callback)\
            .grid(row=8, column=0, columnspan=3, pady=5, sticky=E + W)

        Button(self.solverFrame, text='Generate List of Words Left', command=self.solver_callback) \
            .grid(row=6, column=0, columnspan=3, pady=5, sticky=E + W)

        Button(self.buttonFrame, text='Reset', command=self.reset_callback)\
            .grid(row=0, column=0, columnspan=2, pady=5, sticky=E + W)
        Button(self.buttonFrame, text='Quit', command=self.close_window)\
            .grid(row=1, column=0, columnspan=2, pady=5, sticky=E + W)

    # Function to check the relative frequencies of letters for given slots in the word
    def check_letter_callback(self):
        for char in self.arr_of_letters:
            if self.letter_input.get() == char:
                processor = Processor()
                slot_frequencies = processor.count_letter_slot(self.letters, self.letter_input.get())
                total = slot_frequencies[0] + slot_frequencies[1] + slot_frequencies[2] + slot_frequencies[3] + \
                    slot_frequencies[4]
                percent1 = slot_frequencies[0] / total
                percent2 = slot_frequencies[1] / total
                percent3 = slot_frequencies[2] / total
                percent4 = slot_frequencies[3] / total
                percent5 = slot_frequencies[4] / total
                percent_total = percent1 + percent2 + percent3 + percent4 + percent5
                self.slot1_result.configure(text=slot_frequencies[0])
                self.slot2_result.configure(text=slot_frequencies[1])
                self.slot3_result.configure(text=slot_frequencies[2])
                self.slot4_result.configure(text=slot_frequencies[3])
                self.slot5_result.configure(text=slot_frequencies[4])
                self.slot1_percentage.configure(text="{:.3%}".format(percent1))
                self.slot2_percentage.configure(text="{:.3%}".format(percent2))
                self.slot3_percentage.configure(text="{:.3%}".format(percent3))
                self.slot4_percentage.configure(text="{:.3%}".format(percent4))
                self.slot5_percentage.configure(text="{:.3%}".format(percent5))
                self.total_results.configure(text=total)
                self.total_percentage.configure(text="{:.3%}".format(percent_total))

                values = []
                for val in slot_frequencies:
                    temp = (val / total) * 100
                    values.append(temp)

                plt.figure()
                plt.bar(self.slots, values)
                plt.title('Frequency of Letter in a Given Slot')
                plt.xlabel('Letter')
                plt.ylabel('Percent (%)')
                plt.show(block=False)

    # Function to retrieve the score of a word
    def get_word_score_callback(self):
        for word in self.word_score_dict.keys():
            if self.word_input.get() == word:
                self.word_label.configure(text=word)
                self.word_score.configure(text=self.word_score_dict[word])

    # Function that returns the five best scoring words that don't share any letters with inputted word
    def get_second_word_callback(self):
        w = []
        for word in self.word_score_dict.keys():
            if self.first_word_input.get() == word:
                temp = [char for char in word]

        for word in self.word_score_dict.keys():
            try:
                for index, t in enumerate(temp):
                    if t in word:
                        break
                    elif index == 4:
                        w.append(word)
            except UnboundLocalError:
                print("The input is not a valid 5-letter word.")
                break

        print("Second words that provide the most information...")
        for index, x in enumerate(w):
            if index == 0:
                self.second_word_label1.configure(text=x)
                self.second_word_score1.configure(text=self.word_score_dict[x])
                print(f"{x}: {self.word_score_dict[x]}")
            elif index == 1:
                self.second_word_label2.configure(text=x)
                self.second_word_score2.configure(text=self.word_score_dict[x])
                print(f"{x}: {self.word_score_dict[x]}")
            elif index == 2:
                self.second_word_label3.configure(text=x)
                self.second_word_score3.configure(text=self.word_score_dict[x])
                print(f"{x}: {self.word_score_dict[x]}")
            elif index == 3:
                self.second_word_label4.configure(text=x)
                self.second_word_score4.configure(text=self.word_score_dict[x])
                print(f"{x}: {self.word_score_dict[x]}")
            elif index == 4:
                self.second_word_label5.configure(text=x)
                self.second_word_score5.configure(text=self.word_score_dict[x])
                print(f"{x}: {self.word_score_dict[x]}")
            elif index == 5:
                self.second_word_label6.configure(text=x)
                self.second_word_score6.configure(text=self.word_score_dict[x])
                print(f"{x}: {self.word_score_dict[x]}")
            else:
                print(f"{x}: {self.word_score_dict[x]}")
                break

    # Function to attempt to solve Wordle from manual inputs the user receives while playing
    # NOTE: B = Black, G = Green, and Y = Yellow
    def solver_callback(self):
        processor = Processor()
        x = []
        y = []
        z = []

        # First attempt
        word1 = self.solver_word1.get()
        info1 = self.solver_info1.get()
        if len(word1) != 0 or len(info1) != 0:
            if len(word1) == 5:
                temp1 = [char for char in word1]
            if len(info1) == 5:
                temp2 = [char for char in info1]
            x = processor.exclude_b(temp1, temp2, self.word_score_dict.keys())
            y = processor.check_g(temp1, temp2, x)
            z = processor.check_y(temp1, temp2, y)
            z.sort()
            print(z)

        # Second attempt
        word2 = self.solver_word2.get()
        info2 = self.solver_info2.get()
        if len(word2) != 0 or len(info2) != 0:
            if len(word2) == 5:
                temp1 = [char for char in word2]
            if len(info2) == 5:
                temp2 = [char for char in info2]
            x = processor.exclude_b(temp1, temp2, z)
            y = processor.check_g(temp1, temp2, x)
            z = processor.check_y(temp1, temp2, y)
            z.sort()
            print(z)

        # Third attempt
        word3 = self.solver_word3.get()
        info3 = self.solver_info3.get()
        if len(word3) != 0 or len(info3) != 0:
            if len(word3) == 5:
                temp1 = [char for char in word3]
            if len(info3) == 5:
                temp2 = [char for char in info3]
            x = processor.exclude_b(temp1, temp2, z)
            y = processor.check_g(temp1, temp2, x)
            z = processor.check_y(temp1, temp2, y)
            z.sort()
            print(z)

        # Fourth attempt
        word4 = self.solver_word4.get()
        info4 = self.solver_info4.get()
        if len(word4) != 0 or len(info4) != 0:
            if len(word4) == 5:
                temp1 = [char for char in word4]
            if len(info4) == 5:
                temp2 = [char for char in info4]
            x = processor.exclude_b(temp1, temp2, z)
            y = processor.check_g(temp1, temp2, x)
            z = processor.check_y(temp1, temp2, y)
            z.sort()
            print(z)

        # Fifth attempt
        word5 = self.solver_word5.get()
        info5 = self.solver_info5.get()
        if len(word5) != 0 or len(info5) != 0:
            if len(word5) == 5:
                temp1 = [char for char in word5]
            if len(info5) == 5:
                temp2 = [char for char in info5]
            x = processor.exclude_b(temp1, temp2, z)
            y = processor.check_g(temp1, temp2, x)
            z = processor.check_y(temp1, temp2, y)
            z.sort()
            print(z)

    # Function to reset state of program
    def reset_callback(self):
        self.slot1_result.configure(text=0)
        self.slot2_result.configure(text=0)
        self.slot3_result.configure(text=0)
        self.slot4_result.configure(text=0)
        self.slot5_result.configure(text=0)
        self.slot1_percentage.configure(text="0%")
        self.slot2_percentage.configure(text="0%")
        self.slot3_percentage.configure(text="0%")
        self.slot4_percentage.configure(text="0%")
        self.slot5_percentage.configure(text="0%")
        self.total_results.configure(text=0)
        self.total_percentage.configure(text="0%")
        self.letter_input.delete(0, 'end')

        self.word_label.configure(text="XXXXX")
        self.word_score.configure(text="125")
        self.word_input.delete(0, 'end')

        self.second_word_label1.configure(text="XXXXX")
        self.second_word_score1.configure(text="0")
        self.second_word_label2.configure(text="XXXXX")
        self.second_word_score2.configure(text="0")
        self.second_word_label3.configure(text="XXXXX")
        self.second_word_score3.configure(text="0")
        self.second_word_label4.configure(text="XXXXX")
        self.second_word_score4.configure(text="0")
        self.second_word_label5.configure(text="XXXXX")
        self.second_word_score5.configure(text="0")
        self.second_word_label6.configure(text="XXXXX")
        self.second_word_score6.configure(text="0")
        self.first_word_input.delete(0, 'end')

        self.solver_word1.delete(0, 'end')
        self.solver_word2.delete(0, 'end')
        self.solver_word3.delete(0, 'end')
        self.solver_word4.delete(0, 'end')
        self.solver_word5.delete(0, 'end')
        self.solver_info1.delete(0, 'end')
        self.solver_info2.delete(0, 'end')
        self.solver_info3.delete(0, 'end')
        self.solver_info4.delete(0, 'end')
        self.solver_info5.delete(0, 'end')

        print("The program has been reset.")

    # Function to close window on click of Quit button
    def close_window(self):
        self.master.destroy()
        print("The application has been quit.")
