"""
Example usage:
python event_average --wt <int value representing the window limit in seconds>
python event_average --wt 3
OR 
DEFAULT
python event_average 
"""

from __future__ import division
import random
import time
import sys
import argparse


class AverageWindow(object):

    def __init__(self, window_limit):
        self.window_limit = window_limit
        self.data_list = []
        self.avg_dict = {}

    def flush_data(self):
        self.data_list = []
        self.avg_dict = {}

    @staticmethod
    def get_value():
        event_id = random.randint(1, 10)
        value = random.randint(1, 100) * random.random()
        return time.time(), event_id, value

    def process(self):
        start_time = time.time()
        while True:
            time_stamp, event_id, value = self.get_value()
            if time_stamp - start_time >= self.window_limit:
                return
            self.data_list.append((time_stamp, event_id, value))

    def get_aggregate_data(self):
        data_dict = {}
        for each_data in self.data_list:
            event_id = each_data[1]
            value = each_data[2]
            if event_id in data_dict.keys():
                cur_sum = data_dict[event_id][0]
                cur_counter = data_dict[event_id][1]
                data_dict[event_id] = (cur_sum + value, cur_counter + 1)
            else:
                data_dict[event_id] = (value, 1)
        return data_dict

    def get_average(self):
        data_dict = self.get_aggregate_data()
        for event_id, sum_counter in data_dict.items():
            self.avg_dict[event_id] = sum_counter[0] / sum_counter[1]

    def print_average(self):
        for event_id, avg in self.avg_dict.items():
            print("Average for {} is {}".format(event_id, avg))

    @staticmethod
    def main(window_limit):
        if window_limit is None:
            window_limit = 60
        awd = AverageWindow(window_limit)
        awd.process()
        awd.get_average()
        awd.print_average()
        awd.flush_data()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Find average per event over a window.')
    parser.add_argument('--wt', metavar='wt', type=int,
                        help='An integer value for max limit on the data collection window')
    args = parser.parse_args()
    AverageWindow.main(args.wt)
