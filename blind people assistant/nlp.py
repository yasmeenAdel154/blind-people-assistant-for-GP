import pandas as pd
corpus = [ "This is the first document." , "This is the second document", "And the third one. One is fun" ]

# original Count Vectorizer
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(corpus).toarray()
print ( pd.DataFrame(X ,columns=cv.get_feature_names()) )
# new TFIDF Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
cv_tfidf = TfidfVectorizer()
X_tfidf = cv_tfidf.fit_transform(corpus).toarray()
print ( pd.DataFrame ( X_tfidf ,columns=cv_tfidf.get_feature_names()) )