import dill
import pickle
# import spacy
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.neighbors import NearestNeighbors


def processor(doc):
    doc = nlp(doc)

    return " ".join([token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct])


 
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def vectorize(text):
    """Turn input text into a vector representation.

    Args:
        text (list): List of document(s) to vectorize
    Returns:
        vect (scipy.sparse.csr.csr_matrix): Vector representation of input text
    """
    vect = vectorizer.transform(text)

    return vect


def predict(text):
    """Use pre-defined tools to process and predict input data.

    Args:
        text (str): Input data to be processed and predicted
    Returns:
        indices (list): List most to least similar documents to input data
    """
    vect = vectorize([text])
    _, indices = model.kneighbors(vect)

    return indices[0].tolist()
