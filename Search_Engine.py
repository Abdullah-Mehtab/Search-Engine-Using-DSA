# Used to import OS functions
import os
# Used to import HTML from a file to the program
import codecs
# Used to convert HTML into text (customizable)
import html2text
# Calculate time
import time
# Data Structures to be Used
from Linked_List import LinkedList
from Binary_Search_Tree import BST
from AVL_Tree import AVL
from Hash_Table import HashTable
from Triee import Trie

class SearchEngine:
    def __init__(self,directory,mode):
            self.directory = directory
            self.mode = mode
            self.data_structure = [] # Default
            self.Loading()

    def GetStructure(self):
        if self.mode == 1:
            # self.data_structure = LinkedList()
            return LinkedList()
        elif self.mode == 2:
            # self.data_structure = BST()
            return BST()
        elif self.mode == 3:
            # self.data_structure = AVL()
            return AVL()
        elif self.mode == 4:
            # self.data_structure = HashTable()
            return HashTable()
        elif self.mode == 5:
            # self.data_structure = Trie()
            return Trie()

    def Loading(self):
        starting = time.time()
        self.data_structure = self.GetStructure()
        nURL = 0
        for file_name in os.listdir(self.directory):
            # Joining the directory with the file
            full_path = os.path.join(self.directory, file_name)
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
                page = h.handle(file.read())
                wordlist = page.split()
                for i in range(len(wordlist)):
                    # Iterage through every word and make it a lowercase word
                    wordlist[i] = wordlist[i].lower()
                # Removing Duplicates (function inside the text_cleaner()) then cleaning the words (removing non-existing words)
                final_wordlist = self.text_cleaner(list(dict.fromkeys(wordlist)))
                for alfaz in final_wordlist:
                    self.data_structure.insert(alfaz,file_name)
                # Increase number of total URLs
                nURL += 1
        #---------------------------------------------------------------
        ending = time.time()

        # self.data_structure.printer() # Printer for LL and HashTable || InOrder for BST/AVL || AutoComplete for Trie

        print(f"\nFiles loaded successfully. {nURL} URLs loaded from the folder " + self.timer(starting,ending))

    def search(self,word=None):
        if word == None:
            print("Error! Please Enter a word to search.")
            return
        starting = time.time()
        results = self.data_structure.search(word)
        ending = time.time()

        if results != None:
            print(f"{len(results)} result(s) found " + self.timer(starting,ending))

        return results
        
    def timer(self,start,end):
        total_milliseconds = (end - start) * 1000
        total_seconds = total_milliseconds / 1000
        minutes = int(total_seconds / 60)
        seconds = int(total_seconds - minutes * 60)
        milliseconds = int(total_milliseconds % 1000)
        minutes_str = (f"{minutes} minute(s) ") if (minutes > 0) else ("")
        seconds_str = (f"{seconds} second(s) and ") if (seconds > 0) else ("")
        return f"in {minutes_str}{seconds_str}{milliseconds} milliseconds."

    def text_cleaner(self,listy):
        try:
            for i in listy:
                if len(i) == 1:
                    listy.remove(i)
            listy.remove('###')
            listy.remove('---|---')
            listy.remove('inc.,')
        except:
            pass
        finally:
            return listy