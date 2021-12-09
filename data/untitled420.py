from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd 
from corpy.morphodita import Tokenizer
from deduplicate import deduplicate
from vectorized_lemmatized_articles import vectorized_lemmatized_articles
from sklearn.decomposition import NMF, LatentDirichletAllocation
from time import time
import matplotlib.pyplot as plt

# def csv2dict():
#     file = open("article_archive_all_9_12_10am.csv", encoding="utf8")
#     csvreader = csv.reader(file)
#     header = next(csvreader)
#     zpravy_csv = []
#     for row in csvreader:
#         zpravy_csv.append(row)
#     file.close()

#     pom = zpravy_csv[0]   

#     zpravy = [
#         {'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]}
#             ]   

#     for i in range(1,np.size(zpravy_csv,0)):
#         pom = zpravy_csv[i]
#         zpravy.append({'id': pom[0], header[1]:  pom[1], header[2]: pom[2], header[3]: pom[3], header[4]: pom[4], header[5]: pom[5], header[6]: pom[6], header[7]: pom[7], header[8]: pom[8]})
    
#     return zpravy

def plot_top_words(model, feature_names, n_top_words, title):
    fig, axes = plt.subplots(2, 5, figsize=(30, 15), sharex=True)
    axes = axes.flatten()
    for topic_idx, topic in enumerate(model.components_):
        top_features_ind = topic.argsort()[: -n_top_words - 1 : -1]
        top_features = [feature_names[i] for i in top_features_ind]
        weights = topic[top_features_ind]

        ax = axes[topic_idx]
        ax.barh(top_features, weights, height=0.7)
        ax.set_title(f"Topic {topic_idx +1}", fontdict={"fontsize": 30})
        ax.invert_yaxis()
        ax.tick_params(axis="both", which="major", labelsize=20)
        for i in "top right left".split():
            ax.spines[i].set_visible(False)
        fig.suptitle(title, fontsize=40)

    plt.subplots_adjust(top=0.90, bottom=0.05, wspace=0.90, hspace=0.3)
    plt.show()


# zpravy = csv2dict()
# articles = pd.DataFrame(zpravy)

df=pd.read_csv ('article_archive_all_9_12_10am.csv')
articles=df[['title','summary']]

# vla=vectorized_lemmatized_articles(articles,0,articles.shape[0])
# a=vla.run()
# ded=deduplicate(a)
# b=ded.run()
# articles= articles.drop(articles.index[b])
vla1=vectorized_lemmatized_articles(articles,0,articles.shape[0])
vektory = vla1.run()

vectorizer = TfidfVectorizer(max_features=900)
X = vectorizer.fit_transform(vektory)
y = vectorizer.get_feature_names()
nmf = NMF(n_components=10, random_state=42, alpha=0.1, l1_ratio=0.5).fit(X)

tfidf_feature_names = vectorizer.get_feature_names()
plot_top_words(
    nmf, tfidf_feature_names, 20, "Topics in NMF model (Frobenius norm)"
)