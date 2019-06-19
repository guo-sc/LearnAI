#!/usr/bin/env python3
import sys

from read_inputs import read_inputs

def main():    
    current_key = None
    sum_operate_count = 0
    deal_sum = 0
    lines = read_inputs(sys.stdin)
    for classid, date, count in lines:
        try:
            count = int(count)
        except ValueError:
            continue
        if current_key == (classid, date):
            deal_sum += count
            sum_operate_count += 1
        else:
            if current_key:
                print("{}\t{}\t{}".format(current_key[0], current_key[1], deal_sum*1.0/sum_operate_count))
            current_key = (classid, date)
            deal_sum = count
            sum_operate_count = 1
    if current_key:
        print("{}\t{}\t{}".format(current_key[0], current_key[1], deal_sum*1.0/sum_operate_count))

if __name__ == "__main__":    
    main()