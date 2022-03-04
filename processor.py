########################################################################################################################
# Imports
########################################################################################################################
import csv
import numpy as np
from datetime import datetime


class Processor:
    ####################################################################################################################
    # Variables
    ####################################################################################################################
    responses = []

    ####################################################################################################################
    # Methods
    ####################################################################################################################
    def load_csv(self, file_path):
        w = []
        csv_file = open(file_path)
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            for col in row:
                w.append(col)
                line_count += 1
        print(f'Processed {line_count} words.')
        return w

    def parse_letters(self, w):
        chars = []
        letter_count = 0
        for col in w:
            temp = [char for char in col]
            chars = np.concatenate((chars, temp))
            letter_count += 5
        print(f'Processed {letter_count} letters.')
        return chars

    def count_letters(self, chars, alphabet):
        char_count = 0
        array = []
        for char in alphabet:
            for i in chars:
                if i == char:
                    char_count += 1
            array.append(char_count)
            char_count = 0
        # print(f'Processed {char_count} lines.')
        return array

    def count_letter_slot(self, chars, char):
        char_count = 0
        slot = 0
        array = []
        while slot < 5:
            for index, i in enumerate(chars):
                if i == char:
                    if index % 5 == slot:
                        char_count += 1
            array.append(char_count)
            char_count = 0
            slot += 1
        # print(f'Processed {char_count} lines.')
        return array

    def count_all_letter_slot(self, chars, alphabet):
        char_count = 0
        slot = 0
        array = []
        s1_array = []
        s2_array = []
        s3_array = []
        s4_array = []
        s5_array = []
        for char in alphabet:
            while slot < 5:
                for index, i in enumerate(chars):
                    if i == char:
                        if index % 5 == slot:
                            char_count += 1
                if slot == 0:
                    s1_array.append(char_count)
                elif slot == 1:
                    s2_array.append(char_count)
                elif slot == 2:
                    s3_array.append(char_count)
                elif slot == 3:
                    s4_array.append(char_count)
                elif slot == 4:
                    s5_array.append(char_count)
                char_count = 0
                slot += 1
            slot = 0
        array.append(s1_array)
        array.append(s2_array)
        array.append(s3_array)
        array.append(s4_array)
        array.append(s5_array)
        return array

    def weigh_words(self, letters, w, s_percentages):
        scores = []
        for index, letter in enumerate(letters):
            if index % 5 == 0:
                score = 0
                slot1_dict = self.sorter(s_percentages[0])
                for i, sp in enumerate(slot1_dict.keys()):
                    if letter == sp:
                        score += i
            elif index % 5 == 1:
                slot2_dict = self.sorter(s_percentages[1])
                for i, sp in enumerate(slot2_dict.keys()):
                    if letter == sp:
                        score += i
            elif index % 5 == 2:
                slot3_dict = self.sorter(s_percentages[2])
                for i, sp in enumerate(slot3_dict.keys()):
                    if letter == sp:
                        score += i
            elif index % 5 == 3:
                slot4_dict = self.sorter(s_percentages[3])
                for i, sp in enumerate(slot4_dict.keys()):
                    if letter == sp:
                        score += i
            elif index % 5 == 4:
                slot5_dict = self.sorter(s_percentages[4])
                for i, sp in enumerate(slot5_dict.keys()):
                    if letter == sp:
                        score += i
                        scores.append(score)

        # Make word score dictionary and sort it from greatest score to least score
        word_score_dict = {w[i]: scores[i] for i in range(len(w))}
        word_score_dict = self.sorter(word_score_dict, False)
        return word_score_dict

    def exclude_b(self, t1, t2, x):
        array = []
        if "B" in t2:
            for word in x:
                for index, t in enumerate(t1):
                    if t in word and t2[index] == "B":
                        break
                    elif index == 4:
                        array.append(word)
        else:
            array = x
        return array

    def check_g(self, t1, t2, x):
        array = []
        if "G" in t2:
            gs = [g for g in t2]
            count_gs = 0
            for a in gs:
                if a == "G":
                    count_gs += 1
            for word in x:
                temp = [char for char in word]
                count = 0
                for index, t in enumerate(t1):
                    if t2[index] == "G" and t == temp[index]:
                        count += 1
                        if count == count_gs:
                            array.append(word)
        else:
            array = x
        return array

    def check_y(self, t1, t2, x):
        array = []
        if "Y" in t2:
            ys = [y for y in t2]
            count_ys = 0
            for a in ys:
                if a == "Y":
                    count_ys += 1
            for word in x:
                temp = [char for char in word]
                count = 0
                for index, t in enumerate(t1):
                    if t2[index] == "Y" and t in temp and t != temp[index]:
                        count += 1
                        if count == count_ys:
                            array.append(word)
        else:
            array = x
        return array

    def sorter(self, l_percentages, r=True):
        l_percentages = {k: v for k, v in sorted(l_percentages.items(), key=lambda item: item[1], reverse=r)}
        return l_percentages

    # Function to create all Wordle input response permutations
    def create_all_responses(self):
        colors = ['B', 'Y', 'G']
        for a in colors:
            for b in colors:
                for c in colors:
                    for d in colors:
                        for e in colors:
                            string = a + b + c + d + e
                            self.responses.append(string)
        print(f'Processed {len(self.responses)} responses.')

    ####################################################################################################################
    # Function to check a given word against all possible responses
    # N.B. This function will take quite some time to fully run through large amounts of words
    ####################################################################################################################
    def word_checker_callback(self, wsd, w):
        start_time = datetime.now()
        # array_of_dicts = []
        limited_array = []
        array_of_averages = []
        count = 0
        total = 0
        for index, word in enumerate(w):
            # if index < 100:
            if 12000 <= index < 12478:  # 1000 takes about 1 hour to process
                limited_array.append(word)
                for r in self.responses:
                    info = r
                    temp1 = [char for char in word]
                    temp2 = [char for char in info]
                    x = self.exclude_b(temp1, temp2, wsd.keys())
                    y = self.check_g(temp1, temp2, x)
                    z = self.check_y(temp1, temp2, y)
                    if len(z) > 0:
                        count += 1
                        total += len(z)
                # dictionary = {self.responses[i]: array[i] for i in range(len(self.responses))}
                # array_of_dicts.append(dictionary)
                average = total / count
                array_of_averages.append(average)
                count = 0
                total = 0
        print(array_of_averages)
        # word_averages_dict = {limited_array[i]: array_of_averages[i] for i in range(len(limited_array))}
        # print(word_averages_dict)
        print(datetime.now() - start_time)
