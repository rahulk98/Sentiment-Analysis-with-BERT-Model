import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
# Function to predict sentiment

def predict_sentiment(text):
    label_mapping = {0: "neutral", 1: "positive", 2: "negative"}
    model_name = "rahulk98/bert-finetuned-youtube_sentiment_analysis"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = torch.argmax(logits).item()
    return label_mapping[predicted_class_id]

# Taking input from user
if __name__ == "__main__":
    text = input("Enter a sentence to predict sentiment: ")
    sentiment = predict_sentiment(text)
    print(f"Predicted sentiment: {sentiment}")
