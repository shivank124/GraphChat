# 🤖 GraphChat: AI Chatbot with LangGraph

An intelligent multi-use-case chatbot application built with **LangGraph**, **Groq LLM**, and **Streamlit**. This project demonstrates advanced AI agent orchestration with support for basic chatting, web search integration, and AI news summarization.

## ✨ Features

- **Basic Chatbot**: Simple conversational AI using Groq LLM
- **Chatbot with Web Search**: Advanced chatbot with real-time web search capabilities using Tavily
- **AI News Summarization**: Fetches and summarizes the latest AI news from around the world
- **Streamlit UI**: Interactive web-based user interface
- **LangGraph Integration**: Powerful agent workflow orchestration
- **Multi-LLM Support**: Groq LLM integration with multiple model options
- **State Management**: Robust state handling for complex workflows

## 📁 Project Structure

```
AI Chatbot/
├── app.py                          # Main entry point
├── requirements.txt                # Project dependencies
├── README.md                       # This file
│
└── src/
    └── langgraphagenticai/
        ├── main.py                 # Application loader
        ├── __init__.py
        │
        ├── graph/
        │   ├── graph_builder.py    # LangGraph graph construction
        │   └── __init__.py
        │
        ├── LLMS/
        │   ├── groqllm.py          # Groq LLM configuration
        │   └── __init__.py
        │
        ├── nodes/
        │   ├── basic_chatbot_node.py        # Basic chatbot logic
        │   ├── chatbot_with_Tool_node.py    # Web search chatbot
        │   ├── ai_news_node.py              # News fetching & summarization
        │   └── __init__.py
        │
        ├── state/
        │   ├── state.py            # State schema definition
        │   └── __init__.py
        │
        ├── tools/
        │   ├── search_tool.py      # Tool definitions
        │   └── __init__.py
        │
        └── ui/
            ├── uiconfigfile.ini    # UI configuration
            ├── uiconfigfile.py     # UI config parser
            ├── __init__.py
            │
            └── streamlitui/
                ├── loadui.py           # UI loader & controls
                ├── display_result.py   # Result display handler
                └── __init__.py
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Groq API Key (get from [console.groq.com](https://console.groq.com/keys))
- Tavily API Key (for web search, get from [app.tavily.com](https://app.tavily.com/home))

### Installation

1. **Clone or download the project**
   ```bash
   cd "AI Project/AI Chatbot"
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

### API Keys Setup

The application requires API keys for:

1. **Groq LLM**: Get from [console.groq.com/keys](https://console.groq.com/keys)
2. **Tavily Search** (for web search use case): Get from [app.tavily.com](https://app.tavily.com/home)

These keys will be prompted for in the Streamlit UI sidebar when you select the respective use cases.

### Supported Groq Models

Common models available:
- `qwen/qwen3-32b`
- `llama-3.3-70b-versatile`
- `openai/gpt-oss-120b`

## 🎯 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Use Cases

#### 1. **Basic Chatbot**
- Simple conversational AI
- No external tools needed
- Just chat naturally with the AI

**Steps:**
1. Select "Basic Chatbot" from the usecase dropdown
2. Enter your Groq API key
3. Select your preferred model
4. Type your message and chat!

#### 2. **Chatbot with Web**
- Enhanced chatbot with real-time web search
- Retrieves current information from the web
- Combines knowledge with web search results

**Requirements:**
- Groq API Key
- Tavily API Key

**Steps:**
1. Select "Chatbot with Web" from the usecase dropdown
2. Enter your Groq API key and select model
3. Enter your Tavily API key
4. Ask questions and get web-informed answers!

#### 3. **AI News**
- Fetches latest AI news from around the world
- Summarizes news in markdown format
- Available frequencies: Daily, Weekly, Monthly, Yearly

**Requirements:**
- Groq API Key
- Tavily API Key

**Steps:**
1. Select "AI News" from the usecase dropdown
2. Enter your API keys and select frequency
3. Results are generated and displayed in markdown format
4. Summaries are saved to `./AINews/` directory

## 🔧 Key Components

### Graph Builder (`graph_builder.py`)
Constructs LangGraph workflows for different use cases:
- **basic_chatbot_build_graph()**: Simple linear workflow
- **chatbot_with_tools_build_graph()**: Complex workflow with tool integration
- **ai_news_builder_graph()**: Multi-step news pipeline

### State Management (`state.py`)
Defines the state schema used across all workflows:
```python
class State(TypedDict):
    messages: Annotated[List, add_messages]
```

### Node Processing
Each node processes state and returns updated state:
- `BasicChatbotNode`: Direct LLM invocation
- `ChatbotWithToolNode`: LLM with tool binding
- `AINewsNode`: News fetching, summarization, and persistence

## 🛠️ Troubleshooting

### Common Errors & Solutions

| Error | Solution |
|-------|----------|
| `'module' object is not callable` | Fixed by correctly importing `ToolNode` class instead of `tool_node` module |
| `'messages': minimum number of items is 1` | Fixed by wrapping user input in `HumanMessage()` objects |
| `'charmap' codec can't encode character` | Fixed by using `encoding='utf-8'` when reading/writing files |
| `[Errno 2] No such file or directory: './AINews/'` | Fixed by creating directory with `os.makedirs()` before file operations |
| `KeyError: 'summary'` | Fixed by ensuring correct graph execution order: fetch → summarize → save |

## 📦 Dependencies

- **langchain**: LLM framework
- **langgraph**: Agent orchestration
- **streamlit**: Web UI framework
- **langchain-groq**: Groq LLM integration
- **langchain-tavily**: Tavily search tool
- **faiss-cpu**: Vector store for embeddings

See `requirements.txt` for the complete list.

## 🔐 Security Notes

- Never hardcode API keys in your code
- API keys are entered via the Streamlit UI
- Store API keys in environment variables for production
- The application doesn't save API keys permanently

## 📝 Logging & Output

- Console logs are printed for debugging
- AI News summaries are saved to `./AINews/{frequency}_summary.md`
- Streamlit displays real-time output and errors in the UI

## 🤝 Contributing

Feel free to:
- Add new use cases
- Improve the UI
- Add more tools
- Optimize performance

## 📄 License

This project is open source.

## ❓ FAQ

**Q: What if I don't have a Groq API key?**
A: Get one free at [console.groq.com](https://console.groq.com/keys). Groq offers free API access.

**Q: Can I use a different LLM?**
A: Yes! You can modify `src/langgraphagenticai/LLMS/groqllm.py` to use OpenAI, Anthropic, or other LLMs.

**Q: How do I add a new use case?**
A: Create a new node class in `src/langgraphagenticai/nodes/`, then add a graph builder method in `graph_builder.py`.

**Q: Where are the AI News summaries saved?**
A: In the `./AINews/` directory relative to where you run the app.

---

**Happy Chatting! 🚀**