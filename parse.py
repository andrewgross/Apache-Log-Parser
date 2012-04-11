#!/bin/python
import sys
from log_parsing_functions import parse_nginx
import time

def get_average_over_interval(requests, total_service_time):
    if requests > 0:
        return total_service_time/requests
    else:
        return 0

def parse(line, parsing_function):
    return parsing_function(line)

def get_epoch_time(parsed_line_timestamp):
    # Convert the time to a more regular format and convert that to epoch time
    return int(time.mktime(time.strptime(parsed_line_timestamp, "%d/%b/%Y:%H:%M:%S +0000")))

def save_interval(time):
    interval_data = time_series_data[time]
    requests, total_service_time, average_service_time = interval_data
    total_service_time = interval_data[1]
    average_service_time = get_average_over_interval(requests, total_service_time)
    interval_data[2] = average_service_time

def create_interval(time):
    time_series_data[time] = [0, 0, 0]

def update_interval(time, service_time):
    interval_data = time_series_data[time]
    requests, total_service_time, average_service_time = interval_data
    requests = requests + 1
    total_service_time = total_service_time + service_time
    interval_data[0] = requests
    interval_data[1] = total_service_time

def organize_output(time_series_data, initial_interval_time, interval_size):
    current_time = initial_interval_time
    output = None

    while time_series_data[current_time]:
        if output:
            output = output + ', %.4f' % time_series_data[current_time][2]
        else:
            output = '%.4f' % time_series_data[current_time][2]
        current_time = current_time + interval_size
    return output

def main(input_files):

    time_series_data={} # { interval_time => [requests, total_service_time, average_service_time] }
    interval_size = 300 # 5 minutes is our time bucket for now

    current_interval_time = None
    initial_interval_time = None # Save this so we can interate in order later

    for input_file in input_files:
        f=open(input_file)
        for line in f:
            parsed_line = parse(line, parse_nginx)
            request_time = get_epoch_time(parsed_line['timestamp'])
            service_time = float(parsed_line('service_time'))
            while True:
                if not current_interval_time:
                    initial_interval_time = request_time
                    current_interval_time = request_time
                    create_interval(current_interval_time)

                if request_time - current_interval_time > interval_size:
                    save_interval(current_interval_time)
                    current_interval_time = current_interval_time + interval_size
                    create_interval(current_interval_time)
                    continue # because we can have blank intervals from bad data

                update_interval(current_interval_time, service_time)
                break # Trying to think of a better way to handle blank intervals than 'retry until break'

        save_interval(current_interval_time)
        f.close()

    print "[%s]" % organize_output(time_series_data, initial_interval_time, interval_size)

if __name__ == '__main__':
    input_files = sys.argv[1:]
    main(input_files)


