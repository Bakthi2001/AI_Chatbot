import spacy

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

def preprocess_text(text):
    # Tokenize and lemmatize the text
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]