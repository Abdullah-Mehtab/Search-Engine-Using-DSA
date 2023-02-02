# from Extra.Dictionary_based.Search_Engine import SearchEngine # Dictionary based Search Engine
# from Extra.List_based.Search_Engine import SearchEngine # List based Search Engine
from Search_Engine import SearchEngine # Required Search Engine

def main():
    directory = input('Please enter a the name of a directory: ')
    Cdirectory = "HTMLs/" + directory

    mode = int(input('''\nEnter mode as in what data structure to use:
1. Linked List
2. Binary Search Tree
3. AVL
4. Hash Table
5. Trie
>> '''))

    print('\nBuilding Search Engine...')
    engine = SearchEngine(Cdirectory, mode)
    answer = 'y'
    while (answer == 'y'):
        term = input('\nSearch (enter a term to query): ')
        ranking = engine.search(term)
        print("Displaying results for " + "'" + term + "' (limited to 10):")
        if ranking is None:
            print('No results :(')
        else:
            rank = 1
            for doc in ranking:
                if rank == 11:
                    break
                print(str(rank) + '. ' + doc)
                rank += 1
            print()
        answer = ''
        while not (answer == 'y' or answer == 'n'):
            answer = input('Would you like to search another term (y/n) ')

if __name__ == '__main__':
    main()