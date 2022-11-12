import csv
import os
import sys

def readStudents(txt_file = ""):
	"""Read students from a tab-delimited text file (txt_file).
	"""
	with open(txt_file, newline = '') as students_file:
		student_reader = csv.reader(students_file, delimiter='\t')
		header = next(student_reader)
		#print(header)
		students = []
		for student in student_reader:
			ln = student[0]
			fn = student[1]
			sid = student[2]
			students.append({header[0]: ln, header[1]: fn, header[2]: sid})
	return students

def readHeadings(txt_file = ""):
	with open(txt_file, newline = "") as headings_file:
		lines = headings_file.readlines()	
	lines = "".join(lines)
	print(lines)
	return lines

def tryDir(assg):
	"""Attempt to create a directory for the assignment (assg). If the directory does not exist, 
	it is created and the function returns False. If the directory exists, no directory is created 
	and the function returns True.
	"""
	if not os.path.exists(assg):
		print("Creating a directory " + assg + ".")
		os.makedirs(assg)
		return False
	else:
		return True

def writeStudentSheets(students, assg, headings):
	"""Write individual student sheets for each studend (from students argument). The sheets are 
	output to the assg directory.
	"""
	print("Changing directory to " + assg + ".")
	os.chdir(assg)

	print("Creating " + str(len(students)) + " student files.")

	for student in students:
		headString = student["Student.name"].replace(" ", "-") + "_" + student["Student.number"] + "_" + assg
		file = open(headString + ".txt", "w")
		file.writelines([headString + "\n", headings, "\n\n", "0/100"])
		file.close()

if __name__ == "__main__":
	"""Check whether there are any system arguemnts. If yes, assume it's the assignment name for the directory. 
	Otherwise, prompt for the assignment name. Check whether the assignment directory exists. If it does not exist, 
	create the directory and student files. Otherwise, do nothing to prevent overwriting existing sheets.
	"""
	if len(sys.argv) > 1:
		txt_file = sys.argv[1]
		assg = sys.argv[2]
		headings = sys.argv[3]
	else:
		txt_file = input("Enter the full path for the student text file: ")
		assg = input("Enter the assignment (e.g., A2): ")
		headings = input("Enter the full path for the headings file: ")
	
	dirExists = tryDir(assg)

	if not dirExists:
		students = readStudents("students.txt")
		headings = readHeadings("parts.txt")
		writeStudentSheets(students, assg, headings)
	else:
		print("Directory " + assg + " exists. Not creating student files to prevent overwriting!\nEnter a unique assignment name.")
	

