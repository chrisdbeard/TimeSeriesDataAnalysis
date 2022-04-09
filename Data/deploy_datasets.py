# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 18:05:50 2022

@author: andre
"""

import os
import pathlib
import datetime
import random
import pandas as pd
import numpy as np


def make_event_times(num_events):
    start_times = []
    end_times = []
    
    base_year = random.randint(2020, 2022)
    base_month = random.randint(1, 12)
    base_day = random.randint(1, 30)
    base_hour = random.randint(1, 24)
    base_minute = random.randint(0, 60)
    base_second = random.randint(0, 60)
    base_msecs = random.randint(0, 999_999)
    base_time = datetime.datetime(base_year, base_month, base_day, base_hour, base_minute, base_second, base_msecs)
    
    start_times.append(base_time)
    minutes = random.randint(0, 5)
    seconds = random.randint(0, 60)
    msecs = random.randint(0, 999_999)
    duration = datetime.timedelta(minutes=minutes, seconds = seconds, microseconds = msecs)
    end_times.append(base_time + duration)
        
    for event_num in range(num_events-1):
        minutes = random.randint(0, 5)
        seconds = random.randint(0, 60)
        msecs = random.randint(0, 999_999)
        duration = datetime.timedelta(minutes=minutes, seconds = seconds, microseconds = msecs)
        start_times.append(end_times[event_num] + duration)
        end_times.append(start_times[-1] + duration)
              
    return start_times, end_times


def gen_feature(num_events, feature_values):
    feature_list = []
    for event_num in range(num_events):
        feature_list.append(feature_values[random.randint(0, len(feature_values)-1)])
    return feature_list


def gen_dataset(num_lines, events_start, events_end):
    pre_hours = random.randint(0, 2)
    pre_minutes = random.randint(0, 60)
    pre_seconds = random.randint(0, 60)
    pre_msecs = random.randint(0, 999_999)
    pre_time = datetime.timedelta(hours = pre_hours, minutes=pre_minutes, seconds = pre_seconds, microseconds = pre_msecs)
    data_start_time = events_start - pre_time
    
    post_hours = random.randint(0, 2)
    post_minutes = random.randint(0, 60)
    post_seconds = random.randint(0, 60)
    post_msecs = random.randint(0, 999_999)
    post_time = datetime.timedelta(hours = post_hours, minutes=post_minutes, seconds = post_seconds, microseconds = post_msecs)
    data_end_time = events_end + post_time
    
    time = []
    feature_1 = []
    feature_2 = []
    feature_3 = []
    feature_4 = []
    feature_5 = []
    feature_6 = []
    feature_7 = []
    
    time_step = (data_end_time - data_start_time)/num_lines
    for line_num in range(num_lines):
        curr_time = data_start_time + time_step*line_num
        time.append(curr_time)
        ratio = (curr_time - data_start_time)/(data_end_time - data_start_time)
        feature_1_val = (np.sin(2*np.pi*ratio)*3000) + random.uniform(0,200)
        feature_1.append(feature_1_val)
        feature_2_val = (np.cos(2*np.pi*ratio)*20_000) + random.uniform(0,80)
        feature_2.append(feature_2_val)
        feature_3_val = (np.sin(2*np.pi*ratio)*300) + random.uniform(0,400)
        feature_3.append(feature_3_val)
        feature_4_val = (np.cos(2*np.pi*ratio)) + random.uniform(0,2)
        feature_4.append(feature_4_val)
        feature_5_val = (np.sin(2*np.pi*ratio)*20_000) + random.uniform(0,14000)
        feature_5.append(feature_5_val)
        feature_6_val = 40_000 + random.uniform(0,80)
        feature_6.append(feature_6_val)
        feature_7_val = (np.cos(2*np.pi*ratio)*360) + random.uniform(0,30)
        feature_7.append(feature_7_val)
        print('')
    data = {'Time': time, 
            'Pressure (mmHg)': feature_1,
            'Altitude (ft.)': feature_2,
            'Bit_Rate (Baud)': feature_3,
            'Pitch (°)': feature_4,
            'Slant Range (ft.)': feature_5,
            'Distance to Target (ft)': feature_6,
            'Roll (°)': feature_7}
    return data
    
def create_data_files(num_events, num_data_points, name):
    start_times, end_times = make_event_times(num_events)
    actors = gen_feature(num_events, ['Actor 1', 'Actor 2'])
    event_types = gen_feature(num_events, ['Event type 1', 'Event type 2', 'Event type 3', 'Event type 4', 'Event type 5'])
    attribute_1 = gen_feature(num_events, ['Yes', 'No'])
    attribute_2 = gen_feature(num_events, ['Yes', 'No'])
    attribute_3 = gen_feature(num_events, ['Yes', 'No'])
    attribute_4 = gen_feature(num_events, ['Yes', 'No'])
    attribute_5 = gen_feature(num_events, ['Yes', 'No'])
    data = {'Start Time':start_times,
            'End Time':end_times,
            'Actor':actors,
            'Event Type':event_types,
            'System 1':attribute_1,
            'System 2':attribute_2,
            'System 3':attribute_3,
            'System 4':attribute_4,
            'System 5':attribute_5}
    df = pd.DataFrame(data)
    cwd = pathlib.Path(os.getcwd())
    file_path = cwd / "Event Lists"/ f"Event_List_{name}.csv"
    file_path.parent.mkdir(parents = True, exist_ok = True)
    df.to_csv(file_path, index = False)
    
    events_start = start_times[0]
    events_end = end_times[-1]
    data = gen_dataset(num_data_points, events_start, events_end)
    df = pd.DataFrame(data)
    file_path = cwd / "Datasets" / f"Dataset_{name}.csv"
    file_path.parent.mkdir(parents = True, exist_ok = True)
    df.to_csv(file_path, index = False)
    
def main():
    random.seed(24601)
    num_events = 10
    num_data_points = 1_000
    create_data_files(num_events, num_data_points, 'small')
    num_events = 100
    num_data_points = 100_000
    create_data_files(num_events, num_data_points, 'medium')
    num_events = 1000
    num_data_points = 10_000_000
    create_data_files(num_events, num_data_points, 'large')
    
    
if __name__ == "__main__":
    main()