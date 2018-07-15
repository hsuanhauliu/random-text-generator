import os
import random

class RandomTextGenerator(object):

    def __init__(self, limit=20):
        self.limit = limit # limit of word counts
        self.brain = {"**": {"**": 0}}
        self.file_flag = True

    def train(self, filename):
        titles = []
        if self.read_file(filename, titles):
            self.file_flag = True
            return

        for title in titles:
            words = title.split() # a list of words in the title
            curr_w = words[0]

            # add start word
            if curr_w in self.brain["**"].keys():
                self.brain["**"][curr_w] += 1
            else:
                self.brain["**"][curr_w] = 1
            self.brain["**"]["**"] += 1

            for i in range(1, len(words)):
                prev_w = words[i-1]
                curr_w = words[i]

                if prev_w not in self.brain.keys():
                    self.brain[prev_w] = {"**": 1, curr_w: 1}
                else:
                    self.brain[prev_w]["**"] += 1

                    if curr_w not in self.brain[prev_w].keys():
                        self.brain[prev_w][curr_w] = 1
                    else:
                        self.brain[prev_w][curr_w] += 1

        self.file_flag = False
        return

    def read_file(self, filename, titles_list):
        if os.path.isfile(filename):
            with open(filename, "r") as rFile:
                for line in rFile:
                    titles_list.append(line.strip("\n"))
            return False
        else:
            print("No such file.")

        return True

    def generate_title(self):
        if self.file_flag:
            print("Can't generate title due to file reading failure.")
            return

        new_title = ""
        curr_w = ""
        word_count = 1

        # find starting word first
        prob = random.randint(1, self.brain["**"]["**"])
        counter = 0

        for w in self.brain["**"].keys():
            if w != "**":
                counter += self.brain["**"][w]
                if prob <= counter:
                    curr_w = w
                    new_title += w
                    break

        while curr_w in self.brain.keys() and word_count < self.limit:
            counter = 0
            word_count += 1
            prob = random.randint(1, self.brain[curr_w]["**"])

            for w in self.brain[curr_w].keys():
                if w != "**":
                    counter += self.brain[curr_w][w]
                    if prob <= counter:
                        curr_w = w
                        new_title += " " + w
                        break

        return new_title

    def generate_multiple(self):
        if self.file_flag:
            print("Can't generate title due to file reading failure.")
            return

        flag = True

        while flag:
            print(self.generate_title())
            print()

            user_input = input(">>> Generate more? [type y for yes]: ")
            if user_input == "y":
                flag = True
            else:
                flag = False
        return
