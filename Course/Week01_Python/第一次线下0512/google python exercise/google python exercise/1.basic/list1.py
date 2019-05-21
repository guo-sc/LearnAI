#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

#### by andy_linky@qq.com ####

# 基础的[列表][list]练习
# 在下面的函数中填写代码。
# 在main函数中，已经写好了对每个函数不同输入的调用，
# 当函数代码编写正确时，将打印'OK'
# 每个函数的初始代码包含一个 'return'[返回]
# 它只是代码的占位符，你需要用你的实际代码替换它们。

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

# 输入一个字符串列表，
# 返回同时满足以下两个条件的字符串的个数：
# 1.字符串长度大等于2
# 2.字符串的第一个字符等于最后一个字符
# 注：python语言中没有 ++ 操作符，但是有 += 操作符。
def match_ends(words):
    # +++your code here+++
    return


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.

# 输入一个字符串列表，
# 返回满足以下条件的字符串列表：
# 1.按字母顺序从小到大排序
# 2.第一个字母是'x'的字符串排列在最前面
# 例如：输入 ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
#       返回 ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# 提示：可以通过生成两个列表并对它们分别进行排序，然后再把它们连接起来。
def front_x(words):
    # +++your code here+++
    return

# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element from each tuple.

# 输入一个非空的元组列表
# 返回 按列表中元组的最后一个元素从小到大排序后的元组列表
# 例如：输入：[(1, 7), (1, 3), (3, 4, 5), (2, 2)]
#       返回：[(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# 提示：使用自定义键=函数从每个元组提取最后一个元素。
def sort_last(tuples):
    # +++your code here+++
    return


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
         ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
         ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
    main()
