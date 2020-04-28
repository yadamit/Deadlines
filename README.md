### Deadlines
Simple command line tool to track deadlines.  
Show upcoming deadlines in color.

Use:
* `deadlines --add dl_name date month year --details "Don't miss it"` : Adds a new deadline. Date, month and year are integers and optional.
* `deadlines --remove dl_name` : Removes deadline
* `deadlines --removeall` : Delete all deadlines
* `deadlines --all` : Shows all deadlines, including past.
* `deadlines --upcoming` : Shows upcoming deadlines only

To make the file global, run:
```bash
sudo ./install.sh
```

Examples:
```bash
deadlines --add DL1 27 04
deadlines --add "Deadline 2" 02 05 2021 --details "Important"
deadlines --add "Today's deadline"
deadlines --add "Past deadline" 20 03 2019 --details "Don't worry about it"
deadlines --all
```
```bash
deadlines --remove DL1
```
```bash
deadlines --upcoming
```
