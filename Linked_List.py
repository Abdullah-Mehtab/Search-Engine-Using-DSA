class Node:
    def __init__(self, keyword = "", url = "", next_node=None, prev_node=None):
        self.keyword = keyword
        self.urlist = [url]
        self.next = next_node
        self.prev = prev_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, keyword, url):
        temp = self.head
        while temp:
            if temp.keyword == keyword:
                temp.urlist.append(url)
                return
            temp = temp.next
        
        new_node = Node(keyword,url)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def search(self, word):
        temp = self.head
        flag = 0
        while temp:
            if temp.keyword == word:
                flag = 1
                break
            temp = temp.next
            if temp == None:
                break

        return temp.urlist if (flag == 1) else (None)

    def delete(self, key):
        if (self.head == None):
            return
        if(self.head.data) == key and (self.head.next == self.head):
            self.head = None
        head = self.head
        d = None
        if(self.head.data == key) :
            while(head.next != self.head):
                head = head.next
            head.next = (self.head).next
            self.head = head.next
        while(head.next != self.head and head.next.data != key):
            head = head.next
        if(head.next.data == key) :
            d = head.next
            head.next = d.next
        else:
            print("Doesn't Exist")
        return self.head

    def printer(self):
        temp = self.head
        if self.head is None:
            print("[ ]")
            return
        else:
            print("[")
            while (True):
                if temp.next != None:  
                    print(f"{temp.keyword}: {temp.urlist}") #end=", ") 
                if (temp.next == None):
                    break
                temp = temp.next
            print(f"{temp.keyword}: {temp.urlist}")
        print(']\n')
