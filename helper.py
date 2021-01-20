def check_input(input):
    """
    Verify that the user entered a _positive_ integer input
    """
    check = True
    
    if len(input) == 0:
        check = False
    else:
        for i in range(len(input)):
            if (input[i] < '0') or (input[i] > '9'):
                check = False

    return check

def convert_to_seconds(interval_length_list):
    """
    Convert interval legnth, passed as list of [hr, min, sec] values, to seconds
    """
    # Convert interval length to seconds
    length_in_seconds = 0
    for i in range(len(interval_length_list)):
        length_in_seconds += int(interval_length_list[-1 - i]) * (60 ** i)
    
    return length_in_seconds
