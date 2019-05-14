'''
Created on 2019. 4. 29.

@author: Playdata
'''
import gensim

#저장한 모델을 불러옵니다
md = gensim.models.Doc2Vec.load("test.model")
print(md.wv.similar_by_word("문재인"))
print(md.wv.most_similar("트럼프"))
print(md.docvecs)