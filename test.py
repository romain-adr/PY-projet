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

id2doc = 'The development of parsimonious models for and reliable inference and predictionof responses in high-dimensional regression settings is often challenging dueto relatively small sample sizes and the presence of complex interactionpatterns between a large number of covariates',
word = "and"
passages = []
texte = str(list(id2doc))
sentences = re.split('[ \t,;.!?]', texte)
for sentence in sentences:
        sentence = sentence.lower()
        passages.append(sentence.strip())
print(passages)
vocab_counter = pd.DataFrame.from_dict(dict(Counter(passages)), orient='index', columns=['frequency'])
print(vocab_counter)