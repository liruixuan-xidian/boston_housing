import time
from sklearn.cross_validation import KFold

t0 = time()
kf = KFold(len(authors),2,shuffle=True)        #len(authors)   total number of dataset  k = 2
for train_indices,test_indices in kf:
    #make training and testin datasets
    features_train = [word_data[ii] for ii in train_indices]
    feaures_test = [word_data[ii] for ii in test_indices]
    authors_train = [authors[ii] for ii in train_indices]
    authors_test = [authors[ii] for ii in test_indices]

    #TFIDF and feature selection
    vectorizer = TfidfVectorizer(sublinear_tf = True,max_df = 0.5,stop_words = 'english')

    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)
    selector = SelectPercentile(f_classif,percentile = 10)
    selector.fit(features_train_transformd,authors_train)
    features_train_transformed = selector.transform(features_train_transformed).toarray()
    features_test_transformed = selector.transform(features_test_transformed).toarray()

    clf = GaussianNB()
    clf.fit(featres_train_transformed,authors_train)
    print "training time:", round(time()-t0,3),"s"
    t0 = time()


