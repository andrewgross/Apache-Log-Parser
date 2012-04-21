#!/bin/python
import sys
from functions import parse_nginx
from pprint import pprint

def main(input_files):

    for input_file in input_files:
        f=open(input_file)
        for line in f:
            parsed_line = parse_nginx(line)
            pprint(parsed_line)
        
        f.close()

    
if __name__ == '__main__':
    input_files = sys.argv[1:]
    main(input_files)


