# - ProblemSet3.py *- coding: utf-8 -*-
"""
Problem 3_1:
Write a function that reads a text file and counts the number of characters in 
it.  Print both the text file and the number of characters. Do this so that the 
printout isn't doubled space (use an end=""  argument in the print statement). 
Also, skip a line before printing the count. Note that it is easy to get the 
number of characters in each line using the len() function.
Here is my run for HumptyDumpty.txt.  Let me point out one thing that is not
visible here and is a bit technical.  At the end of each of the first three
lines there is a <newline> character.  These are invisible.  If you do the count
by eye, you are likely to come up short by these three characters, but they
are visible to len() and you should count them -- they are part of the 141
"letters" in the humptydumpty.txt file.  Counting them makes this an easier 
function for you to write.

Your output should look just like this for the autograder:

problem3_1("humptydumpty.txt")
Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall.
All the king's horses and all the king's men
Couldn't put Humpty together again.

There are 141 letters in the file.

"""
#%%
def problem3_1(txtfilename):
    #write your file name, for example, "HumptyDumpty.txt"
    infile = open(txtfilename)
    linect = 0
    wordct = 0
    charct = 0
    for line in infile:
        print(line, end="") # the file has "\n" at the end of each line already
    infile.close() 
    #countin letters in the file
    cfile=open(txtfilename)
    for line in cfile:           # step through each line in the text file
        linect = linect + 1
        for word in line.split():    # split into a list of words
            wordct = wordct + 1
        charct = charct + len(line)

    cfile.close() 
    print("\n")         
    print("There are",charct,"letters in the file" )