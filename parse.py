#!/bin/python
from sys import argv
from aggregate_log_object import Aggregate_log_object
from log_object import Log_object

script, input_file = argv

f=open(input_file)

log_objects=[]
aggregate_log_objects_list={}

# Parse the input file, create an object for each line with the field values
for line in f:
    log_line = Log_object(line) 
    log_objects.append(log_line)
    
# For the set of request URLs, compile aggregate data    
for log_item in log_objects:
    if log_item.request_url not in aggregate_log_objects_list:
        alo = Aggregate_log_object(log_item)
        aggregate_log_objects_list[log_item.request_url] = alo
    else:
        aggregate_log_objects_list[log_item.request_url].add_log_object(log_item)

# Printing            
for value in aggregate_log_objects_list.values():
    if len(value.aggregate_tts) is 1:
        continue
    print "URL: %s" % value.request_url
    print "Mean: %.4f" % value.get_average_tts()
    print "STD:  %.4f" % value.get_std_dev_tts()
    count = 0
    last_tts = 0.0    
    for tts in value.sort_aggregate_tts:
        if tts > last_tts:
            print "%s: %s" % (last_tts .*count)            
            count = 1
        else:
            count = count + 1

        
    
    for tts in value.aggregate_tts:
        print tts

     
    




        
        
