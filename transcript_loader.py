# transcript_loader.py

def load_transcript(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
