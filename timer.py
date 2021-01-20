import time
import math
import os
import subprocess
from tempfile import NamedTemporaryFile
from multiprocessing import Process
from math import inf
from pydub import AudioSegment
from pydub.playback import play
from pydub.utils import get_player_name
from helper import *

class Timer:
    def __init__(self):
        """
        Create Timer object:
        - Set number of rounds in timer
        - Set number of intervals per round
        - Set interval lengths
        """
        # Get number of rounds
        def get_num_rounds(self):
            # Set flag
            input_validated = False

            # Get input from user
            while not input_validated:
                num_rounds = input('Enter number of rounds (enter "inf" for infinity): ')
                # Check for "inf" input 
                if num_rounds == "inf":
                    num_rounds = math.inf
                    input_validated = True
                else:
                    # Check for valid integer input
                    if check_input(num_rounds):
                        num_rounds = int(num_rounds)
                        input_validated = True
                    else:
                        print("Input error: number of rounds must be integer > 0")

            return num_rounds



        # Get number of intervals per round
        def get_num_intervals(self):
            # Set flag
            input_validated = False

            # Get input from user
            while not input_validated:
                num_intervals = input("Enter number of intervals per round: ")
                # Check for valid integer input
                if check_input(num_intervals):
                    num_intervals = int(num_intervals)
                    input_validated = True
                else:
                    print("Input error: number of intervals must be integer > 0")
            return num_intervals



        # Get interval lengths
        def get_interval_lengths(self, intervals_dict):
            i = 1
            print("Enter interval lengths in terms of hours, minutes, and seconds\nseparated by colons (i.e. [hr:][min:]sec)")
            while i <= self.intervals:
                # Set flag
                input_validated = False

                # Get input from user
                while not input_validated:       
                    interval_length = input(f"Interval {i}: ")
                    # Check for valid integer input
                    input_validated = True
                    interval_split = interval_length.rstrip().split(':')
                    for interval in interval_split:
                        if not check_input(interval):
                            print("Input error: interval length must be comprised of non-negative integers separated by colons. e.g. 00:00:00")
                            input_validated = False
                    
                # Convert interval length to seconds
                length_in_seconds = convert_to_seconds(interval_split)
                
                intervals_dict[f"interval_{i}"] = length_in_seconds
                i += 1
        
        # Set timer attributes
        self.rounds = get_num_rounds(self)
        self.intervals = get_num_intervals(self)
        print()
        self.intervals_dict = {}
        get_interval_lengths(self, self.intervals_dict)

        

    def go(self):
        """
        Activate timer
        """
        # Create audio segment object
        ding = AudioSegment.from_file('ding.wav', format='wav')

        # Define custom play function to suppress pydub print output, enable multiprocessing
        def play_sound(self, seg):
            audio_player = get_player_name()

            with NamedTemporaryFile('w+b', suffix='.wav') as f:
                seg.export(f.name, 'wav')
                devnull = open(os.devnull, 'w')
                subprocess.call(
                    [audio_player, "-nodisp", "-autoexit", "-hide_banner", f.name],
                    stdout=devnull, stderr=devnull)
            
        i = 0
        while i < self.rounds:
            j = 0
            while j < self.intervals:
                # Get current interval length from intervals_dict
                countdown = self.intervals_dict[f"interval_{j + 1}"] - 1

                while countdown >= 0:
                    # Convert countdown to seconds, minutes, hours to display
                    secs = countdown % 60
                    mins = (countdown // 60) % 60
                    hrs = (countdown // 60) // 60

                    # Display countdown
                    timer = f"{hrs:02d}:{mins:02d}:{secs:02d}"
                    print(timer, end='\r')
                    time.sleep(1)
                    countdown -= 1

                    # Parallelize play function so that it does not interfere with timer countdown
                    if countdown < 0:
                        p = Process(target=play_sound, args=(self, ding))
                        p.start()

                j += 1
            i += 1

def main():
    timer = Timer()
    print()
    timer.go()

main()
