"""
Design a data structure that supports adding new words and
finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be
matched later.
bool search(word) Returns true if there is any string in the
data structure that matches word or false otherwise. word may
contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary dictionary = new WordDictionary();
dictionary.addWord("bad");
dictionary.addWord("dad");
dictionary.addWord("mad");
dictionary.search("pad"); // return False
dictionary.search("bad"); // return True
dictionary.search(".ad"); // return True
dictionary.search("b.."); // return True
"""