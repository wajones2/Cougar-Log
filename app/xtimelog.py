from math import ceil # rounds up floats


class Timelog:
    def __init__(self): 

        self.hour_convert = lambda x,y: (x * 60) + y 

    def calculate(self, date, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        start_end_time = [self.start_time, self.end_time]

        self.date = date
        self.start_end_time = start_end_time

        self.labels = ["Date", "Start Time", "End Time", "Total", "Minutes"]
        self.date = date
        self.start_end_time = start_end_time

        self.start = self.start_end_time[0]
        self.end = self.start_end_time[1]
        a = [i.split(":") for i in self.start_end_time]  

        for i in range(len(a)):
            a[i][0] = int(a[i][0])
            a[i][1] = int(a[i][1])

        total = [0,0]
        for i in range(len(total)):
            total[i] = a[1][i] - a[0][i]

        self.minutes = self.hour_convert(total[0],total[1])
        self.hours = lambda minutes: str(minutes / 60).split('.')    # hours[0] is the number of hours

        self.hqty = self.hours(self.minutes)    # This value changes on line 71
        hrs, mins = self.hqty[0], self.hqty[1]

        self.decimal = lambda decimal: float('.' + decimal[1])          # hours[1] is a decimal that needs to
                                                                        # be converted to minutes
        self.deci = self.decimal(self.hqty)

        self.hqty[0] = int(self.hqty[0])        # self.hqty changes here
        self.hqty[1] = ceil(self.deci * 60)     # Added ceil() so the time wouldn't round down

        self.duration = f"{self.hqty[0]} hr {int(self.hqty[1])} min"

        self.info = [self.date, self.start, self.end, self.duration, self.minutes]

        self.logdict = {}
        for i in range(len(self.labels)):
            self.logdict[self.labels[i]] = self.info[i]

        return self.duration

    def add_time(self, total_hours, total_minutes): # This should now be able to run without calculate() needing to run first.

        self.total_hours = total_hours
        self.total_minutes = total_minutes

        
        self.minutes = self.hour_convert(self.total_hours, self.total_minutes)
        self.hours = lambda minutes: str(minutes / 60).split('.')    # hours[0] is the number of hours


        self.hqty = self.hours(self.minutes)    # Is two integers because self.hours gets split
        hrs, mins = self.hqty[0], self.hqty[1]

        self.decimal = lambda decimal: float('.' + decimal[1])
        self.deci = self.decimal(self.hqty)

        self.hqty[0] = int(self.hqty[0])
        self.hqty[1] = ceil(self.deci * 60) # Added ceil() so the time wouldn't round down

        self.duration = f"{self.hqty[0]} hr {int(self.hqty[1])} min"

        return self.duration


# m2 = Timelog()
# m2.calculate("01/21/2022", "4:30", "10:20")

