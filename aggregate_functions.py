from math import sqrt
from math import pow

#class Aggregate_functions:
    
    # Expects all of the tts in a list
def calculate_mean_time_to_service(aggregate_tts):
    return sum(aggregate_tts)/len(aggregate_tts)
        
def calculate_std_dev_time_to_service(aggregate_tts):        
    average = calculate_mean_time_to_service(aggregate_tts)
        
    delta_tts = []
    for tts in aggregate_tts:
        delta_tts.append(pow((average - tts), 2))
        
    return sqrt(sum(delta_tts)/len(delta_tts))
        
                
        
        
    
     