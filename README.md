pomodoro -- a super-minimal timer

Example usage:

```bash
$ alias pomodoro=`pwd`/pomodoro.py
$ pomodoro  # start a 25-minute timer
$ pomodoro 20 5 true  # start a 20 minute timer, with 5 minutes of break
                      # and a visual flash afterwards
$ pomodoro 1h 5s  # other ways to specify times
```

pomodoro is meant to be chained with other programs in an unix-y manner.
See http://espeak.sourceforge.net/ and https://github.com/koirikivi/dash for
example programs.

```bash
$ pomodoro && espeak "BREAK TIME"  # alert after
$ dash start sometask && pomodoro && dash end
```
