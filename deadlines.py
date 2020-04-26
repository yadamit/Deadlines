import argparse
import pickle
import os.path
from datetime import datetime


parser = argparse.ArgumentParser()

class Deadline:
    def __init__(self, name=None, date=None, details=None):
        self.name = name
        self.date = date
        self.details = details
    def __repr__(self):
        return f"{self.name[:15]:>20}  {str(self.date):<15} "
    def get_date(self):
        return self.date
    def cmp(self):
        return self.date.cmp()

class Date:
    def __init__(self, date=None, month=None):
        self.week_list = ["Sun", "Mon", "Tue", "Wed", "Thrus", "Fri", "Sat"]
        self.month_list = ["Jan", "Feb", "Mar", "Apr", "May", "June",\
                            "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
        self.date=date
        self.month = month if type(month)==int else month #TODO: styp(month)==int
    def __repr__(self):
        return f"{self.date:<2} {self.month_list[self.month-1]:<5}"
    def cmp(self):
        return (self.month, self.date)


class Data:
    def __init__(self):
        self.deadlines = []
    def add_deadline(self, name="", date=None, month=None):
        date = int(date)
        month = int(month) if month.isdigit() else month
        date = Date(date, month)
        d = Deadline(name, date)
        self.deadlines.append(d)
        self.deadlines.sort(key=lambda x: x.cmp())
        print(f"Added deadline:\t {str(d)}")
    def remove_deadline(self, name=None):
        for i,d in enumerate(self.deadlines):
            if d.name==name:
                delete = self.deadlines.pop(i)
                print(f"Remove deadline:\t {str(delete)}")
                return
        if i+1==len(self.deadlines):
            print(f"{name}: No such deadline found")
    def print_all(self):
        print("All deadlines:")
        for d in self.deadlines:
            print(d)
    def print_upcoming(self):
        print("Upcoming deadlines:")
        for d in self.deadlines:
            if d.date.month>=datetime.now().month:
                if d.date.date>=datetime.now().day:
                    print(d)
    def save_data(self, data_file):
        with open(data_file, "wb") as f:
            pickle.dump(self, f)

data_file = "./deadline.pkl"
data = None
if os.path.isfile(data_file):
    with open(data_file, "rb") as f:
        data = pickle.load(f)
else:
    data = Data()

parser.add_argument("-a", "--add", nargs="+", help="Add a new deadline: Name, date, month")
parser.add_argument("-r", "--remove", help="Remove a deadline: -r Name", type=str)
parser.add_argument("--upcoming", action="store_true", help="Shows upcoming deadlines")
parser.add_argument("--showall", action="store_true", help="Shows all deadlines including past")

args = parser.parse_args()
if args.add is not None:
    (name, date, month) = args.add
    print(name)
    print(date)
    print(month)
    data.add_deadline(name, date, month)
    data.save_data(data_file)

if args.remove is not None:
    name = args.remove
    data.remove_deadline(name)
    data.save_data(data_file)

if args.showall:
    data.print_all()
if args.upcoming:
    data.print_upcoming()

# data_file = "./deadline.pkl"
# with open(data_file, "wb") as f:
#     pickle.dump(deadlines, data_file)
