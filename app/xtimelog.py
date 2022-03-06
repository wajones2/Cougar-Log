from math import ceil # rounds up floats


class Timelog:
    def __init__(self): 

        self.hour_convert = lambda x,y: (x * 60) + y 

    def calculate(self, date, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        start_end_time = [self.start_time, self.end_time]

        self.date = date
        self.start_end_time = start_end_time        # Why twice?

        self.labels = ["Date", "Start Time", "End Time", "Total", "Minutes"]
        self.date = date
        self.start_end_time = start_end_time        # Why twice?

        self.start = self.start_end_time[0]
        self.end = self.start_end_time[1]
        self.a = [i.split(":") for i in self.start_end_time]

        for i in range(len(self.a)):
            self.a[i][0] = int(self.a[i][0])
            self.a[i][1] = int(self.a[i][1])

        self.total = [0,0]
        for i in range(len(self.total)):
            self.total[i] = self.a[1][i] - self.a[0][i]

        if str(self.total[0])[0] == '-':
            self.total[0] += 12
        if str(self.total[1])[0] == '-':
            self.total[1] += 60
            self.total[0] -= 1

        self.duration = f"{self.total[0]} hr {int(self.total[1])} min"
        return self.duration

       
    def add_time(self, total_hours, total_minutes): # This should now be able to run without calculate() needing to run first.

        self.total_hours = total_hours
        self.total_minutes = total_minutes


        hours = int(str(self.total_minutes / 60).split('.')[0])
        self.total_hours += hours
        minutes = self.total_minutes - (60 * hours)
        self.total_minutes = minutes

        self.total_time = [self.total_hours, self.total_minutes]


        self.duration = f"{self.total_time[0]} hr {int(self.total_time[1])} min"

        return self.duration

       

# m2 = Timelog()
# m2.calculate("01/21/2022", "4:30", "10:20")

