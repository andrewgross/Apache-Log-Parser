from math import sqrt
from aggregate_functions import *

class Aggregate_log_object:
    
    def __init__(self, log_object):
        
        self.request_url = ""
        self.std_dev_tts = 0.0
        self.average_tts = 0.0
        self.similar_log_objects = []
        self.aggregate_tts = []
        self.request_url = log_object.request_url
        self.similar_log_objects.append(log_object)
        self.aggregate_tts.append(log_object.time_to_service)
        
    def add_log_object(self, log_object):    
        self.similar_log_objects.append(log_object)
        self.aggregate_tts.append(log_object.time_to_service)

    def get_similar_log_objects(self):
        return self.similar_log_objects
            
    def get_average_tts(self):
        return calculate_mean_time_to_service(self)

    def get_std_dev_tts(self):
        return calculate_std_dev_time_to_service(self)
        
    def sort_aggregate_tts(self):
        return sorted(self)



    
        

        
    
