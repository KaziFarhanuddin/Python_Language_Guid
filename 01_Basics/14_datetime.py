import datetime

today_date = datetime.date.today().strftime("%d-%b-%Y")
time = datetime.datetime.now().time().strftime("%H-%M-%S")

# print(time)
# print(today_date)





# Find difference between 2 dates
	# Just make sure they are in same format
	# 	if not use strftime()
d1 = datetime.datetime.now()
d2 = datetime.datetime.now()

# d3 = (d1-d2)
# print(d3)
# print(d3.days)





# Convert str to datetime obj
datetime_object = datetime.datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
# print(datetime_object)





# Some more substractions
d1 = datetime.datetime.now().strftime("%b %d %Y %I:%M%p")
d1 = datetime.datetime.strptime(d1, '%b %d %Y %I:%M%p')
d2 = datetime.datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

d3 = (d1-d2)
# print(d3)
# print(dir(d3))
