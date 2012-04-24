#!/bin/python
import sys, time, os, signal

from functions import parse_nginx
from pprint import pprint
from locations import get_locations
from outputs import statsd_timer

locations = get_locations()

def SigUSR1Handler(signum, frame):
    global log_file
    is_running = False
    log_file.close()
    sys.exit(1)
    return

def set_pid_file():
    f = open('/tmp/log_parser.pid', 'w')
    f.write(str(os.getpid()))
    f.flush()
    f.close()
    signal.signal(signal.SIGUSR1, SigUSR1Handler) # Set up a handler for SigUSR1


def main(input_file):
    global log_file
    global is_running
    is_running = True
    set_pid_file() # Set our pid so that we can rotate properly
    try:
        log_file = open(input_file)
    except IOError:
        print "Unable to open log file"
        time.sleep(1)
        sys.exit(1)

    parsed_log = follow(log_file)

    for line in parsed_log:
        process(line)
            
    log_file.close()

def follow(log_file):
    log_file.seek(0,2) # Go to the end of the file
    while is_running:
        line = log_file.readline()
        if not line:
            time.sleep(0.1) # Sleep
            continue
        yield parse_nginx(line)

def process(line):
    # Plugins
    # Have some way to do trickle through or at least be aware if anything 
    # process matches
    if line.get('path'):
        process_api(line)
        process_ajax(line)
        process_frame(line)
        process_locations(line)
        process_aff_click(line)
        process_business(line)

def process_locations(line):
    if any( True for location in locations if location in line['path'] ):
        send(line, "locations")

def process_frame(line):
    if "/frame/" in line['path']:
        send(line, "frame")

def process_ajax(line):
    if line['path'].startswith('/ajax/'):
        send(line, "ajax")

def process_api(line):
    if line['path'].startswith('/v1/'):
        send(line, "api")

def process_business(line):
    if line['path'].startswith('/business/'):
        send(line, "business")

def process_aff_click(line):
    if line['path'].startswith('/aff/'):
        send(line, 'aff')

def send(line, metric):
    if line.get('service_time'):
        statsd_timer(metric, line['service_time'])

if __name__ == '__main__':
    input_file = sys.argv[1]
    main(input_file)


# TODO:  
# Make supervisor process
# Test Reload
# Dynamic StatsD config
# Statsd
# Graphite
