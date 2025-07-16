import re
from typing import List, Dict, Tuple

# Expanded intent keywords to catch more task-like phrases
INTENT_KEYWORDS = r'\b(will|should|need to|must|have to|required to|plan to|shall|submit|send|schedule|review|complete|finish|prepare|share|follow up)\b'

# Action verbs used for highlighting and scoring
ACTION_VERBS = [
    'will', 'should', 'need to', 'must', 'have to', 'plan to', 'shall',
    'submit', 'send', 'schedule', 'review', 'complete', 'finish', 'prepare', 'share', 'follow up'
]

def extract_action_items(transcript: str) -> List[str]:
    """Extracts action items from a transcript based on intent keywords."""
    action_items = []
    for line in transcript.splitlines():
        if re.search(INTENT_KEYWORDS, line, re.IGNORECASE):
            cleaned_line = line.strip()
            if cleaned_line:
                action_items.append(cleaned_line)
    return action_items

def extract_action_items_by_speaker(transcript: str) -> Dict[str, List[str]]:
    """Extracts action items and groups them by speaker (if speaker tags are present)."""
    speaker_actions = {}
    for line in transcript.splitlines():
        match = re.match(r'^(\w+):\s*(.*)', line)
        if match:
            speaker, content = match.groups()
            if re.search(INTENT_KEYWORDS, content, re.IGNORECASE):
                speaker_actions.setdefault(speaker, []).append(content.strip())
    return speaker_actions

def highlight_action_verbs(line: str) -> str:
    """Highlights action verbs in a line using Markdown-style bolding."""
    for verb in ACTION_VERBS:
        line = re.sub(rf'\b({verb})\b', r'**\1**', line, flags=re.IGNORECASE)
    return line

def score_action_item(line: str) -> float:
    """Assigns a confidence score to an action item based on keyword density."""
    score = sum(1 for verb in ACTION_VERBS if re.search(rf'\b{verb}\b', line, re.IGNORECASE))
    return round(min(score / 3, 1.0), 2)  # More generous scoring

def extract_with_scores(transcript: str) -> List[Tuple[str, float]]:
    """Extracts action items with confidence scores."""
    items = extract_action_items(transcript)
    scored = [(item, score_action_item(item)) for item in items]
    # Filter out very low-confidence items (optional)
    return [(item, score) for item, score in scored if score >= 0.1]