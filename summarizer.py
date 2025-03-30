# summarizer.py

from transformers import pipeline

# Load summarization pipeline from Hugging Face
summarize = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def generate_summary(text, max_length=120, min_length=30):
    if len(text.split()) < 30:
        return "Transcript too short to summarize."
    return summarize(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
