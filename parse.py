#!/bin/python
from sys import argv
from log_object import *

script, input_file = argv

f=open(input_file)

for line in f:
    log_line = Log_object(line)    
    print "IP Address: %s" % log_line.ip_address
    print "Date: %s" % log_line.log_date
    print "User Agent: %s" % log_line.user_agent
    print "Request URL: %s" % log_line.request_url
    print "HTTP Method: %s" % log_line.http_method
    print "HTTP Version: %s" % log_line.http_version
    print "HTTP Response Code: %s" % log_line.http_code
    print "Referrer: %s" % log_line.referrer
    print "Response Size: %s" % log_line.response_size
    print "Time To Service: %s" % log_line.time_to_service
    
        