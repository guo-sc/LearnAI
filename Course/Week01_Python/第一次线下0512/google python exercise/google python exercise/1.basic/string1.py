#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in string2.py.

# 基础的[字符串][string]练习
# 在下面的函数中填写代码。
# 在main函数中，已经写好了对每个函数不同输入的调用，
# 当函数代码编写正确时，将打印'OK'
# 每个函数的初始代码包含一个 'return'[返回]
# 它只是代码的占位符，你需要用你的实际代码替换它们。

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'

# 输入一个整数(表示圆环的数量)，返回一个字符串，格式如下：
# 'Number of donuts: <count>'，其中 <count> 是传入的参数。
# 但是，如果<count>值大等于10，则使用“many”代替实际的数值
# 所以：输入 donuts(5)  返回 'Number of donuts: 5'
#       输入 donuts(23) 返回 'Number of donuts: many'
def donuts(count):
    # +++your code here+++
    return

# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
# 输入一个字符串 s， 返回 
# 由字符串的最前面两个字母和最后两个字母组成的字符串。
# 例如： 'spring' 返回 'spng'， 'is' 返回 'is'
# 当输入的字符串长度小于2时，返回空字符串
def both_ends(s):
    # +++your code here+++
    return

# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.

# 输入一个字符串s， 返回满足以下条件的字符串
# 1.找出与字符串的第一个字母相同的字母，把它们替换成 '*'，除了第一个字母本身以外
# 例如: 输入'babble'， 返回 'ba**le'
# 提示：使用 s.replace(stra, strb) 函数，可以将字符串 s 中的所有 子字符串stra 替换为 子字符串strb
def fix_start(s):
    # +++your code here+++
    return


# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.

# 输入字符串 a 和 b， 返回添加以下条件的字符串
# 1.使用空格把两个字符串分隔后合并成一个字符串
# 2.交换两个字符串的最前面的两个字母
# 3.字符串 a 和 b 的长度都大等于2
# 例如： 'mix, pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
def mix_up(a, b):
    # +++your code here+++
    return

# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print '%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()
