
#coding: utf-8
#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    
    for word in words:
        print(word,1)
