from tkinter import *

def check_input(input):
    """
    Verify that the user entered a _positive_ integer input
    """
    check = True
    for i in range(len(input)):
        if input[i] < '0' or input[i] > '9':
            check = False

    return check

def convert_to_seconds(interval):
    """
    Convert interval legnth, passed as hr:min:sec string, to seconds
    """
    interval_length_list = interval.split(':')
    # Convert interval length to seconds
    length_in_seconds = 0
    for j in range(len(interval_length_list)):
        if check_input(interval_length_list[-1 - j]):
            length_in_seconds += int(interval_length_list[-1 - j]) * (60 ** j)
        else:
            print("Input error: interval length must be comprised of non-negative integers separated by colons. e.g. 00:00:00")
            return
    
    return length_in_seconds
