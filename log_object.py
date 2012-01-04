import re

    def parse(self, line):
        regex = re.compile("^(?P<ip_address>([0-9]{1,3}\.?){4})\s-\s-\s\[(?P<timestamp>.*?)\]\s\"(?P<method>.*?)\s(?P<request>.*?)\sHTTP\/(?P<http_version>.*?)\"\s(?P<response_code>\d{3})\s(?P<size>.*?)\s\"(?P<referrer>.*?)\"\s\"(?P<client>.*?)\"\s(?P<service_time>.*?)$")    
        r = regex.search(line)
        for k, v in r.groupdict().iteritems():
                if v is "-" or None:
                    del r.groupdict()[k]
