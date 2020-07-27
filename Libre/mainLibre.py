'''
Libre is a virtual Reading List assistant
created by ya boi rayendito
jangan di hack ya
bikinnya susah – gadeng, thanks to tubes IF1210 :>
'''

import csv, newBook, saveFile

#to keep it running
endProgram = False

#converting from txt to list
with open('toBeRead.txt') as bookData:
    csv_reader = csv.reader(bookData, delimiter =',')
    yourList = [row for row in csv_reader]

print("Here's your list :\n")
for book in yourList:
    print(book[0]+', by '+book[1])
print()

while (not endProgram):
    command = str(input("your wish iz my command :"))
    if command == "new":
        yourList = newBook.newBuku(yourList)
        saveFile.writeFile('toBeRead.txt', yourList)
    if command == "show books":
        for book in yourList:
            print(book[0]+', by '+book[1])
        print()
    if command == "exit":
        print("Happy Reading")
        endProgram = True