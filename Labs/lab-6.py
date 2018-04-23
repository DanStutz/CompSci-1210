#!/usr/local/anaconda/bin/python
######################################################################
# YOUR NAMES GO HERE
# YOUR (SHARED) DISCUSSION SECTION (e.g., "A09") GOES HERE
######################################################################

# I certify that the entirety of this file contains only my own work
# and/or that of my assigned partner. I also certify that my partner 
# and I have not shared the contents of this file with anyone in any form.

######################################################################
# Replace "hawkid1", "hawkid2" in the tuple in the function below with
# your own hawkids USING LOWER CASE CHARACTERS ONLY.
#
# ATTENTION: Your hawkid is your login name for ICON, it is not
# your student ID number. 
#
# Failure to correctly do so will result in a 0 grade.
#
# If you are a three-partner group, change the second line to read
#   return(("hawkid1", "hawkid2", "hawkid3"))
# and edit as appropriate.
######################################################################
def hawkid():
    return(("hawkid1", "hawkid2"))

######################################################################
# Write a good comment here.
class Student():
    def __init__(self, name):
        self.name = name		# e.g., "CS1210"
        self.transcript = {}		# My enrollments

    # Simplify what gets printed.
    def __repr__(self):
        return('<Student: {}>'.format(self.name))

    ##################################################################
    # Manipulate the student's transcript to reflect enrollment.
    def enroll(self, c):
        pass

    ##################################################################
    # Manipulate the student's transcript to reflect withdrawl.
    def drop(self, c):
        pass

######################################################################
# Write a good comment here.
class Class():
    def __init__(self, name, cap = 30):
        self.name = name	        # e.g., "Joe"
        self.cap = cap			# Course enrolment cap
        self.roster = {}		# Students in course
        self.waitlist = []		# Students on waitlist

    # Simplify what gets printed.
    def __repr__(self):
        return('<Class: {}>'.format(self.name))

    ##################################################################
    # Method to enroll given student in this class. Make sure you
    # don't exceed the course enrollment cap; you'll need to check the
    # roster for students still marked active. Any student attempting
    # to enroll beyond the cap should be added to the course waitlist
    # instead. Important: once enrolled, make sure you invoke the
    # Student.enroll() method to update the student object as well.
    def enroll(self, student):
        pass

    ##################################################################
    # Method to drop given student in this class. If there are
    # students still on the waitlist, they should be automatically
    # enrolled. Students who drop should remain on the roster but
    # should be marked inactive. Important: once withdrawn, make sure
    # you invoke the Student.drop() method to update the student
    # object as well.
    def drop(self, student):
        pass
