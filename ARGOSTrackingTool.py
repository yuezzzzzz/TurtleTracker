#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Yue Zhang (yz833@duke.edu)
# Date:   Fall 2023
#--------------------------------------------------------------

# Task 3: Read the data directly from the ARGOS file
# Parse Data
# Copy and paste a line of data as the lineString variable value
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"
  
# Use the split command to parse the items in lineString into a list object
lineData = lineString.split()
  
# Assign variables to specfic items in the list
record_id = lineData[0]   # ARGOS tracking record ID
obs_date = lineData[2]   # Observation date
ob_lc = lineData[4]       # Observation Location Class
obs_lat = lineData[6]     # Observation Latitude
obs_lon = lineData[7]     # Observation Longitude
  
# Print information to the use
print (f"Record {record_id} indicates Sara was seen at {obs_lat}N and {obs_lon}W on {obs_date}")

#Create a variable pointing to the data file
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Pretend we read one line of data from the file
lineString = line_list[200]

#Split the string into a list of data items
lineData = lineString.split()

#Extract items in list into variables
record_id = lineData[0]
obs_date = lineData[2]
obs_lc = lineData[4]
obs_lat = lineData[6]
obs_lon = lineData[7]

#Print the location of sara
print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#Task 4a Process all lines in the ARGOS file using a for loop
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

for lineString in line_list[17:]:
    lineData = lineString.split()
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

for lineString in line_list:
    #check if the line is a data line
    if lineString[0] in ('#', 'u'):
        continue
    lineData = lineString.split()
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#Task 4b: Process all lines in the ARGOS fiel using a while loop
#Read contents of file into a list
lineString = file_object.readline()

#while loop
##Iterate through lines
while lineString:
    if lineString[0] in ('#', 'u'):
        lineString = file_object.readline() # go to the next item in the line string before continue. Otherwise it will stay in the first line
        continue
    lineData = lineString.split()
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")
    #Move to the next line
    lineString = file_object.readline()
#Close the file
file_object.close()

#Task5: Building Python dictionaries of ARGOS observations
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Initialize dictionaries
date_dict = {}
location_dict = {}

#For loop
for lineString in line_list:
    #check if the line is a data line
    if lineString[0] in ('#', 'u'):
        continue
    lineData = lineString.split()
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Add items to dictionaries
    date_dict[record_id] = obs_date
    location_dict[record_id] = (obs_lat, obs_lon)
    
    #print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#Task6: Filtering records added to our dictionary
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Initialize dictionaries
date_dict = {}
location_dict = {}

#For loop
for lineString in line_list:
    #check if the line is a data line
    if lineString[0] in ('#', 'u'):
        continue
    lineData = lineString.split()
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Determine if location class criteria is met
    if obs_lc in ("1", "2", "3"):
        #Add items to dictionaries
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
    
    #print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")

#Task7: Displaying information of a user-specified ARGOS observation
#Task7.1: Asking the user to specify a date
#Ask user for a date
user_date = input("Enter a date: ")

#Create a variable pointing to the data file
file_name = './data/raw/Sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contents of file into a list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Initialize dictionaries
date_dict = {}
location_dict = {}

#For loop
for lineString in line_list:
    #check if the line is a data line
    if lineString[0] in ('#', 'u'):
        continue
    lineData = lineString.split()
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_lon = lineData[7]

    #Determine if location class criteria is met
    if obs_lc in ("1", "2", "3"):
        #Add items to dictionaries
        date_dict[record_id] = obs_date
        location_dict[record_id] = (obs_lat, obs_lon)
    
#Initialize key list
keys = []

#Loop through items in date_dict
for item in date_dict.items():
    key = item[0]
    value = item[1]
    if value == user_date:
        keys.append(key)

#Loop through keys and report locations
for key in keys:
    location = location_dict[key]
    lat = location[0]
    lon = location[1]
    print(f"On {user_date}, Sara the turtle was seen at {lat}d Lat, {lon}d Lgn")
    