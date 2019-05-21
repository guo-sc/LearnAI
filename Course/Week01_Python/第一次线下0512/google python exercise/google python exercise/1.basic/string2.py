#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises
# 附加的基础字符串练习

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.

# 输入一个字符串，返回满足以下条件的字符串
# 1. 如果字符串长度大等于3，添加 'ing' 到字符串的末尾
# 2. 如果字符串是以 'ing' 结尾的，就在末尾添加 'ly'
# 3. 如果字符串长度小于3，返回原字符串
def verbing(s):
    # +++your code here+++
    return


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!

# 输入一个字符串，返回满足以下条件字符串
# 1.找到字符串中的子串 'not' 和 'bad'
# 2.如果 'bad' 出现在 'not' 后面，就把 'not' ... 'bad' 之间包含的所有字符串替换成 'good'
# 例如：'This dinner is not that bad!' 返回 'This dinner is good!'
def not_bad(s):
    # +++your code here+++
    return


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

# 考虑把一个字符串拆分成两个等分
# 1. 如果字符串长度是偶数，前一半和后一半的长度是相同的
# 2. 如果字符串长度是奇数，则多出的一个字符加到前一半，如：'abcde'，前一半是'abc'，后一半是'de'
# 3. 输入两个字符串, a 和 b,按以下格式返回结果
#  a-front + b-front + a-back + b-back
def front_back(a, b):
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


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print
    print 'not_bad'
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print
    print 'front_back'
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
    main()
