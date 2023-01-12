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



id2doc = 'The development of parsimonious models for and reliable inference and predictionof responses in high-dimensional regression settings is often challenging dueto relatively small sample sizes and the presence of complex interactionpatterns between a large number of covariates',
word = "and"
passages = []
texte = str(list(id2doc))
word_re = re.compile(word, re.IGNORECASE)
sentences = re.split(r'[.!?]', texte)
for sentence in sentences:
    if re.search(word_re, sentence):
        passages.append(sentence.strip())
print(passages)
for sentence in passages:
    start = sentence.find(word)
    end = sentence.find(word) + len(word)
    context1 = sentence[start-20:start]
    context2 = sentence[end:end+20]
    print(context1)
    print(context2)
