from transcript_loader import load_transcript
from summarizer import generate_summary
from action_extractor import (
    extract_with_scores,
    highlight_action_verbs
)

def main():
    file_path = "sample_transcripts/sample_transcript.txt"
    transcript = load_transcript(file_path)

    print("\n Meeting Summary:\n")
    summary = generate_summary(transcript)
    print(summary)

    print("\n Action Items (with confidence scores):\n")
    action_items = extract_with_scores(transcript)

    if action_items:
        for item, score in action_items:
            highlighted = highlight_action_verbs(item)
            print(f"- {highlighted}  [Confidence: {score}]")
    else:
        print("No action items identified.")

if __name__ == "__main__":
    main()