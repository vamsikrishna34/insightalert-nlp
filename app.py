import gradio as gr
from summarizer import generate_summary
from action_extractor import extract_with_scores, highlight_action_verbs

def process_transcript(file, text_input):
    status.update(value="⏳ Processing...")

    try:
        # Use uploaded file if available
        if file and hasattr(file, "read"):
            raw_text = file.read().decode("utf-8")
        elif text_input and isinstance(text_input, str):
            raw_text = text_input
        else:
            status.update(value="")
            return "No valid input provided.", "No action items extracted."

        transcript = raw_text.strip()

        # Validate transcript length
        if not transcript or len(transcript.split()) < 30:
            status.update(value="")
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

        status.update(value="")
        return summary, "\n\n".join(formatted_actions)

    except Exception as e:
        status.update(value="")
        return f"Error generating summary: {str(e)}", "Action item extraction skipped due to error."

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("## 🧠 InsightAlert")
    gr.Markdown("GenAI-powered meeting summarizer and action item extractor using T5 or DistilBART.")

    with gr.Row():
        file_input = gr.File(label="Upload Transcript (.txt)")
        text_input = gr.Textbox(label="Or Paste Transcript Text", lines=10, placeholder="Paste meeting notes here...")

    status = gr.Textbox(label="Status", interactive=False)

    summary_output = gr.Textbox(label="Summary", lines=10)
    actions_output = gr.Markdown(label="Action Items")

    run_button = gr.Button("Run")
    run_button.click(process_transcript, inputs=[file_input, text_input], outputs=[summary_output, actions_output])

demo.launch()