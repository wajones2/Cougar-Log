import sqlite3

database_name = "tutoring.db"
location_db = "./data"
con = sqlite3.connect(f"{location_db}/{database_name}")
cursor = con.cursor()

# column "backtick" in the hours and notes tables track the backticks to keep when converting back to apostrophes

cursor.execute("""create table if not exists tutor (ROWID integer primary key autoincrement, myUH text, first_name text, last_name text, discord_handle text, discord_tag text, date text, time text, date_updated text, time_updated text)""")
cursor.execute("""create table if not exists students (ROWID integer primary key autoincrement, myUH text, first_name text, last_name text, discord_handle text, discord_tag text, subject text, date text, time text, date_updated text, time_updated text)""") # Table of just students
cursor.execute("""create table if not exists hours (ROWID integer primary key autoincrement, student_id text, log_id integer, comment text, start_time text, end_time text, total_time text, volunteer_type text, date_of_session text, date_log_created text, time_log_created text, date_updated text, time_updated text, backtick text)""") # total is in minutes
cursor.execute("""create table if not exists firstrun (marker text)""")
cursor.execute("""create table if not exists local (ROWID integer primary key autoincrement, student_id text, time_tutored text)""")
cursor.execute("""create table if not exists global (ROWID integer primary key autoincrement, grand_total text)""")
cursor.execute("""create table if not exists notes (ROWID integer primary key autoincrement, student_id text, log_id integer, note text, backtick text)""")

cursor.execute("""insert into firstrun ('marker')
values ('%s')""" % 0)
con.commit()

cursor.execute("""insert into global ('grand_total')
values ('0 hr 0 min')""")
con.commit()
