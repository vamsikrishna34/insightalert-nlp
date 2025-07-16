import gradio as gr
from transcript_loader import load_transcript
from summarizer import generate_summary
from action_extractor import extract_with_scores, highlight_action_verbs

def process_transcript(file):
    transcript = load_transcript(file.read())
    summary = generate_summary(transcript)
    action_items = extract_with_scores(transcript)

    if action_items:
        formatted_actions = [
            f"**{highlight_action_verbs(item)}**\nConfidence: `{score}`"
            for item, score in action_items
        ]
    else:
        formatted_actions = ["No action items identified."]

    return summary, "\n\n".join(formatted_actions)

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