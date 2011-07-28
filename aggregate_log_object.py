from math import sqrt
from aggregate_functions import *

class Aggregate_log_object:
    
    def __init__(self, log_object):
        
        self.request_url = ""
        self.std_dev_tts = 0.0
        self.average_tts = 0.0
        self.aggregate_tts = []
        self.request_url = log_object.request_url
        self.aggregate_tts.append(log_object.time_to_service)
        
    def add_log_object(self, log_object):    
        self.aggregate_tts.append(log_object.time_to_service)

    def get_average_tts(self):
        self.average_tts = calculate_mean_time_to_service(self.aggregate_tts)
        return self.average_tts

    def get_std_dev_tts(self):
        self.std_dev_tts = calculate_std_dev_time_to_service(self.aggregate_tts)
        return self.std_dev_tts
    
        

        
    