import gradio as gr
from summarizer import generate_summary
from action_extractor import extract_with_scores, highlight_action_verbs

def process_transcript(file, text_input):
    try:
        transcript = ""
        status_message = "⏳ Processing..."

        # Try reading from file
        if file and hasattr(file, "read"):
            try:
                transcript = file.read().decode("utf-8").strip()
            except Exception as decode_err:
                return f"Error decoding file: {decode_err}", "", ""

        # Fallback to textbox input
        if not transcript and text_input:
            transcript = text_input.strip()

        # Validate transcript
        if not transcript or len(transcript.split()) < 30:
            return "Transcript too short or empty.", "", "No action items extracted."

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

        return "", summary, "\n\n".join(formatted_actions)

    except Exception as e:
        return f"Error: {str(e)}", "", "Action item extraction skipped due to error."

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 InsightAlert")
    gr.Markdown("GenAI-powered meeting summarizer and action item extractor using DistilBART.")

    with gr.Row():
        file_input = gr.File(label="Upload Transcript (.txt)")
        text_input = gr.Textbox(label="Or Paste Transcript Text", lines=10, placeholder="Paste meeting notes here...")

    status = gr.Textbox(label="Status", interactive=False)
    summary_output = gr.Textbox(label="Summary", lines=10)
    actions_output = gr.Markdown(label="Action Items")

    run_button = gr.Button("Run")
    run_button.click(
        fn=process_transcript,
        inputs=[file_input, text_input],
        outputs=[status, summary_output, actions_output]
    )

demo.launch()