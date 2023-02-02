class Node:
    def __init__(self, keyword, url):
        self.left = None
        self.right = None
        self.parent = None
        self.keyword = keyword
        self.urlist = [url]
        self.height = 1
        self.count = 1

class AVL:
    def __init__(self):
        self.root = None

    def inOrderHelper(self, temp):
        if temp == None:
            return
        self.inOrderHelper(temp.left)
        print(f"[{str(temp.keyword)} : {temp.urlist}]") #h: {temp.height} c: {temp.count}]")
        self.inOrderHelper(temp.right)

    def inOrder(self):
        self.inOrderHelper(self.root)

    def getHeight(self, temp):
        if temp == None:
            return 0
        else:
            return temp.height

    def leftRotation(self, node):
        try:
            parent = node.parent
            rightChild = node.right
            node.right = rightChild.left
            if node.right is not None:
                node.right.parent = node
            rightChild.left = node
            node.parent = rightChild
            if parent is None:
                self.root = rightChild
            elif parent.left == node:
                parent.left = rightChild
            else:
                parent.right = rightChild
            rightChild.parent = parent
        except:
            return
    def rightRotation(self, node):
        try:
            parent = node.parent
            leftChild = node.left
            node.left = leftChild.right
            if node.left is not None:
                node.left.parent = node
            leftChild.right = node
            node.parent = leftChild
            if parent is None:
                self.root = leftChild
            elif parent.left == node:
                parent.left = leftChild
            else:
                parent.right = leftChild
            leftChild.parent = parent
        except:
            return
    def recomputeHeight(self, temp):
        if temp is not None:
            temp.height = 1+max(self.getHeight(temp.left), self.getHeight(temp.right))

    def checkForBalance(self, temp):
        while temp is not None: #Loop to go to parent until you reach the root
            balance = self.getHeight(temp.right) - self.getHeight(temp.left)
            if balance == -2:
                leftChild = temp.left
                leftChildBalance = self.getHeight(leftChild.right) -  self.getHeight(leftChild.left) 
                if leftChildBalance <= 0:
                    #Right rotation:
                    self.rightRotation(temp)
                    self.recomputeHeight(temp.left)
                    self.recomputeHeight(temp.right)
                    self.recomputeHeight(temp)
                else:
                    #1. Left rotation on leftChild
                    self.leftRotation(leftChild)
                    #2. Right rotation on temp
                    self.rightRotation(temp)
                    self.recomputeHeight(temp.left)
                    self.recomputeHeight(temp.right)
                    self.recomputeHeight(temp)
                break
            elif balance == 2:
                rightChild = temp.right
                rightChildBalance = self.getHeight(rightChild.left) - self.getHeight(rightChild.right)
                if rightChildBalance <= 0:
                    #Left rotation:
                    self.leftRotation(temp)
                    self.recomputeHeight(temp.left)
                    self.recomputeHeight(temp.right)
                    self.recomputeHeight(temp)
                else:
                    #1. Right rotation on rightChild
                    self.rightRotation(rightChild)
                    #2. Left rotation on temp
                    self.rightRotation(temp)
                    self.recomputeHeight(temp.left)
                    self.recomputeHeight(temp.right)
                    self.recomputeHeight(temp)
                break
            self.recomputeHeight(temp)
            temp = temp.parent

    def insertHelper(self, keyword, url, temp):
        if (temp == None):
            return
        if keyword < temp.keyword and temp.left == None:
            temp.left = Node(keyword, url)
            temp.left.parent = temp
            self.checkForBalance(temp)
        elif keyword > temp.keyword and temp.right == None:
            temp.right = Node(keyword, url)
            temp.right.parent = temp
            self.checkForBalance(temp)

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
            self.root = Node(keyword, url)
        else:
            temp = self.root
            if keyword == temp.keyword:
                (temp.count) += 1
                return
            self.insertHelper(keyword, url, self.root)

    def search(self, value):
        node = self.root
        while node is not None:
            if node.keyword == value:
                return node.urlist
            if node.keyword > value:
                node = node.left
            else:
                node = node.right
        return None

# avl = AVL()
# avl.insert("word","san.com")
# avl.insert("life","san.com")
# avl.insert("life","xyz.com")
# avl.insert("word","abc.com")
# avl.insert("Unique","ich.com")
# avl.insert("word","xyz.com")

# avl.inOrder()