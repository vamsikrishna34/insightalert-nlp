# InsightAlert – Meeting Summary and Action Item Extractor

InsightAlert is a lightweight NLP tool that processes meeting transcripts and automatically generates a summary along with a list of key action items. It simulates how product teams or remote teams can quickly extract value from their discussions without manually reviewing notes.

## Overview

This project reads a plain text transcript, uses a transformer-based summarization model to generate a concise overview, and applies simple rule-based logic to extract actionable statements. It was built to explore real-world applications of natural language processing that are both explainable and practical.

## Features

- Generates a summary of a meeting transcript using a pretrained transformer model
- Identifies and extracts sentences that include action items (e.g., "will", "need to", "should")
- Designed with modular Python files for clarity and scalability

## Technologies

- Python
- Hugging Face Transformers (T5)
- Regular Expressions (re)
- CLI-based interface

## How to Run

1. Install dependencies:

```bash
pip install transformers
```

2. Run the project:

```bash
python main.py
```

## Project Structure

- `transcript_loader.py`: Loads the transcript from a text file
- `summarizer.py`: Applies transformer model to summarize meeting text
- `action_extractor.py`: Extracts actionable follow-up items
- `main.py`: Runs the full pipeline
- `sample_transcript.txt`: Sample meeting input

## Why I Built This

I wanted to explore how modern NLP models can be applied to everyday productivity tasks like meeting documentation. This project gave me experience working with transformer pipelines, designing a simple rule-based NLU component, and structuring Python code for real-world workflows.

## Future Ideas

- Use named entity recognition (NER) to identify responsible team members
- Add support for multi-speaker attribution
- Convert to a Streamlit or Flask web app

