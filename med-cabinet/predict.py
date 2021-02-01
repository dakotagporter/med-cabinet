import pickle

vectorizer = pickle.load('vectorizer.pkl', 'rb')
model = pickle.load('model.pkl', 'rb')


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
