import csv
print("Your List")
print()
with open('toBeRead.txt') as bookData:
    csv_reader = csv.reader(bookData, delimiter =',')
    baris_count = 0
    for baris in csv_reader:
        if baris_count == 0:
            print("List by Title, Author")
            baris_count += 1
        else:
            print(baris[0]+', by '+baris[1])

        