
# coding: utf-8
from collections import defaultdict
import random
import sys

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  mimic_dict = {}
  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = text.split()
  prev = ''
  while len(words)>0:
    for word in words:
      try:
        mimic_dict[prev].append(word)
      except Exception as e:
        mimic_dict[prev] = [word]
    prev = words[0]
    words.pop(0)
  return mimic_dict

'''
def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  mimic_dict = defaultdict(list)
  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = text.split()
  prev = ''
  while len(words)>0:
    for word in words:
        mimic_dict[prev].append(word)
    prev = words[0]
    words.pop(0)
  return mimic_dict
'''

def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  for unused_i in range(200):
    print(word),
    nexts = mimic_dict.get(word)          # Returns None if not found
    if not nexts:
      nexts = mimic_dict['']  # Fallback to '' if not found
    word = random.choice(nexts)


def main():
    if len(sys.argv) != 2:
        print('usage: ./mimic.py file-to-read')
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print(dict)
    print_mimic(dict, '')


if __name__ == '__main__':
    main()




