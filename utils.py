import warnings
warnings.filterwarnings('ignore')
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