nu = input("Enter a number ")

try:
	nu = int(nu)

#Handels valueError 
except ValueError as e:
	print(e)

#Catching all un handeled errors
except Exception as e:
	print(e)

#Runs if no exception
else:
	print("No exception")

#Runs at the end no matter the exception
finally:
	print("By by")


	# try:
	#     statements # statements that can raise exceptions
	# except:
	#     statements # statements that will be executed to handle exceptions
	# else:
	#     statements # statements that will be executed if there is no exception
	# finally:
	#     statements # statements that will be executed every time
