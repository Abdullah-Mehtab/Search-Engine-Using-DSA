class HashTable():
    def __init__(self, size = 10):
        self.hash_table = [[] for _ in range(size)]

    def hash_key(self, keyword):
        return hash(keyword) % len(self.hash_table)

    def insert(self, keyword, url):
        # If word already exists, add URL to it
        if self.search(keyword) != None:
            self.search(keyword).append(url)
            return
        # Else, continue normally and insert in hash_table
        keyword_i = self.hash_key(keyword)
        keyword_exists = False
        bucket = self.hash_table[keyword_i]
        urlist = [url]

        for i, kv in enumerate(bucket):
            k, v = kv
            if k == keyword:
                keyword_exists = True
                break
        if keyword_exists:
            bucket[i] = (keyword, urlist)
        else:
            bucket.append((keyword, urlist))

    def search(self, keyword):
        keyword_i = self.hash_key(keyword)
        bucket = self.hash_table[keyword_i]
        for i, kv in enumerate(bucket):
            k, v = kv
            if k == keyword:
                return v
        return None

    def printer(self):
        for i in self.hash_table:
            for j in i:
                print(j)

# ht = HashTable()
# ht.insert("word","san.com")
# ht.insert("life","san.com")
# ht.insert("life","xyz.com")
# ht.insert("word","abc.com")
# ht.insert("Unique","ich.com")
# ht.insert("word","xyz.com")
# ht.printer()