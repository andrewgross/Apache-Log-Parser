from math import sqrt
from math import pow
import re

def parse(line):
    regex = re.compile("^(?P<ip_address>([0-9]{1,3}\.?){4})\s-\s-\s\[(?P<timestamp>.*?)\]\s\"(?P<method>.*?)\s(?P<request>.*?)\sHTTP\/(?P<http_version>.*?)\"\s(?P<response_code>\d{3})\s(?P<size>.*?)\s\"(?P<referrer>.*?)\"\s\"(?P<client>.*?)\"\s(?P<service_time>.*?)$")    
    r = regex.search(line)
    s = {}
    if r:
        for k, v in r.groupdict().iteritems():
            if v is None or v is "-":
                continue
            s[k] = r.groupdict().pop(k)
    return s    
    # 
    # def std_dev(aggregate_log_object):        
    #     average = calculate_mean_time_to_service(aggregate_log_object)
    #     for tts in aggregate_log_object.aggregate_tts:
    #         delta_tts.append(pow((average - tts), 2))
    #     return sqrt(sum(delta_tts)/len(delta_tts))
    # 
    # def get_max_tts(aggregate_log_object):
    #     sorted_aggregate_tts = sorted(aggregate_log_object.aggregate_tts)
    #     return sorted_aggregate_tts[-1]
    # 
    # def get_min_tts(aggregate_log_object):
    #     sorted_aggregate_tts = sorted(aggregate_log_object.aggregate_tts)
    #     return sorted_aggregate_tts[0]
    






