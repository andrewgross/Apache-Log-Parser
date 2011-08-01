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

for aggregate_log_object in aggregate_log_objects_list.values():
    print aggregate_log_object.get_average_tts()
    for similar_log_object in aggregate_log_object.get_similar_log_objects():
        print similar_log_object.http_code
        print similar_log_object.log_date
        print similar_log_object.user_agent
        print similar_log_object.request_raw
        print similar_log_object.request_url
        print similar_log_object.request_query
        print similar_log_object.http_method
        print similar_log_object.http_version
        print similar_log_object.http_code
        print similar_log_object.referrer
        print similar_log_object.response_size
        print similar_log_object.time_to_service
        print similar_log_object.ip_address
    




        
        
