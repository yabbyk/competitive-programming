class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        
        sorted_words = [""]* len(words)
        for i in words:
            pos = int(i[-1])
            sorted_words[pos-1]= i[:-1]
        return " ".join(sorted_words)

    s = "is2 sentence4 This1 a3"
    original_sentence = sorted(s)
    print(original_sentence)
            
