#!/bin/python
from sys import argv
from aggregate_log_object import Aggregate_log_object
from log_object import Log_object
from operator import itemgetter, attrgetter

script, input_file, output_file = argv

f=open(input_file)

log_objects=[]
aggregate_log_objects_list={}
sorted_tts = []

# Parse the input file, create an object for each line with the field values

[ log_objects.append(Log_object(line)) for line in f ]

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

o=open(output_file, 'w')
o.writelines('%s\n' % 'Categories')





# for aggregate_log_object in aggregate_log_objects_list.values():
#     aggregate_log_object.calculate_average_tts()
#     
# s = sorted(aggregate_log_objects_list.values(), key=attrgetter('average_tts'), reverse=True)
#  
# for aggregate_log_object in s: 
#     if "resources" not in aggregate_log_object.request_url:
#         if "operations" not in aggregate_log_object.request_url:
#             if ".pdf" not in aggregate_log_object.request_url:
#                 if aggregate_log_object.average_tts >= 1500:  
#                     o.writelines('%s,%s\n' % (aggregate_log_object.request_url, str(aggregate_log_object.get_average_tts()/1000)))

o.close()



        
        
