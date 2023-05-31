#Modules needed in python

- numpy
- pandas
- datetime
- random


#The only lines that need changed within the python file (just right click and open in text editor) are:

- Line 14 - path to file of inputs (default: "Data/Project-Data.xlsx")

#Optional changes:

- Line 15 - Number of training epochs to complete (10,000 will take ~43 seconds, 100,000 around 10 minutes) the more the better

#This script assumes that:

- Inputs will be in the form of xlsx files
- Data within the xlsx file will be in the same format/order as the files originally given as inputs
		i.e. projects available, section and their capacity in the first sheet and the student choices in the second sheet


# Once paths and options have been set this script can be ran in a terminal of which the best epoch will be fed to a csv named 'Best_allocation.csv'

