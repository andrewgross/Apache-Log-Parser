from socket import socket, AF_INET, SOCK_DGRAM
#  s = StatsD('127.0.0.1', '1234', debug=True)
# class StatsD(object):
#     def __init__(self, host, port, debug=False):
#         self.hostname = host
#         self.port = int(port)
#         if debug:
#             self.debug = debug

debug = True
hostname = "127.0.0.1"
port = 1234

def statsd_timer(stat, time):
    time = float(time)*1000 # Convert from s to ms
    data = "{0}:{1}|ms".format(stat, time)
    udp = socket(AF_INET,SOCK_DGRAM)
    udp.sendto(data, (hostname, port))
    if debug:
        print data