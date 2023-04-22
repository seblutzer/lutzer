import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def get_coordinates(char):
    coordinates = []
    if char == 'A':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (2,5), (3,4), (3,3), (3,2), (3,1), (3,3), (2,3), (1,3)]
    elif char == 'B':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (2,5), (3,4), (2,3), (1,3), (2,3), (3,2), (2,1), (1,1)]
    elif char == 'C':
        coordinates = [(3,1), (2,1), (1,2), (1,3), (1,4), (2,5), (3,5)]
    elif char == 'D':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (2,5), (3,4), (3,3), (3,2), (2,1), (1,1)]
    elif char == 'E':
        coordinates = [(3,1), (2,1), (1,1), (1,2), (1,3), (2,3), (1,3), (1,4), (1,5), (2,5), (3,5)]
    elif char == 'F':
        coordinates = [(1,1), (1,2), (1,3), (2,3), (1,3), (1,4), (1,5), (2,5), (3,5)]
    elif char == 'G':
        coordinates = [(2,3), (3,3), (3,2), (3,1), (2,1), (1,2), (1,3), (1,4), (2,5), (3,5)]
    elif char == 'H':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,3), (2,3), (3,3), (3,4), (3,5), (3,2), (3,1)]
    elif char == 'I':
        coordinates = [(2,1), (2,2), (2,3), (2,4), (2,5)]
    elif char == 'J':
        coordinates = [(1,3), (1,2), (2,1), (3,2), (3,3), (3,4), (3,5)]
    elif char == 'K':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (1,3), (2,4), (3,5), (1,3), (2,2), (3,1)]
    elif char == 'L':
        coordinates = [(3,1), (2,1), (1,1), (1,2), (1,3), (1,4), (1,5)]
    elif char == 'M':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (2,2), (3,5), (3,4), (3,3), (3,2), (3,1)]
    elif char == 'N':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (2,3), (3,1), (3,2), (3,3), (3,4), (3,5)]
    elif char == 'O':
        coordinates = [(3,2), (2,1), (1,2), (1,3), (1,4), (2,5), (3,4), (3,3), (3,2)]
    elif char == 'P':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (2,5), (3,4), (2,3), (1,3)]
    elif char == 'Q':
        coordinates = [(2,3), (3,2), (2,1), (1,2), (1,3), (1,4), (2,5), (3,4), (3,3), (3,2), (3,1)]
    elif char == 'R':
        coordinates = [(1,1), (1,2), (1,3), (1,4), (1,5), (2,5), (3,4), (2,3), (1,3), (2,3), (3,1)]
    elif char == 'S':
        coordinates = [(1,1), (2,1), (3,2), (2,3), (1,4), (2,5), (3,5)]
    elif char == 'T':
        coordinates = [(2,1), (2,2), (2,3), (2,4), (2,5), (1,5), (3,5)]
    elif char == 'U':
        coordinates = [(3,5), (3,4), (3,3), (3,2), (2,1), (1,2), (1,3), (1,4), (1,5)]
    elif char == 'V':
        coordinates = [(3,5), (2,1), (1,5)]
    elif char == 'W':
        coordinates = [(1,5), (1,4), (1,3), (1,2), (1,1), (2,4), (3,1), (3,2), (3,3), (3,4), (3,5)]
    elif char == 'X':
        coordinates = [(1,1), (2,3), (3,5), (2,3), (1,5), (3,1)]
    elif char == 'Y':
        coordinates = [(2,1), (2,3), (3,5), (2,3), (1,5)]
    elif char == 'Z':
        coordinates = [(3,1), (2,1), (1,1), (2,3), (3,5), (2,5), (1,5)]
    elif char == '0':
        coordinates = [(3,2), (2,1), (1,2), (1,3), (1,4), (2,5), (3,4), (3,3), (3,2)]
    elif char == '1':
        coordinates = [(2,1), (2,2), (2,3), (2,4), (2,5), (1,4)]
    elif char == '2':
        coordinates = [(3,1), (2,1), (1,2), (2,3), (3,4), (2,5), (1,5)]
    elif char == '3':
        coordinates = [(1,1), (2,1), (3,1), (3,2), (3,3), (2,3), (3,3), (3,4), (3,5), (2,5), (1,5)]
    elif char == '4':
        coordinates = [(3,1), (3,2), (3,3), (3,4), (3,5), (1,3), (2,3), (3,3)]
    elif char == '5':
        coordinates = [(1,1), (2,1), (3,2), (2,3), (1,3), (1,4), (1,5), (2,5), (3,5)]
    elif char == '6':
        coordinates = [(1,2), (2,3), (3,2), (2,1), (1,2), (1,3), (1,4), (2,5), (3,5)]
    elif char == '7':
        coordinates = [(1,1), (2,3), (3,5), (2,5), (1,5)]
    elif char == '8':
        coordinates = [(3,2), (2,1), (1,2), (2,3), (1,4), (2,5), (3,4), (2,3), (3,2)]
    elif char == '9':
        coordinates = [(1,1), (2,1), (3,2), (3,3), (3,4), (2,5), (1,4), (2,3), (3,3)]
    elif char == '!':
        coordinates = [(2,2), (2,3), (2,4), (2,5)]
    elif char == '?':
        coordinates = [(2,2), (2,3), (3,4), (2,5), (1,4)]
    elif char == '.' or char == ',':
        coordinates = [(2,1)]
    elif char == '-':
        coordinates = [(1,3), (2,3), (3,3)]
    elif char == ' ':
        coordinates = []
    else:
        coordinates = []

    #Return the list of coordinates
    return coordinates

def get_word_coordinates(word):
    word = word.upper()
    coordinates_df = pd.DataFrame(columns=['letra', 'x', 'y'])
    letter_count = {}
    for i, char in enumerate(word):
        if char not in letter_count:
            letter_count[char] = 1
        else:
            letter_count[char] += 1
        coordinates = get_coordinates(char)
        for coord in coordinates:
            x = coord[0] + i*4
            y = coord[1]
            if letter_count[char] > 1:
                new_row = {'letra': f"{char}{letter_count[char]}", 'x': x, 'y': y}
            else:
                new_row = {'letra': char, 'x': x, 'y': y}
            coordinates_df = pd.concat([coordinates_df, pd.DataFrame(new_row,index=[0])],ignore_index=True)
    return coordinates_df
