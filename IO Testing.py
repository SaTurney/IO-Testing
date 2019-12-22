#IO Testing.py
#August 28, 2018
#Sabrina Turney
#This program demonstrates both input and output

def main():
    #Declare and initialize variables (give starting values)
    #string called StudentID - I use CamelCase convention for variables in this program.
    StudentID = ""
    #int called GPA 
    GPA = 0
    #string called Class
    Class = ""

    #Introduction
    print("Welcome to my program!\n") #\n shortcut to skip a line - newline

    #Prompt user for their Student ID
    #Assign the variable StudentID a new value for input in one step
    StudentID = input("Please enter your student ID: ")

    #Prompt for GPA
    #When prompting for a numeric value, use eval function
    GPA = eval(input("Please enter your GPA: "))

    #Prompt user for their class name
    #Assign the variable Class a new value for input in one step
    Class = input("Please enter the name of your class: ")

    #Display user's input info on the screen
    #Student ID: 00334394
    #GPA: 4.0
    #Class: COP1000
    #The \n moves to a new line, then the word for Name: appears, then \t is  a new tab.
    #All this is in "", so it will print to the screen as output.
    #Comma to separate what we're typing from the value of the variable printing.

    print("\nStudent ID\tGPA\tClass")    #\t is new tab, separates three input value headers.
    print(f'{StudentID}\t{GPA}\t{Class}')
    #f to format input correctly (avoiding issues with int, float, str variables)
