# action_extractor.py

import re

def extract_action_items(transcript):
    action_items = []
    lines = transcript.split('\n')
    for line in lines:
        if re.search(r'\b(will|should|need to|must)\b', line, re.IGNORECASE):
            action_items.append(line.strip())
    return action_items
