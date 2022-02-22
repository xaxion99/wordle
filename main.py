import os
import sys
from gui import *

########################################################################################################################
# Constants / Variables
########################################################################################################################
words = []
letters = []
letter_counts = []
letter_percentages = []
slot_counts = []
slot_percentages = []

arr_of_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']


########################################################################################################################
# Main function for starting Tkinter loop
########################################################################################################################
def main(w, le, lc, pd, wsd):
    root = Tk()
    app = GUI(root, w, le, lc, pd, wsd)
    root.mainloop()


########################################################################################################################
# Main Function
########################################################################################################################
if __name__ == '__main__':
    try:
        wd = sys._MEIPASS
    except AttributeError:
        wd = os.getcwd()
    file_path = os.path.join(wd, 'words.csv')

    # Create a Processor instant to access available class methods
    processor = Processor()

    # Load words from .csv file and then parse the word strings into characters
    words = processor.load_csv(file_path)
    letters = processor.parse_letters(words)

    # Count each letter and determine percentage of total letter represents
    letter_counts = processor.count_letters(letters, arr_of_letters)

    for num in letter_counts:
        percentage = num / letters.size
        letter_percentages.append(percentage)

    percentage_dict = {arr_of_letters[i]: letter_percentages[i] for i in range(len(arr_of_letters))}
    percentage_dict = processor.sorter(percentage_dict)

    values = []
    for val in percentage_dict:
        values.append(percentage_dict[val] * 100)

    # Get the amount of each character at each slot
    slot_counts = processor.count_all_letter_slot(letters, arr_of_letters)

    for slot in slot_counts:
        array = []
        total = 0
        for num in slot:
            total += num
        for index, num in enumerate(slot):
            percentage = num / total
            array.append(percentage)
        slot_percentages.append({arr_of_letters[i]: array[i] for i in range(len(arr_of_letters))})

    # Generate a score for each word and sort them from least (best) to greatest (worst)
    word_score_dict = processor.weigh_words(letters, words, slot_percentages)

    # Graphs
    # Graphs for general frequencies sorted greatest to lease
    plt.subplot(3, 2, 1)
    plt.bar(percentage_dict.keys(), values)
    plt.title('Frequency of Letters in 5-Letter English Words')
    plt.xlabel('Letter')
    plt.ylabel('Percent (%)')
    plt.yticks(np.arange(0, 11, 5))

    # Graph for first slot frequencies
    slot1_dict = processor.sorter(slot_percentages[0])
    values = []
    for val in slot1_dict:
        values.append(slot1_dict[val] * 100)

    plt.subplot(3, 2, 2)
    plt.bar(slot1_dict.keys(), values)
    plt.title('Frequency of Letters in Slot 1')
    plt.xlabel('Letter')
    plt.ylabel('Percent (%)')
    plt.yticks(np.arange(0, 16, 5))

    # Graph for second slot frequencies
    slot2_dict = processor.sorter(slot_percentages[1])
    values = []
    for val in slot2_dict:
        values.append(slot2_dict[val] * 100)

    plt.subplot(3, 2, 3)
    plt.bar(slot2_dict.keys(), values)
    plt.title('Frequency of Letters in Slot 2')
    plt.xlabel('Letter')
    plt.ylabel('Percent (%)')
    plt.yticks(np.arange(0, 21, 5))

    # Graph for third slot frequencies
    slot3_dict = processor.sorter(slot_percentages[2])
    values = []
    for val in slot3_dict:
        values.append(slot3_dict[val] * 100)

    plt.subplot(3, 2, 4)
    plt.bar(slot3_dict.keys(), values)
    plt.title('Frequency of Letters in Slot 3')
    plt.xlabel('Letter')
    plt.ylabel('Percent (%)')
    plt.yticks(np.arange(0, 11, 5))

    # Graph for fourth slot frequencies
    slot4_dict = processor.sorter(slot_percentages[3])
    values = []
    for val in slot4_dict:
        values.append(slot4_dict[val] * 100)

    plt.subplot(3, 2, 5)
    plt.bar(slot4_dict.keys(), values)
    plt.title('Frequency of Letters in Slot 4')
    plt.xlabel('Letter')
    plt.ylabel('Percent (%)')
    plt.yticks(np.arange(0, 21, 5))

    # Graph for fifth slot frequencies
    slot5_dict = processor.sorter(slot_percentages[4])
    values = []
    for val in slot5_dict:
        values.append(slot5_dict[val] * 100)

    plt.subplot(3, 2, 6)
    plt.bar(slot5_dict.keys(), values)
    plt.title('Frequency of Letters in Slot 5')
    plt.xlabel('Letter')
    plt.ylabel('Percent (%)')
    plt.yticks(np.arange(0, 31, 5))

    # Add super title, format subplot layout, and then display all graphs
    plt.suptitle("Slot Frequencies")
    plt.tight_layout()
    plt.show(block=False)

    # Run the main function to start the GUI
    main(words, letters, letter_counts, percentage_dict, word_score_dict)
