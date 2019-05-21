#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

# 输入一个数字列表
# 将所有相邻且相同的元素去重保留一个元素后返回
# 例如：输入[1, 2, 2, 3] 返回 [1, 2, 3]
#       输入[1, 1, 2, 2, 3, 3, 3] 返回 [1, 2, 3]
# 新建一个列表 或者 修改原来的列表返回均可。
def remove_adjacent(nums):
    # +++your code here+++
    return


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

# 给定两个按递增顺序排序的列表
# 创建并返回一个合并的
# 按排序排列的所有元素的列表。
# 你可以修改传入的列表。
# 理想情况下，解决方案应该在“线性”时间内工作，使两个列表都可以一次完成。
def linear_merge(list1, list2):
    # +++your code here+++
    return

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.

# 注：上述解决方法不是严格的线性时间的，
# 由于python中list.pop(0)不保证在恒定的时间内完成。
# 另一种方法使用list.pop(-1)取出并删除末端的元素，
# 这样生成的每个列表都是倒序的，需要用reversed()将结果排序，
# 这是一个解线性时间的解，但代码显得丑陋些。 

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
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
         ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
         ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
    main()
