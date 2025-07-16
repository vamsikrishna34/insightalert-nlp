import re
from typing import Union

def load_transcript(file_input: Union[str, bytes]) -> str:
    """
    Loads and cleans a transcript from a file path or uploaded file.

    Args:
        file_input (Union[str, bytes]): File path (CLI) or file bytes (Streamlit).

    Returns:
        str: Cleaned transcript text.
    """
    try:
        if isinstance(file_input, str):
            with open(file_input, 'r', encoding='utf-8') as file:
                raw_text = file.read()
        else:
            raw_text = file_input.decode("utf-8")

        return clean_transcript(raw_text)

    except Exception as e:
        return f"Error loading transcript: {str(e)}"

def clean_transcript(text: str) -> str:
    """
    Cleans transcript by removing timestamps, speaker tags, and extra whitespace.

    Args:
        text (str): Raw transcript text.

    Returns:
        str: Cleaned transcript.
    """
    # Remove timestamps like [00:01], (00:01), etc.
    text = re.sub(r'\[?\(?\d{1,2}:\d{2}\)?\]?', '', text)

    # Remove speaker tags like "John:" or "Speaker 1:"
    text = re.sub(r'^\s*\w+:\s*', '', text, flags=re.MULTILINE)

    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)

    return text.strip()