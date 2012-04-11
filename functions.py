import re

def parse(line, regex):
    r = regex.search(line)
    result_set = {}
    if r:
        for k, v in r.groupdict().iteritems():
            if v is None or v is "-":
                continue
            result_set[k] = r.groupdict().pop(k)
    return result_set

def parse_apache_combined(line):
    regex = re.compile("^(?P<ip_address>([0-9]{1,3}\.?){4})\s-\s-\s\[(?P<timestamp>.*?)\]\s\"(?P<method>.*?)\s(?P<request>.*?)\sHTTP\/(?P<http_version>.*?)\"\s(?P<response_code>\d{3})\s(?P<size>.*?)\s\"(?P<referrer>.*?)\"\s\"(?P<client>.*?)\"\s(?P<service_time>.*?)$")    
    return parse(line, regex) 


def parse_nginx(line):
    regex = re.compile("(?P<ip_address>\S*)\s-\s(?P<requesting_user>\S*)\s\[(?P<timestamp>.*?)\]\s\s\"(?P<method>\S*)\s*(?P<request>\S*)\s*(HTTP\/)*(?P<http_version>.*?)\"\s(?P<response_code>\d{3})\s(?P<size>\S*)\s\"(?P<referrer>[^\"]*)\"\s\"(?P<client>[^\"]*)\"\s(?P<service_time>\S*)\s(?P<application_time>\S*)")    
    r = regex.search(line)
    result_set = {}
    if r:
        for k, v in r.groupdict().iteritems():
            if v is None or v is "-":
                continue
            result_set[k] = r.groupdict().pop(k)
    return result_set   




