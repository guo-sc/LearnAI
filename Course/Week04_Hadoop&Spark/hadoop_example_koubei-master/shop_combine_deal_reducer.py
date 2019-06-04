#!/usr/bin/env python3
import sys

from read_inputs import read_inputs

def main():    
    current_key = None
    lines = read_inputs(sys.stdin)
    # lines = read_map_outputs(io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'))
    deal_table_left = []
    shop_table_right = []
    for words in lines:
        shopid = words[0]
        if shopid == current_key:
            if 'L' == words[-1]:
                deal_table_left.append(words[:-1])
            else:
                shop_table_right.append(words[:-1])
        else:
            if len(deal_table_left) != 0 and len(shop_table_right) != 0:
                for adeal in deal_table_left:
                    for ashop in shop_table_right:
                        print(ashop[0], *ashop[1:], *adeal[1:], sep='\t', end='\n')

            current_key = words[0]
            deal_table_left.clear()
            shop_table_right.clear()
            if 'L' == words[-1]:
                deal_table_left.append(words[:-1])
            else:
                shop_table_right.append(words[:-1])

    if len(deal_table_left) != 0 and len(shop_table_right) != 0:
        for adeal in deal_table_left:
            for ashop in shop_table_right:
                print(ashop[0], *ashop[1:], *adeal[1:], sep='\t', end='\n')

if __name__ == "__main__":    
    main()