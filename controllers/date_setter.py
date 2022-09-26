from csv import reader, writer
import csv
from datetime import date, datetime, timedelta

import shutil
import tempfile
from time import time
import pandas as pd
from pathlib import Path


def set_num_of_days( num_of_days):
       
        """Set internal date"""
        internal_date_path =  Path.cwd()/"data/Internal_date.csv" 
        data = [num_of_days]
        print(data)
        with open(internal_date_path ,"w") as csvfile:
            csvwriter = writer(csvfile, lineterminator="\n")
            for _ in data:
                csvwriter.writerow( data)


def read_nums_of_days():
     internal_date_path =  Path.cwd()/"data/Internal_date.csv" 
       
     with open(internal_date_path ,"r") as csvfile:
            data = list(csvfile)
   
     return data[0]

def get_internal_date(self,num_of_days):
        """get the internal num ogf days"""
        NUM_OF_DAYS = num_of_days
        today = datetime.now()
        return today + timedelta(days=NUM_OF_DAYS)
        
          
     
