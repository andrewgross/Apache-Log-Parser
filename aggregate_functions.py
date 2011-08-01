from math import sqrt
from math import pow

    
# Expects all of the tts in a list
def calculate_mean_time_to_service(aggregate_log_object):
    return sum(aggregate_log_object.aggregate_tts)/len(aggregate_log_object.aggregate_tts)
        
def calculate_std_dev_time_to_service(aggregate_log_object):        
    average = calculate_mean_time_to_service(aggregate_log_object)
        
    delta_tts = []
    for tts in aggregate_log_object.aggregate_tts:
        delta_tts.append(pow((average - tts), 2))
        
    return sqrt(sum(delta_tts)/len(delta_tts))

def get_max_tts(aggregate_log_object):
    sorted_aggregate_tts = sorted(aggregate_log_object.aggregate_tts)
    return sorted_aggregate_tts[-1]

def get_min_tts(aggregate_log_object):
    sorted_aggregate_tts = sorted(aggregate_log_object.aggregate_tts)
    return sorted_aggregate_tts[0]
    
        
                
        
        
    
     
