
# This file is separate because it was originally planned that all database-related 
# functions would be in a designated class located here, but that didn't come to 
# fruition. This may (and probably should) change in future versions.

import sqlite3

database_name = "tutoring.db"
location_db = "./data"
con = sqlite3.connect(f"{location_db}/{database_name}")
cursor = con.cursor()


class ListRefresh:
    def  __init__(self):
        pass

    def write_student_data(self, MYSID, FIRST, LAST, HANDLE, TAG, SUBJECT, DATE, TIME):
        cursor.execute("""insert into students ('mySID','first_name','last_name','discord_handle','discord_tag','subject','date','time')
        values ('%s','%s','%s','%s','%s','%s','%s','%s')""" % (MYSID, FIRST, LAST, HANDLE, TAG, SUBJECT, DATE, TIME))
        con.commit()

    def add_student_local(self):   
        cursor.execute("""
            SELECT ROWID FROM students
        """)
        self.all_student_ids = cursor.fetchall()
        self.student_id_local = str(max([student_id[0] for student_id in self.all_student_ids])) # Takes the maximum ROWID

        cursor.execute("""insert into local('student_id')
        values ('%s')""" % self.student_id_local)
        con.commit()

    def student_list(self):
        cursor.execute("""
            SELECT * FROM students
        """)
        self.student_check = cursor.fetchall()


datawrite = ListRefresh()
datawrite.student_list()

