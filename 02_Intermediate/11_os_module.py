'''This is a script to show basic functions of os module'''
import os

# Get curent working directory 
print(os.getcwd())
# Make a directory
os.mkdir('NewDir')
# Chnage current working directory  
os.chdir('NewDir')

print(os.getcwd())
os.chdir('..')
print(os.getcwd())

# Rename directory
os.rename('NewDir', 'NewName')

# Delete directory
os.rmdir('NewName')