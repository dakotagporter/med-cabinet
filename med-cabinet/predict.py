import pickle
import spacy

nlp = spacy.load("en_core_web_md")


vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


def preprocessor(doc):
    """Preprocess input text data using spaCy functionality.

    Args:
        doc (list): List of input data to be processed
    Returns:
        new_text (str): New processed document
    """
    doc = nlp(doc)
    new_text = " ".join([token.lemma_.lower() for token in doc if not
                         token.is_stop and not token.is_punct])

    return new_text


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
    text = preprocessor(text)
    vect = vectorize([text])
    _, indices = model.kneighbors(vect)

    return indices[0].tolist()
