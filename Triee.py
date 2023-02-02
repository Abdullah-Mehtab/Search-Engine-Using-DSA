class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, url):
        prev_inserver = self.search(word)
        #if prev_inserver != None:
        if type(prev_inserver) == type([]):
            prev_inserver.append(url)
            return
        if type(self.search(word)) == type(list):
            self.search(word).append(url)
            return
        urlist = [url]
        temp = self.root
        for char in word:
            if type(temp.children.get(char)) == type(TrieNode()):
            # if temp.children.get(char):
                temp = temp.children[char]
            else:
                newNode = TrieNode()
                temp.children[char] = newNode
                temp = newNode
        temp.children["*"] = urlist

    def search(self,word):
        temp = self.autocompletehelper(word)
        if not temp:
            return None
        return self.searchhelper(temp)

    def searchhelper(self, node=None, word="", words=[]):
        temp = node
        for key, childNode in temp.children.items():
            if key == "*":
                words.append(word)
                return temp.children[key]
            else:
                self.collecting(childNode, word + key, words)
        return
        
    def collecting(self, node=None, word="", words=[]):
        temp = node or self.root
        for key, childNode in temp.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collecting(childNode, word + key, words)
        return words

    def searchAC(self,word):
        temp = self.autocompletehelper(word)
        temp = self.searchhelper(word)
        if temp == type(list):
            return False
        else:
            return True

    def autocomplete(self, prefix = ''):
        temp = self.autocompletehelper(prefix)
        if not temp:
            return None
        return self.collecting(temp)

    def autocompletehelper(self, word):
        temp = self.root
        for char in word:
            if type(temp.children.get(char)) == type(TrieNode()):
                temp = temp.children[char]
            else:
                return None
        return temp	

trie = Trie()


trie.insert("word","san.com")
trie.insert("life","san.com")
trie.insert("life","xyz.com")
trie.insert("word","abc.com")
trie.insert("Unique","ich.com")
trie.insert("word","xyz.com")

print(trie.autocomplete())
print("\nsearch")
print(trie.search('word'))

