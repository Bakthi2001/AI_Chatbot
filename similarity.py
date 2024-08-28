import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from preprocess import preprocess_text

# Load the spaCy model
nlp = spacy.load("en_core_web_md")

def get_closest_faq(user_input, faqs):
    # Preprocess the user input
    processed_input = " ".join(preprocess_text(user_input))
    
    # Convert the user input to a vector
    input_vector = nlp(processed_input).vector.reshape(1, -1)
    
    # Initialize variables to store the best match
    best_match = None
    highest_similarity = -1
    
    # Iterate over each FAQ
    for faq in faqs:
        # Preprocess the FAQ question
        processed_faq = " ".join(preprocess_text(faq["question"]))
        
        # Convert the FAQ question to a vector
        faq_vector = nlp(processed_faq).vector.reshape(1, -1)
        
        # Calculate the cosine similarity
        similarity = cosine_similarity(input_vector, faq_vector)[0][0]
        
        # Update the best match if the current similarity is higher
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = faq["answer"]
    
    return best_match