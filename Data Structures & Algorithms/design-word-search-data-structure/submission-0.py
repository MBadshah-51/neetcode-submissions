class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        temp = self.node

        for i in range(len(word)):
            if word[i] not in temp.children:
                temp.children[word[i]] = TrieNode()
            temp = temp.children[word[i]]
        temp.end_of_word = True
        

    def search(self, word: str) -> bool:
        
        def dfs(idx, node):
            temp = node

            for i in range(idx, len(word)):
                if word[i] == ".":
                    for child in temp.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                
                else:
                    if word[i] not in temp.children:
                        return False
                    temp = temp.children[word[i]]
            
            return temp.end_of_word

        return dfs(0, self.node)