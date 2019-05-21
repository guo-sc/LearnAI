#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

下面的main()函数已经定义好了。它调用你所写的print_words()和print_top()函数功能。 

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

1.如果输入参数 --count ,则调用print_words(filename)函数，计算并输入每个单词在文件中出现的频次：
[单词 出现频次]
word1 count1
word2 count2
...

打印的结果满足以下条件：
 1).按单词的字母表顺序排列。
 2).将所有的单词转换成小写后计数，如：'The' 和 'the' 按同一个单词计算。

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

2. 如果输入参数 --count ,则调用print_top(filename)函数
打印出现频次最高的前20个单词

使用 str.split() (无参数)方法来分割所有的空格符

流程：不要一次性构建整个程序。先得到一个中间结果并运行sys.exit(0)。当它能够正常运行后，再尝试下一个步骤。

参考：定义一个辅助函数来避免在print_words()和print_top()中出现重复代码。

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

# 定义两个函数  print_words(filename) 和 print_top(filename) 
# 你可以编写一个 工具函数 来读取文件、建立并返回一个 单词/数量 的字典
# 然后在 函数 print_words()和print_top() 中调用它。

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    if len(sys.argv) != 3:
        print 'usage: ./wordcount.py {--count | --topcount} file'
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print 'unknown option: ' + option
        sys.exit(1)

if __name__ == '__main__':
    main()
