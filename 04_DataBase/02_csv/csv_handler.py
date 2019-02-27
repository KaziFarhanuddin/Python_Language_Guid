import csv

# Read Method 1 -> Using simple read
with open('data.csv') as file:
    readCSV = csv.reader(file, delimiter=',')
    for row in readCSV:
        print(row[0], row[1])
print()


# Read Method 2 -> Using DictReader
''' 
	This has a optional parameter "fieldnames"
		if not supplied it uses 'first wor' as keys 
'''
with open('data.csv') as file:
    readCSV = csv.DictReader(file, delimiter=',')
    for row in readCSV:
        print(row)
        # print(row['NAME'], row["AGE"])
print()


# Write/Append Method 1 -> writerow / writerows
# Hear newline='' is used to avoid newlines to be inserted in the file 
with open('data.csv', 'w', newline='') as file:
    writerCSV = csv.writer(file, delimiter=',')
    # writerCSV.writerow(['A',18])
    writerCSV.writerows([['A', 18], ['L', 21]])
print()


# Write/Append Method 2 -> DictWriter to make writer object
with open('data.csv', 'w', newline='') as file:
    writerCSV = csv.DictWriter(file, delimiter=',', fieldnames=['NAME', 'AGE'])
    # writerCSV.writerow({'NAME':'A','AGE':18})
    writerCSV.writerows([{'NAME': 'A', 'AGE': 18}, {'NAME': 'L', 'AGE': 21}])
