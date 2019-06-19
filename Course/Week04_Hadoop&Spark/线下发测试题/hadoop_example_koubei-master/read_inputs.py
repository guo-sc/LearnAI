import re

def read_inputs(file):
    for line in file:
        line = line.strip()
        words = re.split('\t| |,',  line)
        for i in range(len(words) - 1, -1, -1):
            if words[i] == '':
                words.pop(i)
        if len(words) > 1:
            yield words

def read_inputs_fill_nan(file):
    for line in file:
        line = line.strip()
        words = re.split('\t| |,',  line)  #[]
        for i in range(len(words) - 1, -1, -1):
            if words[i] == '':
                words[i] = 'nan'
        if len(words) > 1:
            yield words