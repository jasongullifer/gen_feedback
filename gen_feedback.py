# Generate student feedback sheets (for Omnivox/Lea). Omnivox expects the
# student ID numbers to be contained in the filename. This program uses a
# delimited text file containing student names and ids to create the text
# feedback files. It can also instead create multiple copies of a template file,
# following the naming conventions (e.g., for making copies of a rubric that can
# be uploaded as  student feebdack). 

# Jason Gullifer

import csv
import os
import sys
import shutil

def readStudents(txt_file = "", delimiter=","):
	"""
	Read students from a text file (txt_file) w/ delimiters (delimiter).
	"""
	with open(txt_file, newline = '') as students_file:
		student_reader = csv.reader(students_file, delimiter=delimiter)
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
	""" Reads a file that contains text to be placed inside the generated text files (such
	as assignment headings / parts)."""
	with open(txt_file, newline = "") as headings_file:
		lines = headings_file.readlines()	
	lines = "".join(lines)
	print(lines)
	return lines

def tryDir(assg):
	"""
	Attempt to create a directory for the assignment (assg). If the directory
	does not exist, it is created and the function returns False. If the
	directory exists, no directory is created and the function returns True.
	"""
	if not os.path.exists(assg):
		print("--- Creating a directory " + assg + ".")
		os.makedirs(assg)
		return False
	else:
		return True

def writeStudentSheets(students, assg, headings):
	"""
	Write individual student sheets for each student (from students argument).
	The sheets are output to the assg directory.
	"""
	
	orig_path = os.getcwd()
	print("--- Changing directory to " + assg + ".")
	os.chdir(assg)

	print("--- Creating " + str(len(students)) + " student files.")

	for student in students:
		headString = student["Student.name"].replace(" ", "-") + "_" + student["Student.number"] + "_" + assg
		file = open(headString + ".txt", "w")
		file.writelines([headString + "\n", headings, "\n\n", "0/100"])
		file.close()
	os.chdir(orig_path)
	print("--- Changing directory back to " + orig_path + ".")

def copyFeedbackFile(students, assg, templateFile):
	"""
	Use a file (e.g., word file or excel file) as a template, and make a copy of
	that file for each student.
	"""
	orig_path = os.getcwd()
	print("--- Changing directory to " + assg + ".")
	os.chdir(assg)

	print("--- Creating " + str(len(students)) + " student files.")

	for student in students:
		headString = student["Student.name"].replace(" ", "-") + "_" + student["Student.number"] + "_" + assg
		extension = os.path.splitext(templateFile)[1]
		shutil.copyfile("../"+templateFile, headString+extension)
	
	os.chdir(orig_path)
	print("--- Changing directory back to " + orig_path + ".")


if __name__ == "__main__":
	""" 
	Prompt the user for information and then proceed with one of two program
	modes. Either create a bunch of text files for each student, or copy a
	template file for each student. Otherwise, prompt for the assignment name.
	Check whether the assignment directory exists. If it does not exist, create
	the directory and student files. Otherwise, do nothing to prevent
	overwriting existing sheets.
	"""

	prog_mode = input("(1) Generate feedback text files; (2) Make copies of a template file (e.g., PDF)?; or (Q) to quit: ")

	while prog_mode != "Q" and prog_mode != "q":
		txt_file = input("Enter the full path for the student text file: ")
		assg = input("Enter the assignment name (e.g., A2): ")
		dirExists = tryDir(assg)
		students = readStudents(txt_file, )

		if dirExists:
			print("--- Directory " + assg + " exists. Not creating student files to prevent overwriting!\n--- Enter a unique assignment name.")
		elif (prog_mode == "1"):
			headings = input("Enter the full path for the headings file or leave blank: ")
			if headings != '':
				headings = readHeadings(headings)
			writeStudentSheets(students, assg, headings)
		elif (prog_mode == "2"):
			templateFile = input("Enter the full path for the feedback template file: ")
			copyFeedbackFile(students, assg, templateFile)
		else: 
			print("--- Invalid program mode")
		prog_mode = input("(1) Generate feedback text files; (2) Copy feedback from a template file?; or (Q) to quit: ")
