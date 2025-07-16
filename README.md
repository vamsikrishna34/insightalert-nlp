🧠 InsightAlert
GenAI-powered meeting summarizer and action item extractor
Built with Hugging Face Transformers, Gradio, and Python

🚀 Overview
InsightAlert transforms raw meeting transcripts into concise summaries and actionable tasks. Designed for enterprise productivity, it uses state-of-the-art NLP models to extract key insights and highlight responsibilities — making follow-ups faster and meetings more meaningful.

✨ Features
- 🧠 Summarization using DistilBART or Pegasus
- 📌 Action item extraction with confidence scoring
- 📄 Dual input: upload .txt files or paste text directly
- ⚙️ Modular architecture for easy extension
- 🖥️ Gradio UI for fast prototyping and deployment

🛠️ Tech Stack
| Component | Description | 
| transformers | Summarization via Hugging Face models | 
| Gradio | Interactive UI for file/text input | 
| Python | Core logic and orchestration | 
| Hugging Face Spaces | Deployment and hosting | 



📦 Installation
git clone https://github.com/your-username/InsightAlert
cd InsightAlert
pip install -r requirements.txt
python app.py



🧪 Usage
- Upload a .txt transcript or paste meeting notes
- Click Run
- View the generated summary and extracted action items
- Use the results for follow-ups, reports, or automation

📄 Sample Transcript
Moderator: Thanks for joining. Let’s start with project updates.

Priya: I’ll finalize the API documentation by Wednesday and send it to the dev team.

Carlos: I need to schedule a client demo for Friday and prepare the slide deck tomorrow.

Moderator: Everyone should review the Q3 roadmap before Monday.



📈 Roadmap
- [ ] Add speaker grouping for action items
- [ ] Export results to Markdown or PDF
- [ ] Integrate with LangChain for agentic workflows
- [ ] Add support for timestamped transcripts

🤝 Contributing
Pull requests and feedback are welcome! If you’d like to collaborate or suggest improvements, feel free to open an issue or reach out.

📬 Contact
Created by Vamsi
Feel free to connect or message me for collaboration opportunities.
