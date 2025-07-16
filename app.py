import gradio as gr
from transcript_loader import load_transcript
from summarizer import generate_summary
from action_extractor import extract_with_scores, highlight_action_verbs

def process_transcript(file):
    try:
        # Handle both file-like and string-like inputs
        if hasattr(file, "read"):
            raw_text = file.read().decode("utf-8")
        elif isinstance(file, str):
            raw_text = file
        else:
            return "Unsupported file format.", "No action items extracted."

        transcript = load_transcript(raw_text)

        # Validate transcript length
        if not transcript or len(transcript.strip()) < 30:
            return "Transcript too short or empty.", "No action items extracted."

        # Generate summary
        summary = generate_summary(transcript)

        # Extract action items
        action_items = extract_with_scores(transcript)
        if action_items:
            formatted_actions = [
                f"**{highlight_action_verbs(item)}**\nConfidence: `{score}`"
                for item, score in action_items
            ]
        else:
            formatted_actions = ["No action items identified."]

        return summary, "\n\n".join(formatted_actions)

    except Exception as e:
        return f"Error generating summary: {str(e)}", "Action item extraction skipped due to error."

# Gradio interface
demo = gr.Interface(
    fn=process_transcript,
    inputs=gr.File(label="Upload Transcript (.txt)"),
    outputs=[
        gr.Textbox(label="Summary", lines=10),
        gr.Markdown(label="Action Items")
    ],
    title="🧠 InsightAlert",
    description="GenAI-powered meeting summarizer and action item extractor using T5 Transformers."
)

if __name__ == "__main__":
    demo.launch()