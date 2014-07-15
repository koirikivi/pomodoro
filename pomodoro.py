#!/usr/bin/env python
import re
import sys
import time


DEFAULT_POMODORO_TIME = 25 * 60
DEFAULT_BREAK_TIME = 5 * 60


if sys.stdout.isatty():
    def output(string):
        string = "\r%s" % string
        sys.stdout.write(string)
        sys.stdout.flush()
else:
    def output(string):
        print string


def pomodoro(pomodoro_time=DEFAULT_POMODORO_TIME,
             break_time=DEFAULT_BREAK_TIME):
    time_left = pomodoro_time
    while time_left > 0:
        output("%2d:%02d" % ((time_left / 60), (time_left % 60)))
        time_left -= 1
        time.sleep(1)
    time_left = break_time
    while time_left > 0:
        output("BREAK %2d:%02d"
               % ((time_left / 60), (time_left % 60)))
        time_left -= 1
        time.sleep(1)
    for _ in range(3):
        output("                  ")
        time.sleep(0.5)
        output("****   DONE   ****")
        time.sleep(0.5)
    print("")


def get_index(indexable, index, default=None):
    try:
        return indexable[index]
    except IndexError:
        return default


def parse_time(string):
    multipliers = {
        "s": 1,
        "sec": 1,
        "second": 1,
        "seconds": 1,
        "m": 60,
        "min": 60,
        "minute": 60,
        "minutes": 60,
        "h": 60 * 60,
        "hour": 60 * 60,
        "hours": 60 * 60,
    }

    if isinstance(string, (int, long)):
        return string
    string = string.lower().strip()
    match = re.match("^(\d+)\s*(.*)$", string)
    if match is None or not match.groups()[1]:
        # Try to return the time as minutes
        return int(string) * 60
    time_str, multiplier_str = match.groups()
    try:
        multiplier = multipliers[multiplier_str]
    except KeyError:
        raise ValueError("invalid time format")
    return int(time_str) * multiplier


def main():
    if get_index(sys.argv, 1, "").endswith("help"):
        print("USAGE: %s [--help] [time] [break_time]"
              % sys.argv[0])
        return 0
    pomodoro_time = parse_time(get_index(
            sys.argv, 1, DEFAULT_POMODORO_TIME))
    break_time = parse_time(get_index(
            sys.argv, 2, DEFAULT_BREAK_TIME))
    pomodoro(pomodoro_time=pomodoro_time,
             break_time=break_time)


if __name__ == "__main__":
    main()
