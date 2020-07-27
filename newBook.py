def newBuku(yourList):

    #input buku baru
    title = str(input("Masukkan judul buku : "))
    author = str(input("Sokap tuch yang nulis : "))
    bukuBaru = [[str(title), str(author)]]

    #add new book to list
    yourList = yourList + bukuBaru

    #print success statement
    print("Successfully added "+title+" by "+author+" to your list\n")
    
    return yourList
