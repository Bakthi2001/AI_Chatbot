# Codealpha_AI_Chatbot
a chatbot that can answer frequently asked questions (FAQs) about a particular topic or product.
To run the chatbot, follow these steps:

Step 1: Ensure All Dependencies Are Installed

Make sure you have all the necessary dependencies installed in your virtual environment. You need `spacy`, `scikit-learn`, and the spaCy model `en_core_web_md`.

1. **Activate your virtual environment**:
   ```sh
   .\chatbot-env\Scripts\activate
   ```

2. **Install dependencies**:
   ```sh
   pip install spacy scikit-learn
   ```

3. **Download the spaCy model**:
   ```sh
   python -m spacy download en_core_web_md
   ```

### Step 2: Run the Chatbot

1. **Activate your virtual environment** (if not already activated):
   ```sh
   .\chatbot-env\Scripts\activate
   ```

2. **Run the chatbot**:
   ```sh
   python main.py
   ```

This will start the chatbot, and you can interact with it through the terminal. To exit the chatbot, type `exit` or `quit`.
