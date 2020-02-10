from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import pandas as pd

df = pd.read_csv("pages.tsv", sep='\t', header=None)
documents = df.iloc[:, 1].values

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

num_clusters = 10
model = KMeans(n_clusters=num_clusters, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(num_clusters):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

print("\n")
print("Prediction")

Y = vectorizer.transform(["films are great"])
prediction = model.predict(Y)
print(prediction)

Y = vectorizer.transform(["i dont feel so good"])
prediction = model.predict(Y)
print(prediction)