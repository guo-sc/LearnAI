
# coding: utf-8

# In[1]:


import random
import sys


def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  # LAB(begin solution)
  mimic_dict = {}
  f = open(filename, 'r')
  text = f.read()
  f.close()
  words = text.split()
  prev = ''
  for word in words:
    try:
      mimic_dict[prev].append(word)
    except Exception as e:
      mimic_dict[prev] = [word]
    # Could write as: mimic_dict[prev] = mimic_dict.get(prev, []) + [word]
    # It's one line, but not totally satisfying.
  return mimic_dict


def print_mimic(mimic_dict, word):
  """Given mimic dict and start word, prints 200 random words."""
  for unused_i in range(200):
    print (word),
    nexts = mimic_dict.get(word)          # Returns None if not found
    if not nexts:
      nexts = mimic_dict['']  # Fallback to '' if not found
    word = random.choice(nexts)


# In[2]:




