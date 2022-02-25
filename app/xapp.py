import sys, time
from mainp1v2 import *
from widgetp2v2 import *
from addstudentp2v2 import *
from newstudentdbv2 import *
from tutorinfop2v2 import *
from studentinfop3v2 import *
from loghoursp4 import *
from xtimelog import *
from PyQt5.QtGui import QIcon
from xclip import *
from notesp5v2 import *                 #   [IN PROGRESS]

def strfdate():
    return time.strftime('%m/%d/%Y')

def strftime():
    return time.strftime('%H:%M:%S')

def realtime(convert):
    military = convert.split(':')
    if int(military[0]) >= 12:
        if military[0] == '12':
            return convert + " PM"
        elif int(military[0]) >= 13:
            military[0] = str(int(military[0]) - 12)
            return ':'.join(military) + " PM"
    else:
        return convert + " AM"

class Page1(Ui_MainWindow):
    def __init__(self, window):                     # [COMPLETE]
        self.setupUi(window)

        self.idList = []            # Contains student ids
        # Button Icons
        self.cancelButtonP1.setIcon(QIcon('icons/svg/cancel-47.svg'))
        self.submitButtonP1.setIcon(QIcon('icons/svg/check-mark-3.svg'))

        # Page 1 Buttons
        self.cancelButtonP1.clicked.connect(self.cancel_main)
        self.submitButtonP1.clicked.connect(self.info_check)

    def cancel_main(self):                          # [COMPLETE]
        # MainWindow.close() # Used when editing 
        app.exit()    # Use this when finished editing

    def info_check(self):                           # [COMPLETE] # firstrun
        if self.lineEdit_1.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '' and self.lineEdit_4.text() != '':
            if self.lineEdit_1.text().isalpha() and self.lineEdit_2.text().isalpha():
                if self.lineEdit_4.text().isnumeric():
                    if len(self.lineEdit_4.text()) == 4:
                        cursor.execute("""insert into tutor ('first_name','last_name','discord_handle','discord_tag','date','time')
                        values ('%s','%s','%s','%s','%s','%s') """ % (self.lineEdit_1.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), strfdate(), strftime()))
                        con.commit()
                        
                        cursor.execute("""
                            UPDATE firstrun
                            SET marker = '1'
                            WHERE marker = '0'
                        """)
                        con.commit()
                        self.page2()

                    else:
                        self.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Discord tag must be 4 digits.</span></p></body></html>")
                else:
                    self.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Discord tag must be numeric.</span></p></body></html>")
            else:
                self.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Name must be alphabetical.</span></p></body></html>")
        else:
            self.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">All fields required.</span></p></body></html>")

    def tutor_info(self):                           # [COMPLETE]
        cursor.execute("""
            SELECT * FROM tutor
        """)
        self.tutor = cursor.fetchall()

        self.first_name = self.tutor[0][1]
        self.last_name = self.tutor[0][2]
        self.discord_handle = self.tutor[0][3]
        self.discord_tag = self.tutor[0][4]

        self.ui_p2.tutorFirstName.setText(f"<html><head/><body><p align=\"center\"><span style=\" \">{self.first_name}</span></p></body></html>")
        self.ui_p2.tutorLastName.setText(f"<html><head/><body><p align=\"center\"><span style=\" \">{self.last_name}</span></p></body></html>")
        self.ui_p2.tutorDiscordHandle.setText(f"<html><head/><body><p align=\"center\"><span style=\" \">{self.discord_handle}</span></p></body></html>")
        self.ui_p2.tutorDiscordTag.setText(f"<html><head/><body><p align=\"center\"><span style=\" \">{self.discord_tag}</span></p></body></html>")

    def current_students(self):                     # [COMPLETE]
        self.studentNum = len(datawrite.student_check)
        for x in range(self.studentNum):
            if datawrite.student_check[x][1] not in self.idList:
                self.idList.append(datawrite.student_check[x][1])
                self.ui_p2.listWidget.addItem(f"{datawrite.student_check[x][1]}")   # Should now be Discord Handle + # + Discord Tag

    def page2(self):                                # [COMPLETE]

        self.Form_P2 = QtWidgets.QWidget()
        self.ui_p2 = Ui_Form_P2()
        self.ui_p2.setupUi(self.Form_P2)

        self.current_students()
        self.global_time()

        # Button Icons
        self.ui_p2.addStudentButton.setIcon(QIcon('icons/svg/add-49.svg'))
        self.ui_p2.editTutorButton.setIcon(QIcon('icons/svg/settings-88'))
        self.ui_p2.exportButton.setIcon(QIcon('icons/svg/export-91.svg'))

        # Page 2 Buttons
        self.ui_p2.addStudentButton.clicked.connect(self.page2_1)       # Allows page 2_1 to be opened
        self.ui_p2.editTutorButton.clicked.connect(self.edit_tutor)     # Allows tutor to edit their info
        self.ui_p2.listWidget.itemDoubleClicked.connect(self.page3)     # When you double click a student's name

        self.tutor_info()

        MainWindow.hide()
        self.Form_P2.show()    # Submit button opens page 2
        
    def page2_1(self):                              # [COMPLETE]
        self.Form_P2_1 = QtWidgets.QWidget()
        self.ui_p2_1 = Ui_Form_P2_1()
        self.ui_p2_1.setupUi(self.Form_P2_1)

        self.ui_p2_1.data_browser_0.setText(strfdate())
        self.ui_p2_1.data_browser_1.setText(strftime())

        # Button Icons
        self.ui_p2_1.cancelButtonP2_1.setIcon(QIcon('icons/svg/cancel-47.svg'))
        self.ui_p2_1.submitButtonP2_1.setIcon(QIcon('icons/svg/check-mark-3.svg'))

        # Page 2_1 Buttons
        self.ui_p2_1.cancelButtonP2_1.clicked.connect(self.cancel_add_student)
        self.ui_p2_1.submitButtonP2_1.clicked.connect(self.add_student)

        self.Form_P2.hide()
        self.Form_P2_1.show()

    def cancel_add_student(self):                   # [COMPLETE]
        self.Form_P2_1.hide()
        self.Form_P2.show()

    def add_student(self):                          # [COMPLETE]

        # new_student_id = self.ui_p2_1.data_browser_2.text()     # Why is this the only defined data browser variable?
        new_student_id = self.ui_p2_1.data_browser_5.text() + '#' + self.ui_p2_1.data_browser_6.text()

        if new_student_id not in [str(ID[1]) for ID in datawrite.student_check]:    # student_check imported from newstudentdb                                           
            if self.ui_p2_1.data_browser_5.text() != '':
                if self.ui_p2_1.data_browser_6.text() != '':
                    if self.ui_p2_1.data_browser_6.text().isnumeric():
                        if len(self.ui_p2_1.data_browser_6.text()) == 4:
                            #print("Student successfully added!")
                            date0 = self.ui_p2_1.data_browser_0.text() # date
                            time1 = self.ui_p2_1.data_browser_1.text() # time
                            mySID = self.ui_p2_1.data_browser_5.text() + '#' + self.ui_p2_1.data_browser_6.text() # mySID
                            first_name3 = self.ui_p2_1.data_browser_3.text() # first_name
                            last_name4 = self.ui_p2_1.data_browser_4.text() # last_name
                            discord_handle5 = self.ui_p2_1.data_browser_5.text() # discord_handle
                            discord_tag6 = self.ui_p2_1.data_browser_6.text() # discord_tag
                            subject7 = self.ui_p2_1.data_browser_7.text() # subject
                            
                            datawrite.write_student_data(mySID, first_name3, last_name4, discord_handle5, discord_tag6, subject7, date0, time1)
                            datawrite.add_student_local()   # Adds student to the table "local"
                            datawrite.student_list()
                            self.ui_p2_1.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:792; color:#00a800;\">Student successfully added!</span></p></body></html>")

                            self.current_students()

                            self.Form_P2_1.hide()
                            self.Form_P2.show()

                        else:
                            # "Student Discord tag must be 4 digits."
                            self.ui_p2_1.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Student Discord tag must be 4 digits.</span></p></body></html>")
                    else:
                        # "Student Discord tag must be numeric."
                        self.ui_p2_1.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Student Discord tag must be numeric.</span></p></body></html>")
                else:
                    # "Student Discord tag required."
                    self.ui_p2_1.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Student Discord tag required.</span></p></body></html>")
            else:
                # "Student Discord required."
                self.ui_p2_1.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Student Discord required.</span></p></body></html>")
        else:
            # print("Student already exists!")
            self.ui_p2_1.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Student already exists!</span></p></body></html>")

    def edit_tutor(self):                           # [COMPLETE]
        self.Form_P2_0 = QtWidgets.QWidget()
        self.ui_p2_0 = Ui_Form_P2_0()
        self.ui_p2_0.setupUi(self.Form_P2_0)

        self.ui_p2_0.lineEdit_1.setText(self.first_name)
        self.ui_p2_0.lineEdit_2.setText(self.last_name)
        self.ui_p2_0.lineEdit_3.setText(self.discord_handle)
        self.ui_p2_0.lineEdit_4.setText(self.discord_tag)

        # Button Icons
        self.ui_p2_0.cancelButtonP1.setIcon(QIcon('icons/svg/cancel-47'))
        self.ui_p2_0.submitButtonP1.setIcon(QIcon('icons/svg/check-mark-3.svg'))

        # Edit Tutor Buttons
        self.ui_p2_0.cancelButtonP1.clicked.connect(self.cancel_edit_tutor)
        self.ui_p2_0.submitButtonP1.clicked.connect(self.update_tutor_info)

        self.Form_P2.hide()
        self.Form_P2_0.show()

    def cancel_edit_tutor(self):                    # [COMPLETE]
        self.Form_P2_0.hide()
        self.Form_P2.show()

    def update_tutor_info(self):                    # [COMPLETE]
        if self.ui_p2_0.lineEdit_1.text() != '' and self.ui_p2_0.lineEdit_2.text() != '' and self.ui_p2_0.lineEdit_3.text() != '' and self.ui_p2_0.lineEdit_4.text() != '':
            if self.ui_p2_0.lineEdit_1.text().isalpha() and self.ui_p2_0.lineEdit_2.text().isalpha():
                if self.ui_p2_0.lineEdit_4.text().isnumeric():
                    if len(self.ui_p2_0.lineEdit_4.text()) == 4:
                        self.new_first_name = self.ui_p2_0.lineEdit_1.text()
                        self.new_last_name = self.ui_p2_0.lineEdit_2.text()
                        self.new_discord_handle = self.ui_p2_0.lineEdit_3.text()
                        self.new_discord_tag = self.ui_p2_0.lineEdit_4.text()
                        self.date_updated = strfdate()
                        self.time_updated = strftime()

                        cursor.execute("""
                            UPDATE tutor
                            SET (first_name, last_name, discord_handle, discord_tag, date_updated, time_updated)
                            = ('%s','%s','%s','%s', '%s', '%s')
                            WHERE ROWID = '1'
                        """ % (self.new_first_name, self.new_last_name, self.new_discord_handle, self.new_discord_tag, self.date_updated, self.time_updated))
                        con.commit()

                        self.tutor_info()
                        self.Form_P2_0.hide()
                        self.Form_P2.show()

                    else:
                        self.ui_p2_0.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Discord tag must be 4 digits.</span></p></body></html>")
                else:
                    self.ui_p2_0.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Discord tag must be numeric.</span></p></body></html>")
            else:
                self.ui_p2_0.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">Name must be alphabetical.</span></p></body></html>")
        else:
            self.ui_p2_0.alert_info_error.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;color:#fc0107;\">All fields required.</span></p></body></html>")

    def page3(self):                                # [COMPLETE]
        self.Form_P3 = QtWidgets.QWidget()
        self.ui_p3 = Ui_Form_P3()
        self.ui_p3.setupUi(self.Form_P3)

        self.selected_student = self.ui_p2.listWidget.currentItem().text()
        self.selected_student_mySID = self.selected_student # Will help get the info from student database

        cursor.execute("""
            SELECT * FROM students
            WHERE mySID = '%s'
        """ % self.selected_student_mySID)

        self.selected_student_info = cursor.fetchall()
        self.student_id = self.selected_student_info[0][0] 
        self.student_mySID = self.selected_student_info[0][1]
        self.student_first_name = self.selected_student_info[0][2]
        self.student_last_name = self.selected_student_info[0][3]
        self.student_discord_handle = self.selected_student_info[0][4]
        self.student_discord_tag = self.selected_student_info[0][5]
        self.student_subject = self.selected_student_info[0][6]
        self.student_date_joined = self.selected_student_info[0][7]
        self.student_time_joined = self.selected_student_info[0][8]

        self.ui_p3.data_browser_0.setText(self.student_date_joined)
        self.ui_p3.data_browser_1.setText(self.student_time_joined)
        self.ui_p3.data_browser_3.setText(self.student_first_name)
        self.ui_p3.data_browser_4.setText(self.student_last_name)
        self.ui_p3.data_browser_5.setText(self.student_discord_handle)
        self.ui_p3.data_browser_6.setText(self.student_discord_tag)
        self.ui_p3.data_browser_7.setText(self.student_subject)

        self.student_discord_handle_tag = self.student_discord_handle + '#' + self.student_discord_tag

        self.show_student_logs()
        self.local_time()       # Updates the total time spent tutoring and displays it at the bottom of each student's page.
        # self.global_time()      # Updates the global time # May not be necessary here.

        # Button Icons
        self.ui_p3.newLogButtonP3.setIcon(QIcon('icons/svg/add-49.svg'))
        self.ui_p3.editStudentButton.setIcon(QIcon('icons/svg/settings-88.svg'))
        self.ui_p3.backButtonP3.setIcon(QIcon('icons/svg/back-22.svg'))

        # Page 3 Buttons
        self.ui_p3.backButtonP3.clicked.connect(self.back_button)           # When you press the "Back" button
        self.ui_p3.newLogButtonP3.clicked.connect(self.student_log)         # When you press the "New Log" button
        self.ui_p3.listWidgetP3.itemDoubleClicked.connect(self.new_log)     # When you double click a Log to edit

        self.Form_P2.hide()
        self.Form_P3.show()

    def back_button(self):                          # [COMPLETE]
        self.Form_P3.hide()
        self.Form_P2.show()

    def student_log(self):                          # [COMPLETE]

        self.last_student_log()
        self.last_start_time = strftime()
        self.last_date_of_session = strfdate()

        cursor.execute("""insert into hours ('student_id','log_id','start_time','date_of_session','date_log_created','time_log_created')
        values ('%s','%s','%s','%s','%s','%s')""" % (self.student_id, self.last_lognum + 1, self.last_start_time, self.last_date_of_session, self.last_date_of_session, self.last_start_time))
        con.commit()

        # Copies id info to notes table
        cursor.execute("""insert into notes ('student_id','log_id')
        values ('%s','%s')""" % (self.student_id, self.last_lognum + 1))
        con.commit()

        self.last_student_log()
        self.show_student_logs()

    def new_log(self):                              # [COMPLETE]

        self.Form_P4 = QtWidgets.QWidget()
        self.ui_p4 = Ui_Form_P4()
        self.ui_p4.setupUi(self.Form_P4)
        
        self.roomcheck = 0      # variable that will be used to determine which table to send the backtick string to

        self.edit_log()

        self.ui_p4.studentDiscordHandleTag.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;\">%s</span></p></body></html>" % self.student_discord_handle_tag)
        self.ui_p4.dateP4.setText(self.log_date_of_session)

        self.ui_p4.startTime.setTime(QtCore.QTime(self.log_start_time_hour, self.log_start_time_minute))

        if type(self.last_log_dict[self.selected_log]) == str:
            self.ui_p4.endTime.setTime(QtCore.QTime.currentTime())  # If an end time hasn't been submitted, the end time will be set to the current time.
            pass
        else:
            self.selected_end_time = self.last_log_dict[self.selected_log][1]
            self.selected_end_time_hour = self.selected_end_time.split(':')[0]
            self.selected_end_time_minute = self.selected_end_time.split(':')[1]
            self.ui_p4.endTime.setTime(QtCore.QTime(int(self.selected_end_time_hour), int(self.selected_end_time_minute)))

        self.ui_p4.commentBox.setPlainText(self.tick_string)
        self.ui_p4.volunteerTypeBoxP4.setCurrentText(self.log_volunteer_type)


        # Button Icons
        self.ui_p4.copyToClipboardButton.setIcon(QIcon('icons/svg/clipboard.svg'))
        self.ui_p4.submitButtonP4.setIcon(QIcon('icons/svg/check-mark-3.svg'))
        self.ui_p4.cancelButtonP4.setIcon(QIcon('icons/svg/cancel-47.svg'))
        self.ui_p4.calculateButtonP4.setIcon(QIcon('icons/svg/calculate-3.svg'))
        self.ui_p4.notesButtonP4.setIcon(QIcon('icons/svg/compose-11.svg'))    

        # Student Log Buttons
        self.ui_p4.calculateButtonP4.clicked.connect(self.calculate_time)
        self.ui_p4.cancelButtonP4.clicked.connect(self.cancel_log)
        self.ui_p4.submitButtonP4.clicked.connect(self.submit_log)
        self.ui_p4.copyToClipboardButton.clicked.connect(self.clipboard)
        self.ui_p4.notesButtonP4.clicked.connect(self.notes)

        self.Form_P3.hide()
        self.Form_P4.show()

    def convert_log_time(self, log_time):           # [INCOMPLETE] # Need to make '00:00:00' change to '12:00 AM' when converted

        self.military_time = log_time
        self.log_time = realtime(log_time)

        self.edit_log_num = self.log_time.split()[0]
        self.edit_log_start_time =  self.log_time.split()[1]

        self.edit_log_start_time_clean = self.edit_log_num[:-3] + ' ' + self.edit_log_start_time
        return self.edit_log_start_time_clean

    def edit_log(self):                             # [COMPLETE]

        self.selected_log = self.ui_p3.listWidgetP3.currentItem().text().split(':   ')[0].split()[1]
        # ^ This gets the log number from the selected item


        # This is where the function will convert the backtick back to an apostrophe
        # [Below this block of code.] [Below self.log_comment]
        cursor.execute("""
            SELECT * FROM hours
            WHERE student_id = '%s'
            AND log_id = '%s'
        """ % (self.student_id, self.selected_log))
        self.log_info = cursor.fetchall()

        self.log_ROWID = self.log_info[0][0]
        self.log_student_id = self.log_info[0][1]
        self.log_log_id = self.log_info[0][2]                   # Same as self.selected_log
        self.log_comment = self.log_info[0][3]
        self.log_start_time_unconverted = self.log_info[0][4]   # Unconverted time
        self.log_start_time_converted = self.convert_log_time(self.log_info[0][4])  # Converted time
        self.log_end_time = self.log_info[0][5]
        self.log_total_time = self.log_info[0][6]
        self.log_volunteer_type = self.log_info[0][7]
        self.log_date_of_session = self.log_info[0][8]
        self.log_tracklist = self.log_info[0][13]

        # Military time formatted from page 3 to be inserted into
        # the QTime by the hour and minute respectively.
        self.log_start_time_format = self.log_start_time_unconverted.split(':')[:-1]
        self.log_start_time_hour = int(self.log_start_time_format[0])
        self.log_start_time_minute = int(self.log_start_time_format[1])

        self.tickignore(self.log_tracklist, self.log_comment)

    def cancel_log(self):                           # [COMPLETE]
        self.Form_P4.hide()
        self.Form_P3.show()

    def last_student_log(self):                     # [COMPLETE]

        self.last_log_dict = {}     # Each time the "New Log" button is clicked, the dictionary is recreated.

        cursor.execute("""
            SELECT log_id FROM hours
            WHERE student_id = '%s'
        """ % self.student_id)
        self.last_log = cursor.fetchall()


        cursor.execute("""
            SELECT start_time FROM hours
            WHERE student_id = '%s'
        """ % self.student_id)
        self.last_start_list = cursor.fetchall()

        
        cursor.execute("""
            SELECT end_time FROM hours
            WHERE student_id = '%s'
        """ % self.student_id)
        self.last_end_list = cursor.fetchall()



        for i in range(len(self.last_log)):
            if self.last_end_list[i][0] == None:
                self.last_log_dict[str(self.last_log[i][0])] = self.last_start_list[i][0]
            else:
                self.last_log_dict[str(self.last_log[i][0])] = [self.last_start_list[i][0], self.last_end_list[i][0]]


        if self.last_log == []:
            self.last_lognum = 0
        else:
            self.last_lognum = self.last_log[-1][0]
   
    def show_student_logs(self):                    # [COMPLETE]

        cursor.execute("""
            SELECT total_time FROM hours
            WHERE student_id = '%s'
        """ % self.student_id)
        self.time_tutoring_student = cursor.fetchall()      # if the below conditional is a list, then it has a total_total time


        self.last_student_log()    # Used here for when used before the "New Log" button is pressed

        if self.ui_p3.listWidgetP3.count() == 0:                                                                                # I think I used 0 because I wasn't sure if the items would clear each time. 
            for num in self.last_log_dict:                                                                                      # UPDATE: Just confirmed that it (listWidgetP3) clears each time the page is hidden
                if type(self.last_log_dict[num]) == str:                                                                        
                    self.ui_p3.listWidgetP3.addItem(f"Log {num}:   {self.convert_log_time(self.last_log_dict[num])}")           
                    # print("Equal to string")
                else:
                    self.ui_p3.listWidgetP3.addItem(f"Log {num}:   {self.convert_log_time(self.last_log_dict[num][0])}   -   {self.convert_log_time(self.last_log_dict[num][1])}   -   {self.time_tutoring_student[int(num)-1][0]}")    
                    # print("Not equal to string")
        else:
            self.ui_p3.listWidgetP3.addItem(f"Log {self.last_lognum}:   {self.convert_log_time(self.last_start_time)}")

    def calculate_time(self):                       # [COMPLETE]

        tl.calculate(self.ui_p4.dateP4.text(),self.ui_p4.startTime.text()[:-3],self.ui_p4.endTime.text()[:-3])

        if str(tl.hqty[0])[0] == '-':
            tl.hqty[0] += 12

        self.ui_p4.totalTime.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;\">%s hr %s min</span></p></body></html>" % (tl.hqty[0], tl.hqty[1]))

    def update_total_time(self):                    # [COMPLETE]

        cursor.execute("""
            SELECT total_time FROM hours
            WHERE student_id = '%s'
            AND log_id = '%s'
        """ % (self.student_id, self.selected_log))
        self.time_tutoring_student = cursor.fetchall()
        self.log_total_time = self.time_tutoring_student[0][0]

    def update_end_time(self):                      # [COMPLETE]


        self.update_total_time()

        for item in self.ui_p3.listWidgetP3.selectedItems():
            item.setText(f"Log {self.selected_log}:   {self.convert_log_time(self.submit_start_time)}   -   {self.convert_log_time(self.submit_end_time)}   -   {self.log_total_time}")

    def local_time(self):                           # [COMPLETE]
        # Adds the time spent tutoring each student.
        # "self.log_total_time" is the total_time from the database 
        # each time a log is double clicked.

        cursor.execute("""
            SELECT total_time FROM hours
            WHERE student_id = '%s'
        """ % self.student_id)
        self.local_total_time = cursor.fetchall()


        if (None,) in self.local_total_time:
            z = True
            while z == True:
                self.local_total_time.remove((None,))
                if (None,) not in self.local_total_time:
                    z = False
                else:
                    pass

        self.local_total_time_list = [total[0].split(' min')[0].split(' hr ') for total in self.local_total_time]
        self.local_total_time_added = lambda n: sum([int(total[n]) for total in self.local_total_time_list])
        self.local_total_time_hour = self.local_total_time_added(0)
        self.local_total_time_minute = self.local_total_time_added(1)
        self.total_student_time = tl.add_time(self.local_total_time_hour, self.local_total_time_minute)


        cursor.execute("""
            UPDATE local
            SET (time_tutored)
            = ('%s')
            WHERE student_id = '%s'
        """ % (self.total_student_time, self.student_id))
        con.commit()

        self.ui_p3.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;\">Total:\t%s</span></p></body></html>" % self.total_student_time)

    def global_time(self):                          # [COMPLETE]
        # Adds the time spent tutoring all students.

        cursor.execute("""
            SELECT time_tutored FROM local
        """)
        self.student_totals = cursor.fetchall()


        if (None,) in self.student_totals:
            z = True
            while z == True:
                self.student_totals.remove((None,))
                if (None,) not in self.student_totals:
                    z = False
                else:
                    pass
        
        self.student_totals_list = [total[0].split(' min')[0].split(' hr ') for total in self.student_totals]
        self.student_totals_added = lambda n: sum([int(total[n]) for total in self.student_totals_list])
        self.student_totals_hour = self.student_totals_added(0)
        self.student_totals_minute = self.student_totals_added(1)
        self.grand_total = tl.add_time(self.student_totals_hour, self.student_totals_minute)


        cursor.execute("""
            UPDATE global
            SET (grand_total)
            = ('%s')
        """ % self.grand_total)
        con.commit()

        self.ui_p2.alert_file_exists.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:800;\">Time Logged:\t%s</span></p></body></html>" % self.grand_total)
    
    def format_time(self):                          # [COMPLETE]

        self.start_time = self.ui_p4.startTime.time()
        self.start_time_hour = self.start_time.hour()
        self.start_time_minute = self.start_time.minute()

        self.end_time = self.ui_p4.endTime.time()
        self.end_time_hour = self.end_time.hour()
        self.end_time_minute = self.end_time.minute()


        if len(str(self.start_time_hour)) == 1:
            self.start_time_hour = '0' + str(self.start_time_hour)

        if len(str(self.start_time_minute)) == 1:
            self.start_time_minute = '0' + str(self.start_time_minute)

        if len(str(self.end_time_hour)) == 1:
            self.end_time_hour = '0' + str(self.end_time_hour)

        if len(str(self.end_time_minute)) == 1:
            self.end_time_minute = '0' + str(self.end_time_minute)

        self.start_time_formatted = f"{self.start_time_hour}:{self.start_time_minute}:00"
        self.end_time_formatted = f"{self.end_time_hour}:{self.end_time_minute}:00"

    def submit_log(self):                           # [COMPLETE]

        # [Log Comment]
        # Clears backtick so the indices 
        # determining which backticks 
        # in the string need to remain 
        # backticks and not converted to apostrophes
        cursor.execute("""
            UPDATE hours
            SET backtick = NULL
            WHERE student_id = '%s'
            AND log_id = '%s'
        """ % (self.student_id, self.selected_log))


        self.calculate_time() 
        self.format_time()
        self.submit_comment = self.ui_p4.commentBox.toPlainText()
        self.submit_start_time = self.start_time_formatted
        self.submit_end_time = self.end_time_formatted
        self.submit_total_time = self.ui_p4.totalTime.text().split('>')[5][:-6]
        self.submit_volunteer_type = self.ui_p4.volunteerTypeBoxP4.currentText()
        self.submit_date_of_session = self.ui_p4.dateP4.text()
        self.submit_date_updated = strfdate()
        self.submit_time_updated = strftime()


        if self.submit_comment == '':
            pass
        else:
            self.submit_comment = self.comment_error(self.submit_comment)  # Fixes the apostrophe error
        
        # This is where the apostrophe convert function should be
        # [Above this block of code.]
        cursor.execute("""
            UPDATE hours
            SET (comment, start_time, end_time, total_time, volunteer_type, date_of_session, date_updated, time_updated)
            = ('%s','%s','%s','%s','%s','%s','%s','%s')
            WHERE student_id = '%s'
            AND log_id = '%s'
        """ % (self.submit_comment, self.submit_start_time, self.submit_end_time, self.submit_total_time, self.submit_volunteer_type, self.submit_date_of_session, self.submit_date_updated, self.submit_time_updated, self.student_id, self.selected_log))
        con.commit()


        self.last_student_log()
        self.update_end_time()
        self.local_time()       # Updates total_time spent tutoring the student 
        self.global_time()      # Updates the grand_total time spent tutoring  
        self.edit_log()         # Recreates the self.log_info list        
        self.cancel_log() 

    def discord_log(self):                          # [COMPLETE]
        # Don't use self.log_info because the copy to clipboard button
        # will be used before the log is submitted, thus before 
        # self.log_info is rewritten.
        
        # The commands below will work with the button
        #
        self.discord_name = self.first_name + ' ' + self.last_name[0]
        self.discord_date = ui.ui_p4.dateP4.text()
        self.discord_volunteer_type = ui.ui_p4.volunteerTypeBoxP4.currentText()
        self.calculate_time() # Need to be calculated before time can be used
        self.discord_duration = self.ui_p4.totalTime.text().split('>')[5][:-6]
        self.discord_comment = self.ui_p4.commentBox.toPlainText()

        self.discord_text = f"""Name: {self.discord_name}\nDate: {self.discord_date}\nVolunteer Type: {self.discord_volunteer_type}\nDuration: {self.discord_duration}\nComment: {self.discord_comment}"""

    def clipboard(self):                            # [COMPLETE] # Clipboard button  

        self.discord_log()

        write_to_clipboard(self.discord_text)

        self.ui_p4.copyToClipboardButton.setIcon(QIcon('icons/svg/success-62.svg'))

    def notes(self):                                # [COMPLETE]
        self.Form_P5 = QtWidgets.QWidget()
        self.ui_p5 = Ui_Form_P5()
        self.ui_p5.setupUi(self.Form_P5)

        self.roomcheck = 1

        # [Log Note]
        # Clears backtick so the indices 
        # determining which backticks 
        # in the string need to remain 
        # backticks and not converted to apostrophes

        cursor.execute("""
            SELECT note, backtick FROM notes
            WHERE student_id = '%s'
            AND log_id = '%s'
        """ % (self.student_id, self.selected_log))
        self.note_list = cursor.fetchall()                  

        self.pull_log_note = self.note_list[0][0]
        self.pull_log_note_idx = self.note_list[0][1]              

        self.tickignore(self.pull_log_note_idx, self.pull_log_note)

        self.ui_p5.noteBoxP5.setPlainText(self.tick_string)     

        # Button Icons
        self.ui_p5.cancelButtonP5.setIcon(QIcon('icons/svg/cancel-47.svg'))
        self.ui_p5.submitButtonP5.setIcon(QIcon('icons/svg/check-mark-3.svg'))

        # Page 5 Buttons
        self.ui_p5.cancelButtonP5.clicked.connect(self.cancel_note)
        self.ui_p5.submitButtonP5.clicked.connect(self.save_note)     

        self.Form_P4.hide()
        self.Form_P5.show()

    def cancel_note(self):                          # [COMPLETE]
        self.roomcheck = 0
        self.Form_P5.hide()
        self.Form_P4.show()

    def save_note(self):                            # [COMPLETE]

        cursor.execute("""
            UPDATE notes
            SET backtick = NULL
            WHERE student_id = '%s'
            AND log_id = '%s'
        """ % (self.student_id, self.selected_log))

        self.push_log_note = self.ui_p5.noteBoxP5.toPlainText()
        if self.push_log_note == '':
            pass
        else:
            self.push_log_note = self.comment_error(self.push_log_note)

        cursor.execute("""
            UPDATE notes
            SET note = '%s'
            WHERE student_id = '%s'
            AND log_id = '%s'
        """ % (self.push_log_note, self.student_id, self.selected_log))
        con.commit()

        self.cancel_note()
   
    def comment_error(self, comment_string):        # [COMPLETE]  [TO DATABASE] # converts apostrophes to backticks and saves the indices of backticks deliberately written
        self.comment_string = comment_string

        if "`" in self.comment_string:
            self.backtracker(self.comment_string)
            if self.roomcheck == 0:
                cursor.execute("""
                    UPDATE hours
                    SET (backtick)
                    = '%s'
                    WHERE student_id = '%s'
                    AND log_id = '%s'
                """ % (self.tracklist, self.student_id, self.selected_log))
                con.commit()
            elif self.roomcheck == 1:
                cursor.execute("""
                    UPDATE notes
                    SET (backtick)
                    = '%s'
                    WHERE student_id = '%s'
                    AND log_id = '%s'
                """ % (self.tracklist, self.student_id, self.selected_log))
                con.commit()

        if "'" in self.comment_string:
            self.comment_string = self.comment_string.replace(self.comment_string[self.comment_string.find("'")], "`")


        return self.comment_string

    def backtracker(self, tick):                    # [COMPLETE] [TO DATABASE] [BACKTICK TRACKER] # Tracks the indices of backticks in a string
        self.tick = tick
        self.tracklist = []
        num = 0
        for i in self.tick:
            if i == "`":
                self.tracklist.append(str(num))
            num += 1

        self.tracklist = ' '.join(self.tracklist)   

    def tickignore(self, tick_idx, tick_string):    # [COMPLETE] [FROM DATABASE] [BACKTICK TRACKER] 

        self.tick_idx = tick_idx
        self.tick_string = tick_string

        if self.tick_string == None or self.tick_string == '':
            pass

        elif self.tick_idx == None:
            if "`" in self.tick_string:
                self.tick_string = self.tick_string.replace("`","'")
                
        else:                                                   
            self.tick_int = [int(tick) for tick in self.tick_idx.split()]  
            self.tick_string = list(self.tick_string)
            for z in range(len(self.tick_string)):
                if z in self.tick_int:      # Skipping the indices of backticks written by the user
                    pass
                else:
                    if self.tick_string[z] == "`":  # If not the index list, the backtick is converted back to an apostrophe
                        self.tick_string[z] = "'"

            self.tick_string = ''.join(self.tick_string)


    # [IN PROGRESS]

    def export_logs(self):                          # [IN PROGRESS]

        #with open("exports/tutor_logs.json", "w"):

        self.main_dict = {}
        # self.idList # contains all student myUH IDs
        self.students = {}      # Student info 
        self.logs = {}          # Local student logs
        self.times = {}         # Local total times
        self.total = {}         # Grand total time
        self.tutor = {}         # Tutor info
        self.discord_logs = {}  # Discord logs to be submitted

    def update_student_info(self):                  # [IN PROGRESS]

        #if self.ui_p3.data_browser_

        pass
  
    def edit_student(self):                         # [IN PROGRESS]

        pass


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Page1(MainWindow)
tl = Timelog()  # imported 


cursor.execute("""
    SELECT * FROM firstrun
""")
marker = cursor.fetchall()
if marker[0][0] == '0':
    MainWindow.show()
else:
    ui.page2()


app.exec_() # Use this when finished editing

# %gui qt5 
# ipython --gui=qt5
# from xapp import *
# Enter %gui qt5 into the console after starting iPython 
# or start iPython using ipython --gui=qt5 
# to prevent iPython from blocking commands while program is running
