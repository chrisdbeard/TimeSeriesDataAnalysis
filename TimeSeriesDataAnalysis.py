# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 09:32:50 2022

@author: Chris
"""
import pathlib
from datetime import datetime


#MainForm is a GUI. Need to make a GUI here or hard code, or prompt user in console for input?

class DataEntry:
    """
    Represents one line in a data file.

    ...

    Attributes
    ----------
    raw : string
        Represents a line from a data file.
    time : datetime
        Represents the first index of the line from a data file.
    pressure : float
        Represents the second index of the line from a data file.
    altitude : float
        Represents the third index of the line from a data file.
    bit_rate : float
        Represents the fourth index of the line from a data file.
    pitch : float
        Represents the fifth index of the line from a data file.
    slant_range : float
        Represents the six index of the line from a data file.
    distance_to_target : float
        Represents the seventh index of the line from a data file.
    roll : float
        Represents the eighth index of the line from a data file.

    Methods
    -------
    to_string():
        Represent the DataEntry as a string.

    """

    def __init__(self, line):
        self.raw = line
        split_line = line.split(',')
        self.time = datetime.strptime(split_line[0])
        self.pressure = float(split_line[1])
        self.altitude = float(split_line[2])
        self.bit_rate = float(split_line[3])
        self.pitch = float(split_line[4])
        self.slant_range = float(split_line[5])
        self.distance_to_target = float(split_line[6])
        self.roll = float(split_line[7])
        
        
    def to_string(self):
        return f"{self.time},{self.pressure},{self.altitude},{self.bit_rate},{self.pitch},{self.slant_range},{self.distance_to_target},{self.roll}"
 
  
class Event:

    
    def __init__(self):
        pass
        
        
    def parse_yes_no(self):
        pass
        
 
class DataSet:
    
    
    def __init__(self):
        pass
        
        
    def read_data_file(self):
        pass
        
        
    def get_data_by_event(self):
        pass
        

class EventList:
    
    
    def __init__(self):
        pass
        
        
    def read_event_file(self):
        pass
        

class AnalysisController:
    
    
    def __init__(self):
        pass
        
        
    def read_data_file(self, file_path):
        pass
        
        
    def read_event_file(self):
        pass
        
        
    def seperate_data_files_by_event(self):
        pass
        
        
    def write_data_files_by_event(self):
        pass
        
        
    def clear(self):
        pass
        
        
    
    

def Main():
    #controller = AnalysisController
    dataset_path = pathlib.Path{"C:\Users\heart\Documents\Programming\Python\TimeSeriesDataAnalysis\Data\Datasets\Dataset_small.csv"}
    print("Complete")
    pass
 
    
if __name__ == '__main__':
    Main()