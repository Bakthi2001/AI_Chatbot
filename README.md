# Codealpha_AI_Chatbot
a chatbot that can answer frequently asked questions (FAQs) about a particular topic or product.
To run the chatbot, follow these steps:

### Step-by-Step Process

#### 1. **Ensure Python is Installed**
Make sure Python is installed on your system. You can check this by running:
```powershell
python --version
```
If Python is not installed, download and install it from [python.org](https://www.python.org/).

#### 2. **Navigate to Your Project Directory**
Open PowerShell and navigate to your project directory:
```powershell
cd "C:\Users\USER\OneDrive

 -

 NSBM\Documents\projects\Chatbot"
```

#### 3. **Remove Existing Virtual Environment (if any)**
If there is an existing virtual environment, remove it:
```powershell
Remove-Item -Recurse -Force "C:\Users\USER\OneDrive - NSBM\Documents\projects\Chatbot\chatbot-env"
```

#### 4. **Create a New Virtual Environment**
Create a new virtual environment:
```powershell
python -m venv chatbot-env
```

#### 5. **Activate the Virtual Environment**
Activate the virtual environment:
```powershell
.\chatbot-env\Scripts\Activate.ps1
```
If you encounter an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
Then try activating the virtual environment again:
```powershell
.\chatbot-env\Scripts\Activate.ps1
```

#### 6. **Install Required Packages**
Install the required packages:
```powershell
pip install spacy scikit-learn
```
Download the language model for `spacy`:
```powershell
python -m spacy download en_core_web_md
```

#### 7. **Ensure Required Files Exist**
Make sure you have the following files in your project directory:

- **similarity.py**:
    ```python
    import spacy
    from sklearn.metrics.pairwise import cosine_similarity

    nlp = spacy.load("en_core_web_md")

    def get_closest_faq(user_input, faqs):
        user_doc = nlp(user_input)
        best_match = None
        best_similarity = 0.0
        for faq in faqs:
            faq_doc = nlp(faq['question'])
            similarity = user_doc.similarity(faq_doc)
            if similarity > best_similarity:
                best_similarity = similarity
                best_match = faq
        return best_match['answer'] if best_match else "Sorry, I don't understand your question."
    ```

- **faq_data.json**:
    ```json
    [
        {"question": "What is your name?", "answer": "I am a chatbot."},
        {"question": "How do you work?", "answer": "I use machine learning to understand your questions."}
    ]
    ```

- **chatbot.py**:
    ```python
    import json
    from similarity import get_closest_faq

    class Chatbot:
        def __init__(self):
            self.faqs = self.load_faqs()

        def load_faqs(self):
            with open('faq_data.json', 'r') as f:
                return json.load(f)

        def get_response(self, user_input):
            return get_closest_faq(user_input, self.faqs)

    if __name__ == "__main__":
        chatbot = Chatbot()
        while True:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                break
            response = chatbot.get_response(user_input)
            print(f"Bot: {response}")
    ```

#### 8. **Run Your Script**
Run your chatbot script:
```powershell
python chatbot.py
```

### Interaction Example

When you run the script, you should be able to interact with the chatbot in the terminal:

```plaintext
You: What is your name?
Bot: I am a chatbot.
You: How do you work?
Bot: I use machine learning to understand your questions.
You: exit
```

This setup should ensure that your chatbot is working correctly. If you encounter any specific issues or errors, please provide the error messages so I can assist you further.
