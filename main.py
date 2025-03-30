# main.py

from transcript_loader import load_transcript
from summarizer import generate_summary
from action_extractor import extract_action_items

def main():
    file_path = "sample_transcript.txt"
    transcript = load_transcript(file_path)

    print("\nMeeting Summary:\n")
    summary = generate_summary(transcript)
    print(summary)

    print("\nAction Items:\n")
    actions = extract_action_items(transcript)
    if actions:
        for item in actions:
            print("- " + item)
    else:
        print("No action items identified.")

if __name__ == "__main__":
    main()
