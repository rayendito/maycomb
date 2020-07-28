'''
Libre is a virtual Reading List assistant
created by ya boi rayendito
jangan di hack ya
bikinnya susah – gadeng, thanks to tubes IF1210 :>
'''

import csv, newBook, saveFile, deleteBook

#to keep it running
endProgram = False

#converting from txt to list
with open('toBeRead.txt') as bookData:
    csv_reader = csv.reader(bookData, delimiter =',')
    yourList = [row for row in csv_reader]
print("\nHello, welcome to Libre, your virtual reading list assistant")
print("Here's your list :\n")
for book in yourList:
    print(book[0]+', by '+book[1])
print()

while (not endProgram):
    command = str(input("your wish iz my command : "))
    print()
    if command == "add":
        yourList = newBook.newBuku(yourList)
    if command == "delete":
        yourList = deleteBook.delete(yourList)
    if command == "show":
        print()
        for book in yourList:
            print(book[0]+', by '+book[1])
        print()
    if command == "exit":
        saveFile.writeFile('toBeRead.txt', yourList)
        print("Happy Reading :)\n")
        endProgram = True