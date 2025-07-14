#!/usr/bin/env python3
# Student ID: [162982235]

class Time:
    def __init__(self, hour, minute, second):
        if not (isinstance(hour, int) and isinstance(minute, int) and isinstance(second, int)):
            raise Exception("All arguments must be integers")
        if hour < 0 or minute < 0 or second < 0:
            raise Exception("Time values cannot be negative")
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_sec(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def format_time(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"

    def sum_times(self, other_time):
        total_seconds = self.time_to_sec() + other_time.time_to_sec()
        hour = total_seconds // 3600
        total_seconds %= 3600
        minute = total_seconds // 60
        second = total_seconds % 60
        return Time(hour, minute, second)

    def change_time(self, seconds):
        total_seconds = self.time_to_sec() + seconds
        if total_seconds < 0:
            total_seconds = 0
        self.hour = total_seconds // 3600
        total_seconds %= 3600
        self.minute = total_seconds // 60
        self.second = total_seconds % 60

    def valid_time(self):
        if 0 <= self.hour and 0 <= self.minute < 60 and 0 <= self.second < 60:
            return True
        return False

def sec_to_time(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    second = seconds % 60
    return Time(hour, minute, second)
