#!/usr/bin/python
import re

class Log_object:
    
    # Initialize Fields
    log_date = "-"
    user_agent = "-"
    request_url = "-"
    http_method = "-"
    http_version = "-"
    http_code = "-"
    referrer = "-"
    response_size = "-"
    time_to_service = "-"
    ip_address = "-"    
    
    def __init__(self, log_line):
        # Contruct Data
        self.__parse_ip_address(log_line)
        self.__parse_date(log_line)
        self.__parse_ua_and_tts(log_line)
        self.__parse_request(log_line)
        self.__parse_http_code_size(log_line)
        self.__parse_referrer(log_line)
        
    def __parse_ip_address(self, log_line):
        self.ip_address = re.findall('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}', log_line) 
        if not self.ip_address:
            self.ip_address = "-"

    def __parse_date(self, log_line):
        request = re.search('- - \[(.*)\] "', log_line)
        if request.group(0):
            self.log_date = request.group(1)      
        
    def __parse_ua_and_tts(self, log_line):
        request = re.search('"\s"(.*)"\s(\d{0,10})$', log_line)
        if request.group(0):
            self.user_agent = request.group(1)      

        if request.group(1):
            self.time_to_service = request.group(2)      
        
    def __parse_request(self, log_line):
        request = re.search('"(GET|POST|HEAD|PUT|DELETE) (.*)\??.* (HTTP/1.\d)"', log_line)
        if request.group(0):
            self.http_method = request.group(1)      
            
        if request.group(1):
            self.request_url = request.group(2)      
            
        if request.group(2):
            self.http_version = request.group(3)      
        
    def __parse_http_code_size(self, log_line):
        request = re.search('HTTP/1.\d" (\d{3}|-) (\d*|-) "', log_line)
        
        if request.group(0):
            self.http_code = request.group(1)      
        
        if request.group(1):
            self.response_size = request.group(2)       
     
    def __parse_referrer(self, log_line):
        request = re.search('\d{3} \d*|- "(.*)" "', log_line)
        if request.group(0):
            self.referrer = request.group(1)        

        
        
        
        


    