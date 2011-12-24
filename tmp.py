from sys import argv
import re
script, input_file = argv
f=open(input_file)

for line in f:
    regex = re.compile("^(?P<ip_address>([0-9]{1,3}\.?){4})\s-\s-\s\[(?P<timestamp>.*?)\]\s\"(?P<method>.*?)\s(?P<request>.*?)\sHTTP\/(?P<http_version>.*?)\"\s(?P<response_code>\d{3})\s(?P<size>.*?)\s\"(?P<referrer>.*?)\"\s\"(?P<client>.*?)\"\s(?P<service_time>.*?)$")    
    r = regex.search(line)
    if r is not None:
        s = dict([ (k,r.groupdict().get(k)) for k,v in r.groupdict().iteritems() if v is not "-"])

                
