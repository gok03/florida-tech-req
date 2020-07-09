# Extract technical terms from a document
# Uses dictionary as a stop word filter
import string
exclude = set(string.punctuation) # - set("/'")

ed = {}
techterms = {} 

def cleanword(word):
        word = "".join(ch for ch in word if ch not in exclude)
        if word.startswith('/') or word.startswith("'"):
                word = word[1:]
        return word.lower()

edpath = r"seg_words.txt"
words = open(edpath).read().split()
for  word in words:
       ed[cleanword(word)] = 1

if __name__ == "__main__":
    import sys
    import re
    textwords = open(sys.argv[1]).read().split()

    for word in textwords:
        if re.search("\d",word):
                pass
        else:
            word = cleanword(word)
            if word in ed:
                techterms[word] = 1
                #print word

for term in sorted(techterms):
        print term

print len(techterms)