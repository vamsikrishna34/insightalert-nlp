from transformers import pipeline
from typing import List

def load_summarizer(model_name: str = "t5-small") -> pipeline:
    """
    Loads a Hugging Face summarization pipeline.

    Args:
        model_name (str): Model name (default: t5-small).

    Returns:
        pipeline: Summarization pipeline.
    """
    return pipeline("summarization", model=model_name, tokenizer=model_name)

# Initialize once for reuse
summarizer = load_summarizer()

def chunk_text(text: str, max_words: int = 400) -> List[str]:
    """
    Splits long text into manageable chunks for summarization.

    Args:
        text (str): Input transcript.
        max_words (int): Max words per chunk.

    Returns:
        List[str]: List of text chunks.
    """
    words = text.split()
    return [' '.join(words[i:i + max_words]) for i in range(0, len(words), max_words)]

def generate_summary(text: str, max_length: int = 120, min_length: int = 30) -> str:
    """
    Generates a summary from input text using a T5 model.

    Args:
        text (str): Input transcript.
        max_length (int): Maximum length of summary.
        min_length (int): Minimum length of summary.

    Returns:
        str: Summary text.
    """
    if len(text.split()) < min_length:
        return "Transcript too short to summarize."

    try:
        chunks = chunk_text(text)
        summaries = []
        for chunk in chunks:
            result = summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)
            summaries.append(result[0]['summary_text'])
        return ' '.join(summaries)
    except Exception as e:
        return f"Error during summarization: {str(e)}"