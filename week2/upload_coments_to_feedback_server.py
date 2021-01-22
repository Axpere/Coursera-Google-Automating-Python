#!/usr/bin/env python3

import os
import requests

#Creates list for all files
files_list = os.listdir(path='/data/feedback/')
feedback_dict = {}

for file in files_list:
    with open('/data/feedback/' + file, "r") as a_file: #Once Python exits from with, closes the file automatically
        info = a_file.read().split('\n') #creates a list with the information
        feedback_dict = {'title':info[0], 'name':info[1], 'date':info[2], 'feedback':info[3]} #creates a dictionary from the list
        response = requests.post("http://********/feedback/", data=feedback_dict) #change the "****" with the IP
        response.raise_for_status() #Check response for errors
