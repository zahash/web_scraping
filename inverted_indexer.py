'''
Indexer Exercise:

A corpus contains the following five documents:

"To be or not to be, this is the question!"
"I have a pair of problems for you to solve today."
"It’s a long way to Tipperary, it’s a long way to go. . ."
"I’ve been walking a long way to be here with you today."
"I am not able to question these orders."

Develop an inverted indexer and searcher for any n text documents with m number of words
'''

from collections import defaultdict
import math
import nltk
nltk.download('punkt')

docs = {
"doc1" : "To be or not to be, this is the question!",
"doc2" : "I have a pair of problems for you to solve today.",
"doc3" : "It’s a long way to Tipperary, it’s a long way to go. . .",
"doc4" : "I’ve been walking a long way to be here with you today.",
"doc5" : "I am not able to question these orders.",
}


all_tokens = []
for doc_name in docs:
	all_tokens += nltk.tokenize.word_tokenize(docs[doc_name])

all_tokens = set(all_tokens)

indexer = defaultdict(list)
for token in all_tokens:
	for doc_name, doc_string in docs.items():
		if token in doc_string:
			freq = doc_string.count(token)
			indexer[token].append({"doc_name" : doc_name, "freq" : freq})

term_frequencies = {}
for token, indices_list in indexer.items():
	term_freq = sum(index["freq"] for index in indices_list)/len(indices_list)
	term_frequencies[token] = term_freq

inverse_document_freqencies = {}
for token, term_freq in term_frequencies.items():
	inverse_document_freqencies[token] = round( math.log2(len(docs)/term_freq) , 3)

# print(term_frequencies)
# print(inverse_document_freqencies)

term_weights = {token: term_frequencies[token] * inverse_document_freqencies[token] for token in all_tokens}

print(term_weights)