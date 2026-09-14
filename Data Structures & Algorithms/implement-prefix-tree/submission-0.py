class TrieNode:
    def __init__(self):
        self.end_of_word = False
        self.nodes = [None] * 26
    
    def contains_key(self, ch):
        return self.nodes[ord(ch) - ord('a')] != None

    def get(self, ch):
        return self.nodes[ord(ch) - ord('a')]
    
    def put(self, ch, node):
        self.nodes[ord(ch) - ord('a')] = node
    
    def isEnd(self):
        return self.end_of_word

    def setEnd(self):
        self.end_of_word = True

class PrefixTree:

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        temp = self.node
        for i in range(len(word)):
            if not temp.contains_key(word[i]):
                temp.put(word[i], TrieNode())
            temp = temp.get(word[i])
        
        temp.setEnd()

    def search(self, word: str) -> bool:
        temp = self.node
        for i in range(len(word)):
            if not temp.contains_key(word[i]):
                return False
            temp = temp.get(word[i])
        
        return temp.isEnd()

    def startsWith(self, word: str) -> bool:
        temp = self.node
        for i in range(len(word)):
            if not temp.contains_key(word[i]):
                return False
            temp = temp.get(word[i])
        
        return True
        
        