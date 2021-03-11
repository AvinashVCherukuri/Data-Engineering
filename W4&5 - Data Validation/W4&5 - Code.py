import pandas as pd
import numpy as np
import matplotlib.pyplot as plot


# Data for In Class Activity
data = pd.read_csv('OR-HighWay26-CrashData-2019.csv')

# Print all the data
#print(data, "Number of Rows in Data: ", len(data))


# Restructuring Data into Multiple DataFrames
CrashDF = data[data['Record Type'] == 1]
CrashesDF = CrashDF.dropna(axis=1, how='all')
#print(CrashesDF)

VehiclesDF = data[data['Record Type'] == 2]
VehiclesDF = VehiclesDF.dropna(axis=1, how='all')
#print(VehiclesDF)

ParticipantsDF = data[data['Record Type'] == 3]
ParticipantsDF = ParticipantsDF.dropna(axis=1, how='all')
#print(ParticipantsDF)


# Validating Assertions (Line 28 to 70)
# Checks if Crash ID Exists for each record or not
CrashIDExists = data[data['Crash ID']!="NaN"]
#print(CrashIDExists)

# Checks if Record Type Exists for each record or not
RecordTypeExists = data[data['Record Type']!="NaN"]
#print(RecordTypeExists)

# Checks if Age for every record is in between 0 to 9
AgeInLimitOrNot = data['Age'].between(0.0, 9.0)
#print(AgeInLimitOrNot.all())

# Checks if Week Day Code for every record is in between 1 to 7
WeekCodeInLimit = data['Week Day Code'].between(1.0, 7.0)
#print(WeekCodeInLimit.all())

# Prints the total number of persons involved in Crash
TotalPersonsInvolved = CrashesDF['Total Pedestrian Count'] + CrashesDF['Total Pedalcyclist Count'] + CrashesDF['Total Unknown Non-Motorist Injury Count'] + CrashesDF['Total Vehicle Occupant Count']
#print(TotalPersonsInvolved)

# Prints all the records with a latitude of 45 Degrees
Degrees45 = CrashesDF[CrashesDF['Latitude Degrees'] == 45.0]
#print(Degrees45)

# Prints all the records with Latitude in between 17 to 41 minutes
Minutes17to41 = CrashesDF['Latitude Minutes'].between(17.0, 41.0)
#print(Minutes17to41)

# Prints the list of Unique Vechicle IDs involved in Crashes
CrashedVehicles = VehiclesDF['Vehicle ID'].unique().tolist()
#print(len(CrashedVehicles))

# Prints the list of Unique Participants IDs involved in Crashes
CrashedParticipants = ParticipantsDF['Participant ID'].unique().tolist()
#print(len(CrashedParticipants))

# Checks if Every crash has a Country Code
CrashAndCountry = CrashesDF[['Crash ID','County Code']]
#print(CrashAndCountry.isnull(), CrashAndCountry.isnull().all())

# Checks if Every crash has a Vehicle Code
CrashAndVehicle = VehiclesDF[['Crash ID','Vehicle ID']]
#print(CrashAndVehicle.isnull(), CrashAndVehicle.isnull().all())

# Counts the total crashes happened in each month
CrashesInMonth = CrashesDF['Crash Month'].value_counts()
#print(CrashesInMonth)


# Get all the Values from Column 2 of CrashesInMonth
Temporary = []
for i in range(1,13) :
    Temporary.append(CrashesInMonth[i])
#print(Temporary)

Month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Plots a graph for total number of crashes in each month
#plot.bar(Month, Temporary)
#plot.xlabel("Month")
#plot.ylabel('Crashes Count')
#plot.title('OR HighWay 26 Crash Data for 2019 by Month')
#plot.show()


# Counts the total crashes happened in each day of the week for the year
CrashesInWeek = CrashesDF['Week Day Code'].value_counts()
#print(CrashesInWeek)

Temporary.clear()
for i in range(1,8):
  Temporary.append(CrashesInWeek[i])
#‹print(Temporary)

Day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# Plots a graph for total number of crashes in each day of the week
#plot.bar(Day, Temporary)
#plot.xlabel("Day")
#plot.ylabel('Crashes Count')
#plot.title('OR HighWay 26 Crash Data for 2019 by Day of the Week')
#plot.show()


# Resolving the Age assertion violation by dropping the records
AgeViolation = ParticipantsDF.dropna(subset=['Age'])
NoAgeViolation = AgeViolation['Age'] != "NaN"
NoAgeViolation = AgeViolation['Age'].between(0.0, 9.0)
#print(NoAgeViolation, NoAgeViolation.all())