
# Cougar-Log

Cougar-Log is a time-tracking software with a graphical user interface designed to be used by 
the tutors of CougarCS at the University of Houston. I had a rewarding 
experience being a CougarCS tutor during the fall 2021 semester, but maintaining 
well-organized information, notes, and most importantly, time logs was a bit 
of a struggle at first. This program isn't a complete solution by far, but 
it is a start and one that I am excited to use and happy to share.

Before getting into installation and operation details, I would like to say that this program is still in development with a few features that are currently inoperable. This includes a clickable, but functionless, export button and an editing student information button. There is also no way to remove logs once added, so I suggest setting the start and end time as the same time 
if its removal is desired. None of the buttons have labels but self-explanatory icons instead.


# Installation

macOS Big Sur Version 11.4 running Python 3.7.6 was used throughout the development of this project and the only dependency required from a new Python environment is PyQt5.


Assuming Python is already installed, below is an easy installation process. Upon opening the Terminal app:

```
git clone https://github.com/wajones2/Cougar-Log.git
cd Cougar-Log
source firstrun
./start
```

# Operation

The program opens with an information page tutors need to fill out. This will be used to conveniently produce the logs that are submitted in the CougarCS Tutoring "logging" channel. 

Once submitted, the next page is where new students are added. To add a student, click the "+" (icon) button at the bottom of the page. A separate page will appear with text boxes for Date, Time, First, Last, Handle (Discord), Tag (Discord), and Subject. Out of these, only First is required.

Once added, the previous page will reappear with the newly added student's first name and their index number in the window. Next, double click the student's name to open the logging page. To add a log, click the "+" button at the bottom of the page. This will automatically create a log with the start time shown in the window. To add an end time and other information, double click the start time to open the log edit page.

This page contains input methods labeled Date, Start, End, Total, Type (volunteer), and Comment. These are used not only for tracking the time spent tutoring students but also for creating the Discord logs. Once the correct times are entered, click the calculator (icon) button to view the total time. (Note: the calculator button isn't required to be clicked in order to submit logs.) In the right hand corner of the page is a note (icon) button that opens a page for taking notes. In order to save any notes taken, the submit (check mark icon) button must be clicked. To access these notes, the same note button must be clicked in the log edit page. When ready to submit the Discord logs, simply click the clipboard (icon) button to write the log to the clipboard. The submit button must be clicked to save the log. 

Above the "+" button is the time spent tutoring the respective student and above the previous is total time logged for all students. 
