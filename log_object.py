import re
from urlparse import urlparse

class Log_object:
    
    # Initialize Fields
    log_date = "-"
    user_agent = "-"
    request_raw = "-"
    request_url = "-"
    request_query = "-"
    http_method = "-"
    http_version = "-"
    http_code = 0
    referrer = "-"
    response_size = 0.0
    time_to_service = 0.0
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
        else: 
            self.ip_address = self.ip_address[0].strip('[]')

    def __parse_date(self, log_line):
        request = re.search('- - \[(.*)\] "', log_line)
        if request.group(0):
            self.log_date = request.group(1)      
     
    # User agent and time to serve request    
    def __parse_ua_and_tts(self, log_line):
        request = re.search('"\s"(.*)"\s(\d*)$', log_line)
        if request.group(0):
            self.user_agent = request.group(1)      

        if request.group(1):
            try:
                self.time_to_service = float(request.group(2))/1000            
            except ValueError:
                self.time_to_service = "-"
                  
    # The url that was requested as well as the parameters passed in    
    def __parse_request(self, log_line):
        request = re.search('"(GET|POST|HEAD|PUT|DELETE) (.*)\??.* (HTTP/1.\d)"', log_line)
        if request.group(0):
            self.http_method = request.group(1)      
            
        if request.group(1):
            self.request_raw = request.group(2)
            self.request_url = urlparse(self.request_raw).path
            self.request_query = urlparse(self.request_raw).query
            
        if request.group(2):
            self.http_version = request.group(3)      
     
    # HTTP Code return as well as the size of the request    
    def __parse_http_code_size(self, log_line):
        request = re.search('HTTP/1.\d" (\d{3}|-) (\d*|-) "', log_line)
        
        if request.group(0):
            try:
                self.http_code = int(request.group(1))            
            except ValueError:
                self.http_code = "-"
     
        
        if request.group(1):
            try:
                self.response_size = float(request.group(2))       
            except ValueError:
                self.response_size = "-"
     
    def __parse_referrer(self, log_line):
        request = re.search('\d{3} .* "(.*)" "', log_line)
        if request.group(0):
            self.referrer = request.group(1)        

        
        
        
        


    