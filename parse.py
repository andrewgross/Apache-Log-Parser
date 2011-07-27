from sys import argv
from log_object import *

script, input_file = argv

#print "Reading in from %s" % input_file

# Time to service (tts)
#tts = re.compile('\s\d*$')
#http_action= re.compile('\"(GET|POST)\s.*\s(HTTP\/1\.\d)\"')

f=open(input_file)

i=1

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
    
        
# read in each line
# parse for url
# parse for time to server
# save data
# go to next line