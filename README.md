### Deadlines
Simple command line tool to track deadlines.  
Show upcoming deadlines in color.

Use:
* `deadlines --add dl_name date month` : Adds a new deadline. Can be duplicate. Date and month are integers.
* `deadlines --remove dl_name` : Removes deadline
* `deadlines --removeall` : Removes all deadlines
* `deadlines --all` : Shows all deadlines, including past.
* `deadlines --upcoming` : Shows upcoming deadlines only

To make the file global, run:
```bash
sudo ./install.sh
```
