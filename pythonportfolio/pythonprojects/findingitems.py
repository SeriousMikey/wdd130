largest_chapters = 0
largest_book = ""

largest_bom_chapters = 0
largest_bom_book = ""

largest_choice_chapters = 0
largest_choice_book = ""

scriptures = ["Old Testament", "New Testament", "Book of Mormon", "Doctrine and Covenants", "Pearl of Great Price"]

with open("books_and_chapters.txt") as text_file:
    print("Press ENTER to see options")
    choice = input("Which scripture would you like to learn about? ")
    while choice == "":
        for option in scriptures:
            print(option)
        choice = input("Which scripture would you like to learn about? ")

    for line in text_file:
        line = line.strip()
        line = line.split(":")
        book = line[0]
        chapters = int(line[1])
        scripture = line[2]

        if choice.upper() == scripture.upper() and choice.upper() != "BOOK OF MORMON":
            new_choice = scripture
            if chapters > largest_choice_chapters:
                largest_choice_chapters = chapters
                largest_choice_book = book

        if scripture.upper() == "BOOK OF MORMON":
            # print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")
            if chapters > largest_bom_chapters:
                largest_bom_chapters = chapters
                largest_bom_book = book

        if chapters > largest_chapters:
            largest_chapters = chapters
            largest_book = book

    if choice.upper() != "BOOK OF MORMON":    
        print(f"In the {new_choice}, the largest book is {largest_choice_book} with {largest_choice_chapters} chapters.")
    print(f"The largest book in the Book of Mormon is {largest_bom_book} with {largest_bom_chapters} chapters.")
    print(f"The largest book overall is {largest_book} with {largest_chapters} chapters.")    