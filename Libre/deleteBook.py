def delete(yourList):
    print("Which book do you want to delete?\n")
    index = 1
    for book in yourList:
        print('['+str(index)+'] '+str(book[0])+' by '+str(book[1]))
        index += 1
    which = int(input("\nAnswer with number : "))
    print()
    theBook = yourList[(which-1):which]
    #print(theBook) This Line Is A Testament of Debugging
    confirm = input("Are you sure you want to remove "+theBook[0][0]+" by "+theBook[0][1]+"? (Y/N) : ")
    print()
    if confirm == "Y":
        del yourList[(which-1):which]
        print("Successfully deleted "+theBook[0][0]+" by "+theBook[0][1])
    elif confirm == "N":
        print("Until I feared I would lose it, I never loved to read")
    return yourList