# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

class TrieNode:
    
    #trie node class
    
    def __init__(self):
        self.children = [None] * 26
        
        self.isEndOfWord = False
        
class Trie:
    
    #Trie data structure class 
    def __init__(self):
        self.root = self.getNode()
        
    def getNode(self):
        
        #Returns new trie node (initialized to NULLs)
        return TrieNode()
        
    def _charToIndex(self, ch):
        return ord(ch)-ord('a')
        
    def insert(self,key):
        
        #if not present, inserts key into trie
        #if key is prefix of trie node, mark as leaf node
        
        current_root = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            
            #if index not in current root children, then create a new trie add assign to index
            if not current_root.children[index]:
                current_root.children[index] = self.getNode()
            current_root = current_root.children[index]
            
        #mark last node as leaf
        current_root.isEndOfWord = True
        
        
    def search(self,key):
        current_root = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            
            if current_root.children[index]:
                current_root = current_root.children[index]
            else:
                return False
        return current_root.isEndOfWord
        
def main():
 
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
 
    # Trie object
    t = Trie()
 
    # Construct trie
    for key in keys:
        t.insert(key)
 
    # Search for different keys
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
    
    
main()
        
