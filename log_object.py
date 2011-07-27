#!/usr/bin/python
import re

class Log_object:
    def __init__(self, log_line):
        # Initialize Fields
        self.log_line = log_line
        self.log_date = None
        self.user_agent = None
        self.request_url = None
        self.http_method = None
        self.http_version = None
        self.http_code = None
        self.referrer = None
        self.response_size = None
        self.time_to_service = None
        self.ip_address = None
        # Contruct Data
        self.__parse_ip_address(log_line)
        self.__parse_date(log_line)
        self.__parse_ua_and_tts(log_line)
        self.__parse_request(log_line)
        self.__parse_http_code_size(log_line)
        self.__parse_referrer(log_line)
        
    def __parse_ip_address(self, log_line):
        self.ip_address = re.findall('^(?:[0-9]{1,3}\.){3}[0-9]{1,3}', log_line) 

    def __parse_date(self, log_line):
        request = re.search('- - \[(.*)\] "', log_line)
        self.log_date = request.group(1)
        
    def __parse_ua_and_tts(self, log_line):
        request = re.search('"\s"(.*)"\s(\d{0,10})$', log_line)
        self.user_agent = request.group(1)
        self.time_to_service = request.group(2)
        
    def __parse_request(self, log_line):
        request = re.search('"(GET|POST|HEAD|PUT|DELETE) (.*)\??.* (HTTP/1.\d)"', log_line)
        self.http_method = request.group(1)
        self.request_url = request.group(2)
        self.http_version = request.group(3)
        
    def __parse_http_code_size(self, log_line):
        request = re.search('HTTP/1.\d" (\d{3}|-) (\d*|-) "', log_line)
        self.http_code = request.group(1)
        self.response_size = request.group(2)
        
    def __parse_referrer(self, log_line):
        request = re.search('\d{3} (\d{0,10}|-) "(.*)" "', log_line)
        self.referrer = request.group(2)        
                
        
        
        
        


    