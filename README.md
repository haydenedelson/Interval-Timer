# Interval-Timer
Creates a terminal-based interval timer, using custom audio output functions and multiprocessing

## Dependencies
Pydub requires Python3.7

## Usage
Follow in-line instructions, as shown below:

![Inline Usage Example](https://github.com/haydenedelson/Interval-Timer/blob/main/Content/Timer%20Usage.png)

Hours, minutes, and seconds must be separated by semicolons. Not all values are necessary. For example, if setting an interval length to 30 seconds, the input `30` is equivalent to `0:30` or `0:0:30`. Similarly, if setting an interval length to 10 minutes, the input `10:0` is equivalent to `0:10:0`. However, `10:0` is **not** equivalent to `0:10` because the latter signifies an interval length of 10 seconds.
