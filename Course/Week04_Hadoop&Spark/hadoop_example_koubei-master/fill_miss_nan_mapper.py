#!/usr/bin/env python3
import sys

from read_inputs import read_inputs_fill_nan

def main():
    lines = read_inputs_fill_nan(sys.stdin)
    for words in lines:
        print(*words, sep='\t')
    
if __name__ == "__main__":  
    main()