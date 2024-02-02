from joblib import load

tfidf = load('model_dev/tfidf.joblib')
classifier = load('model_dev/model.joblib')

def sentclf(review):
    review_mat = tfidf.transform([review])
    labels = classifier.predict(review_mat)

    return labels[0]