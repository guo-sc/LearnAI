#!/usr/bin/env python3
import sys

from read_inputs import read_inputs

def main():
    lines = read_inputs(sys.stdin)
    for words in lines:
        # shop combine deal table
        classid, date, deal_count = words[1], words[2], words[3]
        print(classid, date, deal_count, sep='\t')
    
if __name__ == "__main__":  
    main()