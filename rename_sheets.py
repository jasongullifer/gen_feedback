import os
import sys
from gen_feedback import readStudents
import re

# Enter directory that contains the assignments to be renamed
ass_dir = "A1_corrected"

#Enter a list of student files
students_files = ["ECS_students_1-4_W23.csv", "ECS_students_5-8_W23.csv"]

# Loop through the student files, and read each file. Append it to a list.
students = []
for file in students_files:
    students.append(readStudents(file, delimiter=","))

# For each section of students. Search for a text file without the id number (e.g., based on name alone), and rename with the ID number
old_names = os.listdir(ass_dir)
os.chdir(ass_dir)
for section in students:
    for student in section: 
        search_string = student['Student.name'] + " " + student['Student.first.name']
        matching = [name for name in old_names if search_string in name]
        if len(matching) == 1:
            os.replace(matching[0], student['Student.name'] + "_" + student['Student.first.name'] + "_" + student['Student.number'] + ".txt")
        elif len(matching)==0:
            print("Couldn't find match for: ", student['Student.name'], student['Student.first.name'], student['Student.number'])
        else:
            print("Too many matches for: ", student['Student.name'], student['Student.first.name'], student['Student.number'])

