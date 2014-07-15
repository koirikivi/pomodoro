#!/usr/bin/env python
import re
import sys
import time


DEFAULT_POMODORO_TIME = 25 * 60
DEFAULT_BREAK_TIME = 0 * 60
DEFAULT_FLASH = False


def pomodoro(pomodoro_time=DEFAULT_POMODORO_TIME,
             break_time=DEFAULT_BREAK_TIME,
             flash=DEFAULT_FLASH):
    if pomodoro_time:
        pomodoro_round(pomodoro_time)
    if break_time:
        pomodoro_round(break_time, prefix="BREAK ")
    if flash:
        flash_animation()
    print("")


def pomodoro_round(time_, prefix=""):
    time_left = time_
    while time_left > 0:
        output_time(time_left, prefix=prefix)
        time_left -= 1
        time.sleep(1)
    output_time(time_left, prefix=prefix)


def flash_animation():
    for _ in range(3):
        output("                  ")
        time.sleep(0.5)
        output("****   DONE   ****")
        time.sleep(0.5)


def output_time(time_, prefix=""):
    output("%s%2d:%02d" % (prefix, (time_ / 60), (time_% 60)))


if sys.stdout.isatty():
    def output(string):
        string = "\r%s" % string
        sys.stdout.write(string)
        sys.stdout.flush()
else:
    def output(string):
        print string


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


def parse_bool(string):
    return string.lower().strip() in ('1', 't', 'true')


def main():
    if get_index(sys.argv, 1, "").endswith("help"):
        print("USAGE: %s [--help] [time] [break_time] [flash?]"
              % sys.argv[0])
        return 0
    pomodoro_time = parse_time(get_index(
            sys.argv, 1, DEFAULT_POMODORO_TIME))
    break_time = parse_time(get_index(
            sys.argv, 2, DEFAULT_BREAK_TIME))
    flash = parse_bool(get_index(
            sys.argv, 3, "t" if DEFAULT_FLASH else "f"))
    pomodoro(pomodoro_time=pomodoro_time,
             break_time=break_time,
             flash=flash)


if __name__ == "__main__":
    main()
