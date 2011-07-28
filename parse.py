#!/bin/python
from sys import argv
from log_object import Log_object

script, input_file = argv

f=open(input_file)

log_objects={}

for line in f:
    log_line = Log_object(line) 
    log_objects[log_line.request_url] = log_line   

for log_item in log_objects:
    print log_objects[log_item].request_url
        
        