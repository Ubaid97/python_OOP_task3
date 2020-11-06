# This class takes a word, calculates the score by working out how many points each letter is worth, and displays it
class ScoreKeeper:

    def __init__(self, word):
        # takes a word from user input
        self.word = word.upper()

        # score variable set to 0, to be used later in the code
        self.score = 0

        # dictionary with points as keys, and the list of letters worth that many points as their respective values
        self.letters = {
            1: ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"],
            2: ["D", "G"],
            3: ["B", "C", "M", "P"],
            4: ["F", "H", "V", "W", "Y"],
            5: ["K"],
            8: ["J", "X"],
            10: ["Q", "Z"]
        }

    # function that calculates the number of points scored by a word
    def score_count(self):
        # for loop iterating over every character of word passed in by user
        for letter in self.word:
            # nested for loop that iterates over every key and value in the letters dictionary (see line 12)
            for points, letters_list in self.letters.items():
                # nested if statement that checks whether each letter of the word corresponds to a list (value) in the letters dict
                if letter in letters_list:
                    # if the letter is present in one of the lists, score is incremented by the number of points you get for having a letter in that list (see line 12)
                    self.score += points
                    # points corresponds to the keys of the letters dictionary (see lines 12 and 27)
        return self.score

    # a seperate function to display the total score for the word so that the score_keeper function isn't used to perform two different functions
    def display_score(self):
        print(f"Well done, you get {self.score} points for the word '{self.word.capitalize()}'")

