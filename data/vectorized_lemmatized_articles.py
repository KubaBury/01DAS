import numpy as np
import pandas as pd 



class vectorized_lemmatized_articles:
    def __init__(self,clanky, startind, endind):
        self.startind = startind
        self.endind = endind
        self.clanky = clanky
        self.vektory= None
    
    def run(self):
        
        from corpy.morphodita import Tokenizer
        tokenizer = Tokenizer("czech")
        punc='[]{}()"„“!@#$%^=_&*-:/,.\`~;^*,<>|°'
        def tokeny(clanek):
            cont=[]
            for word in tokenizer.tokenize(clanek):
                cont.append(word)
            nopunc = [char for char in cont if char not in punc]
            return nopunc

        from corpy.morphodita import Tagger
        tagger = Tagger("./czech-morfflex-pdt-161115.tagger")
        def lemmatizer(slovo):
            tokens = list(tagger.tag(slovo))
            a=''.join(str(tokens))
            ind1=a.find('a=')
            ind2=a.find("'",ind1+3)
            return a[ind1+3:ind2]

        filename = 'stopwords-cs.txt'
        stopwords = np.loadtxt(filename, dtype=str,encoding="utf8")
        def delete_stopwords(lematizovana_slova):
            return list(set(lematizovana_slova)-set(stopwords))


        #df=pd.ExcelFile('C:/Users/vacla/OneDrive/Dokumenty/Audiozprávy/article_archive_cleared.xls')
        #articles=df.parse('article_archive')
    
        #articles=articles[['title','summary']]
    
        ddd=self.clanky.iloc[self.startind:self.endind]
        # for type in ddd.columns:
        #     ddd[type]=ddd[type].astype(str)
        
                
        data=[]
        for i in range(ddd.shape[0]):
            g=' '.join(ddd.iloc[i])
            data.append(g)
        
        databaze=[]
        d=[]
        for clanek in data:
            d=tokeny(clanek)
            d=delete_stopwords(d)
            e=[]
            for slovo in d:
                k=lemmatizer(slovo)
                if k.find('-')!=-1:
                    e.append(k[0:k.find('-')])
                elif k.find('_')!=-1:
                    e.append(k[0:k.find('_')])
                else:
                    e.append(k)
            e=delete_stopwords(e)
            databaze.append(e)
            
        dataset=[]   ###dataset je ve tvaru co potřebuje CountVectorizer
        for index in range(len(databaze)):
            store=' '.join(databaze[index])
            dataset.append(store)
        
        self.vektory=dataset
        return self.vektory