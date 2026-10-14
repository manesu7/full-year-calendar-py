import calendar
import pyinputplus as inp

# This safely forces the user to enter a valid integer
year = inp.inputInt("Enter a year: ")

# Print the entire, e.g. year 2027 calendar
print(calendar.calendar(year))
