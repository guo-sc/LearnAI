#!/usr/bin/env python3
import sys
import re
import io
from read_inputs import read_inputs

def main():
    lines = read_inputs(sys.stdin)
    for words in lines:
        shop, date, count = words[1], words[2].strip("\"")[:11], 1
        print(shop, date, count, sep='\t')
    
if __name__ == "__main__":  
    main()