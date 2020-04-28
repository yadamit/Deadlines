import pickle
from datetime import datetime, date

days_in_month = [31,29,31,30,31,30,31,31,30,31,30,31]
month_list = ["", "Jan","Feb","Mar","Apr","May","June","July","Aug","Sept","Oct","Nov","Dec"]
week_list = ["Mon", "Tue", "Wed", "Thru", "Fri", "Sat", "Sun"]

today = date.today()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    UPCOMING = '\033[93m'
    DETAILS = '\033[94m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Deadline:
    def __init__(self, name=None, date=None, details=None):
        self.name = name
        self.date = date
        self.details = "" if details is None else details
    def __repr__(self):
        str_date = self.date.strftime("%d/%m/%y")
        str_date = str(self.date.day)+" "+month_list[self.date.month]+" "+str(self.date.year)
        days_left = (self.date-today).days
        details = bcolors.DETAILS+self.details+bcolors.DEFAULT if days_left>=0 else self.details
        week_day = week_list[self.date.weekday()]
        if self.date>=today:
            return f"{bcolors.UPCOMING}{self.name[:30]:>30}:  {week_day:>4}. {str_date:<15} ({days_left:>3} days left) {details}{bcolors.DEFAULT}"
        else:
            return f"{self.name[:30]:>30}:  {week_day:>4}. {str_date:<15} {'past':<15} {details}"
    def get_date(self):
        return self.date
    def in_same_week(self, next_dl):
            """check if the input deadline is in same week"""
            w1 = self.date.weekday()
            w2 = next_dl.date.weekday()
            if w2<w1 or (next_dl.date-self.date).days>=7:
                return False
            return True

class Data:
    def __init__(self):
        self.deadlines = []
    def add_deadline(self, name="", day=today.day, month=today.month, year=today.year, details=None):
        day, month, year = int(day), int(month), int(year)
        if day > days_in_month[month-1]:
            print(bcolors.FAIL, "Days in given month: ", days_in_month[month-1])
            print("Deadline not added", bcolors.DEFAULT)
            exit()
        if month > 12:
            print(bcolors.FAIL, "month can't be greater than 12")
            print("Deadline not added", bcolors.DEFAULT)
            exit()
        dl_date = date(year, month, day)
        d = Deadline(name, dl_date, details)
        self.deadlines.append(d)
        self.deadlines.sort(key=lambda x: x.date)
        print(f"Added deadline:\n{str(d)}\n")
    def remove_deadline(self, name=None):
        for i,d in enumerate(self.deadlines):
            if d.name==name:
                delete = self.deadlines.pop(i)
                print(f"Remove deadline:\n{str(delete)}")
                return
        if i+1==len(self.deadlines):
            print(f"{bcolors.FAIL}{name}: No such deadline found{bcolors.DEFAULT}")

    def removeall(self):
        self.deadlines = []

    def print_all(self):
        print("All deadlines:")
        prev_dl = self.deadlines[0] if len(self.deadlines)!=0 else None
        for d in self.deadlines:
            if not prev_dl.in_same_week(d):
                print(" "*25,"\u2500"*44)
            print(d)
            prev_dl = d

    def print_upcoming(self):
        print("Upcoming deadlines:")
        prev_dl = None
        for i,d in enumerate(self.deadlines):
            if d.date>=today:
                prev_dl = d if prev_dl==None else prev_dl
                if not prev_dl.in_same_week(d):
                    print(" "*25,"\u2500"*44)
                print(d)
                prev_dl = d

    def save_data(self, data_file):
        with open(data_file, "wb") as f:
            pickle.dump(self, f)

