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
$ pomodoro && espeak "BREAK TIME"  # alert after the 'pomodoro' is finished
$ dash start sometask && pomodoro && dash end  # work on a task for a pomodoro
```

See http://pomodorotechnique.com/ for more information about the Pomodoro
technique.
