import re
from typing import List, Dict, Tuple

INTENT_KEYWORDS = r'\b(will|should|need to|must|have to|required to|plan to|shall)\b'
ACTION_VERBS = ['will', 'should', 'need to', 'must', 'have to', 'plan to', 'shall']

def extract_action_items(transcript: str) -> List[str]:
    """
    Extracts action items from a transcript based on intent keywords.

    Args:
        transcript (str): Raw meeting transcript.

    Returns:
        List[str]: Action item lines.
    """
    action_items = []
    for line in transcript.splitlines():
        if re.search(INTENT_KEYWORDS, line, re.IGNORECASE):
            cleaned_line = line.strip()
            if cleaned_line:
                action_items.append(cleaned_line)
    return action_items

def extract_action_items_by_speaker(transcript: str) -> Dict[str, List[str]]:
    """
    Extracts action items and groups them by speaker (if speaker tags are present).

    Returns:
        Dict[str, List[str]]: Speaker-wise action items.
    """
    speaker_actions = {}
    for line in transcript.splitlines():
        match = re.match(r'^(\w+):\s*(.*)', line)
        if match:
            speaker, content = match.groups()
            if re.search(INTENT_KEYWORDS, content, re.IGNORECASE):
                speaker_actions.setdefault(speaker, []).append(content.strip())
    return speaker_actions

def highlight_action_verbs(line: str) -> str:
    """
    Highlights action verbs in a line using Markdown-style bolding.

    Args:
        line (str): Input sentence.

    Returns:
        str: Sentence with highlighted verbs.
    """
    for verb in ACTION_VERBS:
        line = re.sub(rf'\b({verb})\b', r'**\1**', line, flags=re.IGNORECASE)
    return line

def score_action_item(line: str) -> float:
    """
    Assigns a confidence score to an action item based on keyword density.

    Args:
        line (str): Input sentence.

    Returns:
        float: Score between 0.0 and 1.0.
    """
    score = sum(1 for verb in ACTION_VERBS if re.search(rf'\b{verb}\b', line, re.IGNORECASE))
    return round(min(score / len(ACTION_VERBS), 1.0), 2)

def extract_with_scores(transcript: str) -> List[Tuple[str, float]]:
    """
    Extracts action items with confidence scores.

    Returns:
        List[Tuple[str, float]]: List of (action item, score).
    """
    items = extract_action_items(transcript)
    return [(item, score_action_item(item)) for item in items]