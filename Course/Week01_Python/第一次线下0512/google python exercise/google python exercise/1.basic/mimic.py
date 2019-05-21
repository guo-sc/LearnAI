#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Mimic pyquick exercise -- optional extra exercise.
Google's Python Class

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read
it into one giant string and split it once.

Build a "mimic" dict that maps each word that appears in the file
to a list of all the words that immediately follow that word in the file.
The list of words can be be in any order and should include
duplicates. So for example the key "and" might have the list
["then", "best", "then", "after", ...] listing
all the words which came after "and" in the text.
We'll say that the empty string is what comes before
the first word in the file.

With the mimic dict, it's fairly easy to emit random
text that mimics the original. Print a word, then look
up what words might come next and pick one at random as
the next work.
Use the empty string as the first word to prime things.
If we ever get stuck with a word that is not in the dict,
go back to the empty string to keep things moving.

Note: the standard python module 'random' includes a
random.choice(list) method which picks a random element
from a non-empty list.

For fun, feed your program to itself as input.
Could work on getting it to put in linebreaks around 70
columns, so the output looks better.

"""

"""模仿pyquick练习--可选的额外的练习。

从命令行读取指定的文件。
应用split()函数，使用空白字符串分隔得到文件中所有的单词。
建议一次性读成入整个文件内容，保存到一个大字符串中，然后把它一次性拆分。

创建一个名为 mimic 的字典：
以出现在文件中的单词为键，
文件中所有紧跟在单词后面的一个单词组成的列表为值。
单词列表可以是任意顺序的，也可以包含重复的值。
例如，键“and”可能有列表 
["then", "best", "then", "after", ...]
此列表包括了所有的文件中在'and'后面的单词。
我们约定空字符串是文件中第一个单词之前的字符串。

有了mimic字典，很容易生成随机文本来模仿原来的文件内容。
打印一个单词，然后查找下一个单词可能是什么，然后随机选择一个作为下一个单词。

使用空字符串作为第一个单词。
如果遇到查找的单词不在字典的键中，就回到空字符串，让整个过程能够继续下去。

注意：标准Python模块“random”包含一个random.choice(list)可以用来从非空列表选择随机元素。

为了好玩，把你的程序输入到它自己作为输入。
可以让它把换行符70列，以便输出看起来更好。

"""

import random
import sys


def mimic_dict(filename):
    """Returns mimic dict mapping each word to list of words which follow it."""
    # +++your code here+++
    return


def print_mimic(mimic_dict, word):
    """Given mimic dict and start word, prints 200 random words."""
    # +++your code here+++
    return


# Provided main(), calls mimic_dict() and mimic()
def main():
    if len(sys.argv) != 2:
        print 'usage: ./mimic.py file-to-read'
        sys.exit(1)

    dict = mimic_dict(sys.argv[1])
    print_mimic(dict, '')


if __name__ == '__main__':
    main()
