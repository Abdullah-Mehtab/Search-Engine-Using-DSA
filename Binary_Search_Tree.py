class temp:
    def __init__(self, keyword, url):
        self.left = None
        self.right = None
        self.parent = None
        self.keyword = keyword
        self.urlist = [url]
        self.count = 1

class BST:
    def __init__(self):
        self.root = None

    def inOrderHelper(self, temp):
        if temp == None:
            return
        self.inOrderHelper(temp.left)
        print(f"[{temp.keyword} : {temp.urlist}]") #,end=" ")
        self.inOrderHelper(temp.right)

    def inOrder(self):
        self.inOrderHelper(self.root)

    def insertHelper(self, keyword, url, temp):
        if keyword < temp.keyword and temp.left == None:
            temp.left = temp(keyword, url)
            temp.left.parent = temp
        elif keyword > temp.keyword and temp.right == None:
            temp.right = temp(keyword, url)
            temp.right.parent = temp
        if keyword < temp.keyword:
            self.insertHelper(keyword, url, temp.left)
        elif keyword > temp.keyword:
            self.insertHelper(keyword, url, temp.right)

    def insert(self, keyword, url):
        temp = self.root
        while temp is not None:
            if temp.keyword == keyword:
                temp.urlist.append(url)
                return
            if temp.keyword > keyword:
                temp = temp.left
            else:
                temp = temp.right

        if self.root == None:
            self.root = temp(keyword, url)
        else:
            temp = self.root
            if keyword == temp.keyword:
                (temp.count) += 1
                return
            self.insertHelper(keyword, url, self.root)

    def search(self, value):
        temp = self.root
        while temp is not None:
            if temp.keyword == value:
                return temp.urlist
            if temp.keyword > value:
                temp = temp.left
            else:
                temp = temp.right
        return None


# bst = BST()
# bst.insert("word","san.com")
# bst.insert("life","san.com")
# bst.insert("life","xyz.com")
# bst.insert("word","abc.com")
# bst.insert("Unique","ich.com")
# bst.insert("word","xyz.com")

# bst.inOrder()