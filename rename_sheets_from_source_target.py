import os
import sys
from gen_feedback import readStudents
import re

student_files = []
file = open("a1_replacements.txt","r")
for line in file:
    student_files.append(line.strip("\n").split("\t"))

file.close()

ass_dir = "A1_corrected"
os.chdir(ass_dir)

for student in student_files:
    os.rename(student[0], student[1] + str(".txt"))
