from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle 

class deduplicate:
    def __init__(self,vektory):
        self.vektory = vektory
        self.indexy_duplikatu= None
        
    def run(self):
        with open('fin_model.pickle', 'rb') as f:
            fin_model = pickle.load(f)
        

        vectorizer = TfidfVectorizer(ngram_range=(1,2))
        vectorizer.fit(self.vektory)

        x = vectorizer.transform(self.vektory)
        
        inds=[]
        for i in range(x.shape[0]):
            for j in range(x.shape[0]):
                if j >= i:
                    break
                else:
                    container=cosine_similarity(x[i],x[j])
                    pred=fin_model.predict(container)
                    if pred==1:
                        inds.append([i,j])       
        for i in range(len(inds)):
            inds[i].sort()
        inds.sort()
        
        res = []
        for i in range(len(inds)):
            if inds[i][1] not in res:
                res.append(inds[i][1])
        self.indexy_duplikatu=res
        return self.indexy_duplikatu