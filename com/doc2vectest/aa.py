'''
Created on 2019. 4. 29.

@author: Playdata
'''
import gensim


md = gensim.models.Doc2Vec.load("jcjc.model")
print(md.wv.similar_by_word("미국"))
print(md.wv.most_similar("북한"))
print(md.docvecs)