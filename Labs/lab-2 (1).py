#!/usr/local/anaconda/bin/python
######################################################################
# Noah Landon, Daniel Stutz
# A08
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
#   return(("", "", "hawkid3"))
# and edit as appropriate.
######################################################################
def hawkid():
    return(("nrlandon", "dstutz"))

######################################################################
# Write a good comment here.
def minByMax(L):
    return((min(L),)*(max(L))+ (max(L),)*(min(L)))

######################################################################
# Write a good comment here.
def insertString(S, i, j, U):
    return()

######################################################################
# Write a good comment here.
def findUnique(T):
    return(T)

######################################################################
# Write a good comment here.
def inflateCenter(L, k):
    return(max,k*[0])

########################################################
### AutoGrader Feedback
### Honor code declaration is likely correct.
### Warning: Each function should have meaningful comments.
'''

**********************************************************************
File "../lab2test.py", line 21, in __main__
Failed example:
    insertString('abcdefghijk', 0, 3, 'WXYZ')
Expected:
    'WXYZdefghijk'
Got:
    ()
**********************************************************************
File "../lab2test.py", line 24, in __main__
Failed example:
    insertString('abcdefghijk', 100, 100, 'WXYZ')
Expected:
    'abcdefghijkWXYZ'
Got:
    ()
**********************************************************************
File "../lab2test.py", line 27, in __main__
Failed example:
    insertString('', 0, 0, 'a')
Expected:
    'a'
Got:
    ()
**********************************************************************
File "../lab2test.py", line 30, in __main__
Failed example:
    insertString('', 0, 0, '')
Expected:
    ''
Got:
    ()
**********************************************************************
File "../lab2test.py", line 33, in __main__
Failed example:
    findUnique(range(0))
Expected:
    []
Got:
    range(0, 0)
**********************************************************************
File "../lab2test.py", line 45, in __main__
Failed example:
    inflateCenter(list(range(5,9)), 3)
Expected:
    [5, 6, 0, 0, 0, 8]
Got:
    (<built-in function max>, [0, 0, 0])
**********************************************************************
File "../lab2test.py", line 48, in __main__
Failed example:
    inflateCenter([1], 6)
Expected:
    [0, 0, 0, 0, 0, 0]
Got:
    (<built-in function max>, [0, 0, 0, 0, 0, 0])
**********************************************************************
File "../lab2test.py", line 51, in __main__
Failed example:
    inflateCenter([1, 2], 0)
Expected:
    [1]
Got:
    (<built-in function max>, [])
**********************************************************************
File "../lab2test.py", line 54, in __main__
Failed example:
    inflateCenter([1, 2, 3], 0)
Expected:
    [1, 3]
Got:
    (<built-in function max>, [])
**********************************************************************
1 items had failures:
   9 of  16 in __main__
***Test Failed*** 9 failures.
'''

### Hawkid: nrlandon
### Hawkid: dstutz
### Score: 7
