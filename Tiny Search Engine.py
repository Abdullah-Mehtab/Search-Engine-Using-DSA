# Used to import OS functions
import os
# Used to import HTML from a file to the program
import codecs
# Used to convert HTML into text (customizable)
import html2text
# Calculate time
import time
# LL
from Linked_List import LinkedList

def timer(start,end):
    total_milliseconds = (end - start) * 1000
    total_seconds = total_milliseconds / 1000
    minutes = int(total_seconds / 60)
    seconds = int(total_seconds - minutes * 60)
    milliseconds = int(total_milliseconds % 1000)
    minutes_str = (f"{minutes} minute(s) ") if (minutes > 0) else ("")
    seconds_str = (f"{seconds} second(s) and ") if (seconds > 0) else ("")
    return f"in {minutes_str}{seconds_str}{milliseconds} milliseconds."

def text_cleaner(listy):
    try:
        for i in listy:
            if len(i) == 1 and i != 'a':
                listy.remove(i)
        listy.remove('###')
        listy.remove('---|---')
        listy.remove('inc.,')
        listy.remove('*[v]:')
        listy.remove('*[t]:')
        listy.remove('*[e]:')
    except:
        pass
    finally:
        return listy

directory = input("Enter Directory: ")

"""
1) Import all HTML files
2) Iterate through each file, extract proper data from the file and 
   merge it into a massive list (for all keywords in all files)
3) After extraction, iterate through the list of all keywords and 
   search for all the URLS each one resides in (Searching a very long amount of lists and URLS)
4) Store it into the selected data structure
5) Store into a main-variable (dictionary/list) so it can be iterable
6) Searching for the given keyword inside the data-structure and return a list of all URLS of that WORD
"""
starty = time.time()
Link = LinkedList()
nURL =  0
Cdirectory = "HTMLs/" + directory
# Iterate over files in that directory
for file_name in os.listdir(Cdirectory):
    # Joining the directory with the file
    full_path = os.path.join(Cdirectory, file_name)
    # checking if it is a proper file 
    if os.path.isfile(full_path):
        # If proper file is detected
        # Start importing HTML
        file = codecs.open(full_path, "r", "utf-8") 
        h = html2text.HTML2Text()
        # Ignoring the links and images inside the HTML
        h.ignore_links = True
        h.ignore_images = True
        # Extracting all the proper text in proper format to a variable
        # 1 Page per URL
        page = h.handle(file.read())
        # Extracting a list of all words from the given page
        wordlist = page.split()
        for i in range(len(wordlist)):
            # Iterage through every word and make it a lowercase word
            wordlist[i] = wordlist[i].lower()
        # Removing Duplicates (function inside the text_cleaner()) then cleaning the words (removing non-existing words)
        final_wordlist = text_cleaner(list(dict.fromkeys(wordlist)))
        for alfaz in final_wordlist:
            Link.insert(alfaz,file_name)
        # Increase number of total URLs
        nURL += 1

Link.printer()

endy = time.time()
print(f"\nFiles loaded successfully. {nURL} URLs loaded from the folder "+timer(starty,endy))

# Testing
x = 'y'
while x == 'y':
    wordd = input("\nEnter word to search: ")
    startt = time.time()
    results = Link.search(wordd)
    endd = time.time()

    if results == None:
        print("No Results found.")
    else:
        print(f"{len(results)} result(s) found {timer(startt,endd)}")
        displayURLs = 10 if (len(results) > 10) else len(results)
        print(f"Displaying first {displayURLs} URLs.\n")
        for i in range(displayURLs):
            print(str(i+1)+".",results[i])
    results = None
    x = ''
    while not (x == 'y' or x == 'n'):
        x = input('Would you like to search another term (y/n) ')