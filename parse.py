#!/bin/python
from sys import argv
from functions import parse

script, input_file = argv

f=open(input_file)
parsed_log=[]
count = 0

for line in f:
    parsed_log.append(parse(line))
    print len(parsed_log)

f.close()