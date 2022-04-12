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
    __str__():
        Represent the DataEntry as a string.

    """

    def __init__(self, line):
        self.raw = line
        split_line = line.split(',')
        self.time = datetime.strptime(split_line[0], "%Y-%m-%d %H:%M:%S.%f")
        self.pressure = float(split_line[1])
        self.altitude = float(split_line[2])
        self.bit_rate = float(split_line[3])
        self.pitch = float(split_line[4])
        self.slant_range = float(split_line[5])
        self.distance_to_target = float(split_line[6])
        self.roll = float(split_line[7])
        
        
    def __str__(self):
        return f"{self.time},{self.pressure},{self.altitude},{self.bit_rate},{self.pitch},{self.slant_range},{self.distance_to_target},{self.roll}"
 
  
class Event:
    """
    Represents one line in a data file.

    ...

    Attributes
    ----------
    raw : string
        Represents a line from a data file.
    start_time : datetime
        Represents the first index of the line from a data file.
    end_time : datetime
        Represents the second index of the line from a data file.
    actor : string
        Represents the third index of the line from a data file.
    event_type : string
        Represents the fourth index of the line from a data file.
    system1 : boolean
        Represents the fifth index of the line from a data file.
    system2 : boolean
        Represents the six index of the line from a data file.
    system3 : boolean
        Represents the seventh index of the line from a data file.
    system4 : boolean
        Represents the eighth index of the line from a data file.
    system5 : boolean
        Represents the ninth index of the line from a data file.        

    Methods
    -------
    parse_yes_no(input_string):
        Represent the string "yes" to a bool True, "no" to bool False and an empty string as None.

    """
    
    def __init__(self, line):
        self.raw = line
        split_line = line.split(',')
        self.start_time = datetime.strptime(split_line[0], "%Y-%m-%d %H:%M:%S.%f")
        self.end_time = datetime.strptime(split_line[1], "%Y-%m-%d %H:%M:%S.%f")
        self.actor = split_line[2]
        self.event_type = split_line[3]
        self.system1 = self.parse_yes_no(split_line[4])
        self.system2 = self.parse_yes_no(split_line[5])
        self.system3 = self.parse_yes_no(split_line[6])
        self.system4 = self.parse_yes_no(split_line[7])
        self.system5 = self.parse_yes_no(split_line[8])
        
        
    def parse_yes_no(self, input_string):
        output_bool = None
        if input_string.lower() == "yes":
            output_bool = True
        elif input_string.lower() == "no":
            output_bool = False
        return output_bool

                          
class DataSet:
    """
    Represents a list of data once read in a data file.

    ...

    Attributes
    ----------
    file_path : string
        Represents the file path.
    column_names : list
        Represents the first line from a data file.
    raw_header : string
        Represents the first line from a data file. 
    data : list
        Represents the data in the DataSet.

    Methods
    -------
    read_data_file(file_path):
        Reads an file if file.exist() and stores the first line as column names and the remaining lines as an DataEntry in data list.
    get_data_by_event(event):
        Returns select data from the DataEntry for which the data.time is between event.start_time and event.end_time.
    """ 
          
    def __init__(self, file_path, raw_header = "", data = []):
        self.file_path = file_path
        self.column_names = []
        self.raw_header = raw_header
        self.data = data
        if data == []:
            self.read_data_file(file_path)
    
        
    def read_data_file(self, file_path):
        if file_path.exists():
            self.file_path = file_path
            line_num = 0
            with open(self.file_path, 'r') as fh:
                for line in fh:
                    if line_num == 0:
                        self.column_names.append(line.split(','))
                        self.raw_header = line
                    else:
                        self.data.append(DataEntry(line))
                    line_num += 1
        
        
    def get_data_by_event(self, event):
        return [x for x in self.data if (x.time >= event.start_time) & (x.time <= event.end_time)]
        

class EventList:
    """
    Represents a list of Entries once read in of a entry data file.

    ...

    Attributes
    ----------
    events : list of Event
        Represents a Event in a list.
    column_names : list
        Represents the first line from a data file.
    file_path : datetime
        Represents the file path.    

    Methods
    -------
    read_event_file(file_path):
        Reads an file if file.exist() and stores the first line as column names and the remaining lines as an Event in events list.

    """    

   
    def __init__(self, file_path):
        self.events = []
        self.column_names = []
        self.file_path = file_path
        self.read_event_file(file_path)
        
        
    def read_event_file(self, file_path):
        if file_path.exists():
            self.file_path = file_path
            line_num = 0
            with open(self.file_path, 'r') as fh:
                for line in fh:
                    if line_num == 0:
                        self.column_names.append(line.split(','))
                    else:
                        self.events.append(Event(line))
                    line_num += 1
                                     

class AnalysisController:
    """
    Represents the controller of the project.

    ...

    Attributes
    ----------
    all_events : EventList
        Represents all the data in an EventList.
    all_datas : DataSet
        Represents all the data in a DataSet.
    data_by_event : list
        Represents data where the time is in range of the Events time frame. 

    Methods
    -------
    read_data_file(file_path):
        Sets the file_path for DataSets.
    read_event_file(file_path):
        Sets the file_path for the EventList.
    seperate_data_files_by_event():
        Returns select data from the DataEntry for which the data.time is between event.start_time and event.end_time.
    write_data_files_by_event(output_dir):
        Writes data to file by the event.
    """    
    
    
    def __init__(self):
        self.all_events = None
        self.all_data = None
        self.data_by_event = []
        
        
    def read_data_file(self, file_path):
        self.all_data = DataSet(file_path)
        
        
    def read_event_file(self, file_path):
        self.all_events = EventList(file_path)
        
        
    def seperate_data_files_by_event(self):
        for event in self.all_events.events:
            data_for_event = self.all_data.get_data_by_event(event)
            self.data_by_event.append(DataSet(self.all_data.file_path, raw_header = self.all_data.raw_header,  data = data_for_event))
        
        
    def write_data_files_by_event(self, output_dir):
        event_num = 1
        for data_set in self.data_by_event:
            output_file_path = output_dir / f"Data_for_event_{event_num}.csv"
            output_dir.mkdir(parents = True, exist_ok = True)
            with open(output_file_path, 'w') as fh:
                fh.write(data_set.raw_header)
                for entry in data_set.data:
                    fh.write(str(entry) + "\n")
            event_num += 1
   

def Main():
    #controller = AnalysisController
    dataset_file_path = pathlib.Path(r"C:\Users\heart\Documents\Programming\Python\TimeSeriesDataAnalysis\Data\Datasets\Dataset_small.csv")
    event_file_path = pathlib.Path(r"C:\Users\heart\Documents\Programming\Python\TimeSeriesDataAnalysis\Data\Event Lists\Event_List_small.csv")
    output_dir = pathlib.Path(r"C:\Users\heart\Documents\Programming\OutputDump")
    controller = AnalysisController()
    controller.read_data_file(dataset_file_path)
    controller.read_event_file(event_file_path)
    controller.seperate_data_files_by_event()
    controller.write_data_files_by_event(output_dir)
    print("Complete")
 
    
if __name__ == '__main__':
    Main()