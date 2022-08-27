#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 19:27:39 2022

@author: samiwadho
"""
 #Assignment 3
# This program takes User Name and Subject Marks and prints a Marks Sheet

# Gather Input from User
name = input("Enter your Name: ")
Roll_No = input("Enter your Roll number: ")
marksPhysics = int(input("Enter Marks in Physics (out of 100): "))
marksChemistry = int(input("Enter Marks in Chemistry (out of 100): "))
marksMath = int(input("Enter Marks in Math (out of 100): "))
marksComputers = int(input("Enter Marks in Computers (out of 100): "))
marksUrdu = int(input("Enter Marks in Urdu (out of 100): "))
marksEnglish = int(input("Enter Marks in English (out of 100): "))



# Calculate Total Marks Obtained by the user
marksObtained = marksPhysics + marksChemistry + \
    marksMath + marksComputers + marksUrdu + marksEnglish

totalMarks = 600    # Using a hard coded value of 600, this is generally not a good idea
# Calculate the Percentage Marks
percentMarks = (marksObtained / totalMarks) * 100

# Calculate Grade
grade = "F"

# The elif keyowrd is short for Else If in Plain English
if percentMarks > 80:
    grade = "A"
elif (percentMarks<80 ):
    grade ="B"
elif(percentMarks<70):
    grade = "C"
elif(percentMarks<50):
    grade ="D"
else:
    grade = "F"     #this "else" is unecessary since grade is already default at F

# Print the mark sheet
# The \t is called a tab separator
# The \n is used for new line
# Either , or + can be used for strings but since we are taking input as numbers so + will not work

print("******************MARKS SHEET********************")
print("|\tStudent Name: \t\t", name,"\t\t|")
print("|\tStudent Roll Number:\t",Roll_No,"\t\t|")
print("|\tPhysics: \t\t", marksPhysics, "/ 100\t|")
print("|\tChemistry: \t\t", marksChemistry, "/ 100\t|")
print("|\tMath: \t\t\t", marksMath, "/ 100\t|")
print("|\tComputers: \t\t", marksComputers, "/ 100\t|")
print("|\tUrdu: \t\t\t", marksUrdu, "/ 100\t|")
print("|\tEnglish: \t\t", marksEnglish, "/ 100\t|")
print("|\t\t\t\t\t\t|")
print("|\tMarks Obtained: \t", marksObtained, "/", totalMarks,"\t|")
print("|\tPercentage: \t\t", round(percentMarks, 2),"\t\t|")
print("|\tGrade: \t\t\t", grade,"\t\t|")
print("*************************************************")

