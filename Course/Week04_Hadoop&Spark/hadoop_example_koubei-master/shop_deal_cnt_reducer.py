#!/usr/bin/env python3
import sys
import re
from read_inputs import read_inputs

def main():    
    current_key = None
    pay_count = 0
    lines = read_inputs(sys.stdin)
    for words in lines:
        shop, date, count = words
        try:
            count = int(count)
        except ValueError:
            continue
        # print(current_key)
        if current_key == (shop, date):
            pay_count += count
        else:
            if current_key:
                print("{}\t{}\t{}".format(current_key[0], current_key[1], pay_count))
            current_key = (shop, date)
            pay_count = count
    if current_key:
        print("{}\t{}\t{}".format(current_key[0], current_key[1], pay_count))

if __name__ == "__main__":    
    main()