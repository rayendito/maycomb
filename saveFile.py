import csv
def writeFile(filename, yourList):
    with open(filename, mode='w', newline='') as fileBuku:
        books = csv.writer(fileBuku)
        for row in yourList:
            books.writerow(row)


