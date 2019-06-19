#!/usr/bin/env python3
import sys

from read_inputs import read_inputs

def main():  
    file = sys.stdin
    lines = read_inputs(file)
    # lines = read_inputs(io.TextIOWrapper(sys.stdin.buffer, encoding='gbk'))
    for words in lines:
        # print(words)
        # deal cout table
        if len(words) < 10:
            shopid, date, count = words[0], words[1], words[2]
            print("{}\t{}\t{}\t{}".format(shopid, date, count, 'L'))
        else:
            shopid, classid = words[0], words[-2]
            print(shopid, classid, 'R', sep='\t')
    
if __name__ == "__main__":  
    main()