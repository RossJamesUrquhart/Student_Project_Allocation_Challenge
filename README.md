# Modules needed in python

- numpy
- pandas
- datetime
- random


# The only lines that need changed within the python file (just right click and open in text editor) are:

- Line 14 - path to file of inputs (default: "Data/Project-Data.xlsx")

# Optional changes:

- Line 15 - Number of training epochs to complete (10,000 will take ~43 seconds, 100,000 around 10 minutes) the more the better

# This script assumes that:

- Inputs will be in the form of xlsx files
- Data within the xlsx file will be in the same format/order as the files originally given as inputs
		i.e. projects available, section and their capacity in the first sheet and the student choices in the second sheet


Once paths and options have been set this script can be ran in a terminal (or in spyder) of which the best epoch will be fed to a csv named 'Best_allocation.csv'

If a student leaves a choice blank, the script converts that to a 0

If a student gets their first choice a score of 1 is assigned, second choice gets 2 , third is 3, etc.

# Results

~~~~
========================================================================
The best score achieved was 133 and was acheived on epoch 4957
========================================================================
========================================================================
The following shows how the distribution of projects by order of choice:
[[1, 45], [2, 17], [3, 5], [4, 3], [5, 1], [7, 2], [8, 1]]
========================================================================
========================================================================
Of 85 students, 52.94% of students got their first pick
Of the remaining 40 students, 42.5% of students got their second pick
Of the remaining 23 students, 21.74% of students got their third pick
Of the remaining 18 students, 16.67% of students got their fourth pick
========================================================================
========================================================================
The following is the split of allocated projects by section:
13 projects in MCCB
20 projects in CaS
16 projects in MaCC
24 projects in BAC
1 projects in PACERS
========================================================================

Time elapsed = 562s
~~~~
