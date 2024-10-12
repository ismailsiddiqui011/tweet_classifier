import warnings
warnings.filterwarnings('ignore')
import spacy, re
from transformers import T5ForConditionalGeneration, T5Tokenizer

# Load fine-tuned T5 tokenizer and model
model_name = 'luciferMorningstarOmega/fine_tuned_t5'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# Function to make predictions
def predict(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = model.generate(**inputs)
    res = tokenizer.decode(outputs[0], skip_special_tokens=True).split(' | ')
    try:
        emotion, product = res
    except:
        emotion, product = "I can't tell", 'other'
        
    return emotion, product

nlp = spacy.load("en_core_web_sm")
def remove_stopwords(text):
    # Remove @mentions
    text = re.sub(r'@\w+', ' ', text)
    
    # Process the text with spaCy
    doc = nlp(text.lower())
    
    # Filter tokens: remove stopwords, punctuation, and non-alphabetical tokens, and lemmatize
    filtered_tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct and token.is_alpha]
    
    # Join tokens to form a clean string
    text = ' '.join(filtered_tokens)
    
    # Remove single characters and numbers
    text = re.sub(r'\b\w{1}\b|\b\d+\b', '', text)
    
    # Remove extra whitespace
    text = re.sub('\s+', ' ', text).strip()

    # Remove duplicates and ensure final formatting
    text = ' '.join(sorted(set(text.split()))).strip()
    
    return text