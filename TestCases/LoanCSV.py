import csv


DataFile = open("C:\\Users\\Admin\\PycharmProjects\\API_BookStore\\Utilities\\CSVData.csv")
ReadCSV = csv.reader(DataFile)

print(next(ReadCSV))
Namelist = []
for row in ReadCSV:
    if row[1] == "Approved":
        Namelist.append(row[0])

print("ApprovedLoans :",Namelist)

# WriteData = open("C:\\Users\\Admin\\PycharmProjects\\API_BookStore\\Utilities\\CSVData.csv","a")
# Wr = csv.writer(WriteData)
# Wr.writerow(['hulk','Rejected'])


print("Total no of rows : ",ReadCSV.line_num)
