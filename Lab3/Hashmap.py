class SymbolTable:
    def __init__(self):
        self.hashtable = {}
        self.capacity = 1
        self.hashNumber = 3

    def hashFunction(self, word):
        _sum = 0
        for i in word:
            _sum = _sum + ord(i)
        return _sum % self.hashNumber

    def add(self, word):
        key = self.hashFunction(word)
        if key not in self.hashtable.keys():
            self.hashtable[key] = []
        if self.search(word) != -1:
            return
        self.hashtable[key].append(word)

    def search(self, word):
        key = self.hashFunction(word)
        list_ = self.hashtable[key]
        for i in range(0, len(list_)):
            if list_[i] == word:
                return i * self.hashNumber + key
        return -1

    def getValue(self, word):
        key = self.hashFunction(word)
        for x in self.hashtable[key]:
            if x == word:
                return x
        return None

    def getOrAdd(self, word):
        key = self.hashFunction(word)
        if key not in self.hashtable.keys():
            self.hashtable[key] = []
        if self.search(word) != -1:
            return self.search(word)
        self.hashtable[key].append(word)
        return self.search(word)


if __name__ == '__main__':
    symbolTable = SymbolTable()
    symbolTable.add('iulia')
    symbolTable.add('ailui')
    symbolTable.add('mar')
    symbolTable.add('ram')
    symbolTable.add('aliga')
    symbolTable.add('aliga')
    print(symbolTable.hashtable)
    print(symbolTable.search('iulia'))
    print(symbolTable.search('mar'))
    print(symbolTable.getValue('aliga'))
    print(symbolTable.getValue('i'))
    print (symbolTable.getOrAdd("ii"))