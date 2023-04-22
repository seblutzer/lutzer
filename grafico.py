import matplotlib.pyplot as plt
import pandas as pd
from .coordenadas import get_word_coordinates


class Word:
    def __init__(self, word):
        self.word = word.upper()
        self.df = get_word_coordinates(self.word)

    def plot(self):
        num_chars = len(self.word)
        width = num_chars * 1.5
        height = 3

        fig = plt.figure(figsize=(width, height))
        ax = fig.add_subplot(111)

        last_idx = {}
        for idx, (letter, group) in enumerate(self.df.groupby('letra')):
            group = group.reset_index(drop=True)
            last_idx[letter] = len(group) - 1
            for i in range(len(group)-1):
                if letter in ('!', '?') and i == last_idx[letter]:
                    continue
                ax.plot([group.loc[i, 'x'], group.loc[i+1, 'x']],
                        [group.loc[i, 'y'], group.loc[i+1, 'y']],
                        color='blue')

        for _, group in self.df.groupby('letra'):
            group = group.reset_index(drop=True)
            ax.scatter(group['x'], group['y'], color='black')

        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])

        plt.show()
