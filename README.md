# 🤖 AI Web App Builder

An intelligent code generation system powered by LangGraph and AI agents that transforms natural language descriptions into complete, working applications.

[![Demo Video](https://img.shields.io/badge/YouTube-Demo-red?style=for-the-badge&logo=youtube)](https://youtu.be/c6O0EEuOjNE)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/shaheerkhan00/AI-Web-App-Builder)

## 🎥 Video Demo

Watch the full walkthrough and demonstration:
[AI App Builder Demo on YouTube](https://youtu.be/c6O0EEuOjNE)

## 🌟 Features

- **Natural Language to Code**: Describe your app idea in plain English and watch it come to life
- **Multi-Agent Architecture**: Three specialized AI agents work together:
  - **Planner Agent**: Converts your idea into a structured project plan
  - **Architect Agent**: Breaks down the plan into detailed implementation steps
  - **Coder Agent**: Writes the actual code with proper file structure
- **Dual Interface**: 
  - Command-line interface for quick iterations
  - Beautiful Streamlit web UI for enhanced user experience
- **Automatic Project Generation**: Creates complete project folders with all necessary files
- **Tech Stack Flexibility**: Supports various technologies (HTML/CSS/JS, Python, React, etc.)

## 📋 Prerequisites

- Python 3.11 or higher
- UV package manager (recommended) or pip
- Groq API key (for LLM access)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shaheerkhan00/AI-Web-App-Builder.git
   cd AI-Web-App-Builder
   ```

2. **Install dependencies**
   
   Using uv (recommended):
   ```bash
   uv sync
   ```

   Or using pip:
   ```bash
   pip install -e .
   ```

   Or install packages individually:
   ```bash
   pip install groq langchain langchain-core langchain-groq langgraph pydantic python-dotenv streamlit
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## 💻 Usage

### Method 1: Command Line Interface

Run the CLI version for quick project generation:

```bash
python main.py
```

**Options:**
- `-r` or `--recursion-limit`: Set the recursion limit (default: 100)

**Example:**
```bash
python main.py --recursion-limit 150
```

Then enter your project prompt when asked:
```
Enter your project prompt: create a simple web app for calculator
```

### Method 2: Streamlit Web UI

Launch the beautiful web interface:

```bash
streamlit run streamlit_app.py
```

The web UI provides:
- Visual progress tracking
- Example prompts
- Configurable recursion limits
- Direct links to generated applications
- Detailed error reporting

## 📂 Project Structure

```
AI-Web-App-Builder/
├── agent/
│   ├── graph.py          # LangGraph workflow definition
│   ├── prompts.py        # AI agent prompts
│   ├── states.py         # Pydantic models for state management
│   └── tools.py          # File system tools
├── generated_project/    # Output folder for generated apps
├── main.py              # CLI entry point
├── streamlit_app.py     # Web UI entry point
├── pyproject.toml       # Project dependencies
├── .env                 # Environment variables (create this)
└── README.md           # This file
```

## 🎯 Example Prompts

Try these example prompts to get started:

- **Web Calculator**: `create a simple web app for calculator`
- **Todo List**: `build a todo list application with add, delete, and complete functionality`
- **Portfolio Site**: `create a simple portfolio website with sections for about, projects, and contact`
- **Weather Dashboard**: `make a weather dashboard that displays current weather`
- **Expense Tracker**: `build an expense tracker with categories and charts`

## 🔧 How It Works

1. **Planning Phase**: The Planner agent analyzes your prompt and creates a comprehensive project plan including:
   - App name and description
   - Technology stack
   - Required features
   - File structure

2. **Architecture Phase**: The Architect agent breaks down the plan into detailed implementation tasks:
   - Specific code to write in each file
   - Variable and function names
   - Integration points between modules

3. **Coding Phase**: The Coder agent implements each task:
   - Reads existing files for context
   - Writes complete, working code
   - Maintains consistency across files
   - Integrates all components

## 🛠️ Configuration

### Recursion Limit

Adjust the recursion limit based on project complexity:
- **Simple apps** (calculator, todo list): 50-100
- **Medium apps** (multi-page sites, dashboards): 100-200
- **Complex apps** (full-stack applications): 200-500

### LLM Model

By default, the system uses `openai/gpt-oss-120b` via Groq. To change the model, edit `agent/graph.py`:

```python
llm = ChatGroq(model="your-model-name")
```

## 📊 Output

Generated projects are saved in the `generated_project/` folder with a complete file structure:

```
generated_project/
├── index.html
├── styles.css
├── script.js
└── ... (additional files based on your project)
```

Open `index.html` in your browser to view the generated application!

## 🐛 Troubleshooting

### Tool Validation Error

If you see `attempted to call tool 'repo_browser.list_files'`:
- Ensure your `agent/prompts.py` explicitly lists the exact tool names
- The model should only use: `read_file`, `write_file`, `list_files`, `get_current_directory`

### Streamlit Import Error

If Streamlit is not recognized:
```bash
pip install streamlit
```

Or with uv:
```bash
uv add streamlit
```

### API Key Error

Ensure your `.env` file contains a valid Groq API key:
```env
GROQ_API_KEY=gsk_...
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- Powered by [Groq](https://groq.com/)
- UI created with [Streamlit](https://streamlit.io/)

## 📧 Contact

**Muhammad Shaheer Khan**

- GitHub: [@shaheerkhan00](https://github.com/shaheerkhan00)
- Project Link: [https://github.com/shaheerkhan00/AI-Web-App-Builder](https://github.com/shaheerkhan00/AI-Web-App-Builder)
- Demo Video: [https://youtu.be/c6O0EEuOjNE](https://youtu.be/c6O0EEuOjNE)

---

**Made with ❤️ by Muhammad Shaheer Khan**

⭐ If you found this project helpful, please consider giving it a star on GitHub!