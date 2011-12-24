from log_object import Log_object
import unittest


class Log_object_test(unittest.TestCase):
    
    def setUp(self):
        self.raw_data = '192.186.11.123 - - [25/Jul/2011:16:15:03 -0400] "GET /test?first=true&second=false HTTP/1.1" 200 12005 "http://www.example.com/testSubmit?" "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0; T312461; ADR)" 379994'
        self.known_values = (('log_date', '25/Jul/2011:16:15:03 -0400'),
                        ('user_agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.0; T312461; ADR)'),
                        ('request_raw', '/test?first=true&second=false'),
                        ('request_url', '/test'),
                        ('request_query', 'first=true&second=false'),
                        ('http_method', 'GET'),
                        ('http_version', 'HTTP/1.1'),
                        ('http_code', 200),
                        ('referrer', 'http://www.example.com/testSubmit?'),
                        ('response_size', 12005.0),
                        ('time_to_service', float(379994.0)/1000),
                        ('ip_address',  '192.186.11.123') )
                    
    def test_known_values(self):     
        log_item = Log_object(self.raw_data)
        for parameter, parsed_result in self.known_values:
            self.assertEqual(getattr(log_item, parameter), parsed_result)
   
    if __name__ == '__main__':
        unittest.main()             