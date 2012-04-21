from socket import socket, AF_INET, SOCK_DGRAM
data = 'UDP Data Content'
port = 26900
hostname = '192.168.1.102'


def statsd_timer(stat, time):
    time = float(time)*1000 # Convert from s to ms
    data = "{0}:{1}|ms".format(stat, time)
    #udp = socket(AF_INET,SOCK_DGRAM)
    #udp.sendto(data, (hostname, port))
    print data