import re 
'''
def find(word): #retourne les phrases contenant le mot-clef entre en paramettre
    passages = [] 
    text = list(text0.values)
    word_re = re.compile(word, re.IGNORECASE)
    sentences = re.split(r'[.!?]', text)
    for sentence in sentences:
        if re.search(word_re, sentence):
            passages.append(sentence.strip())
    print(passages)

text0 = {42: test . word is your. iiuh}
lst = list(text0.values)
print(lst)

for i in new_list:
    if re.search("^\d+$", i):
        new_list.remove(i)
print(new_list)

print(list(corpus.id2doc.values()))
passages = [] 
text = list(corpus.id2doc.values())
print(type(text))
conv = str(text)
word_re = re.compile('over', re.IGNORECASE)
sentences = re.split(r'[.!?]', conv)
for sentence in sentences:
    if re.search(word_re, sentence):
        passages.append(sentence.strip())
print(passages)
'''

from collections import Counter
import pandas as pd
import re
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
id2doc = ['The development of parsimonious models for and reliable inference 1 and predictionof responses 22 in high depends dimensional. regression 1 settings is often challenging dueto relatively small 8 sample sizes and the presence of complex complex interactionpatterns between a large number of covariates']
toks = word_tokenize(id2doc)
print(toks[:100])
passages = []
new_list = []
texte = str(list((id2doc)))
#print(texte)
sentences = re.split('[ \t,;.!?]', texte)
for sentence in sentences:
        sentence = sentence.lower()
        passages.append(sentence.strip())
#print(passages)
for i in passages:
        if not re.search("^\d+$", i):
                new_list.append(i)
new_list.sort()
#print(new_list)
my_list = {}
counter = Counter(new_list).items()
for word, count in counter:
    my_list[word] = {'id': id(word), 'freq': count }
print(my_list)
 

