'''This is a program to illustrate if elif else statements in python'''

AGE = int(input("Enter your age : "))

if AGE < 18:
    print("You are a minor")
elif AGE == 18:
    print("You are 18 years old")
else:
    print("You are an adult")
