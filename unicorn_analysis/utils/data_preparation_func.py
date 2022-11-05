import numpy as np

def remove_foreign_characters(data):
    values = []

    for value in data:
        without_foreign_characters = value[1: len(value)-1]
        values.append(without_foreign_characters)
    
    return values



def change_value(data, value):
    values = []

    for val in data:
        if val == value:
            values.append(np.nan)
        else:
            values.append(val)
    
    return values



def million_to_billion(data, confirmation):
    billion_values = []

    for i in range(len(data)):
        if confirmation[i][len(confirmation[i])-1] == 'M':
            billion = data[i]/1000
            billion_values.append(billion)
        else:
            billion_values.append(data[i])
    
    return billion_values



def correcting_AI(data):
    correct = []

    for word in data:
        if word == 'Artificial intelligence' or word == 'Artificial Intelligence':
            correcting = word.lower().capitalize()
            correct.append(correcting)
        else:
            correct.append(word)
    
    return correct