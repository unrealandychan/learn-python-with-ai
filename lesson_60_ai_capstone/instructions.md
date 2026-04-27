# Lesson 60: Capstone Project — Build a Complete AI Application

You've learned Python from the ground up with an AI-first approach. Now it's time to put it all together and build a complete, functional AI application.

## Project Options

Choose one of the three capstone projects below based on your interests:

---

## Project A: AI Document Analyzer

**What it does**: Accepts a text document (or PDF text), analyzes it using an LLM, and produces:
- A concise summary
- Key topics extracted
- Sentiment analysis
- Actionable insights

**Skills used**: File I/O, JSON handling, OpenAI SDK, prompt engineering, error handling

**Architecture**:
```
document.txt → Chunker → Embedder → Vector DB
                                        ↓
User Query → Embedder → Semantic Search → Top Chunks → LLM → Answer
```

---

## Project B: AI Chatbot with Memory

**What it does**: A command-line chatbot that:
- Maintains conversation history across turns
- Has a configurable persona (system prompt)
- Saves/loads conversation history to disk
- Supports `/clear`, `/save`, `/load`, `/persona` commands

**Skills used**: OOP, File I/O, JSON, OpenAI SDK, asyncio

**Architecture**:
```
User Input → Command Parser → [Command] OR [Chat]
                                              ↓
                                   Conversation History
                                              ↓
                                    OpenAI Chat API
                                              ↓
                                    Display + Save
```

---

## Project C: Automated Data Pipeline with AI Insights

**What it does**: 
- Reads a CSV dataset (any kind)
- Uses Pandas for data cleaning and analysis
- Generates statistical summaries with NumPy
- Uses an LLM to generate natural-language insights
- Creates visualizations with Matplotlib
- Saves a PDF/text report

**Skills used**: Pandas, NumPy, Matplotlib, OpenAI SDK, File I/O

---

## Your Implementation

The `exercise.py` file implements **Project B: AI Chatbot with Memory** as a complete, runnable example using a mock LLM. It demonstrates all the patterns you need.

## Code Quality Checklist

Before considering your project complete:

- [ ] Functions are small and have a single responsibility
- [ ] All functions have docstrings explaining parameters and return values
- [ ] Error handling is in place (try/except for API calls, file I/O)
- [ ] Sensitive config (API keys) loaded from environment variables
- [ ] Code is readable — clear variable names, no magic numbers
- [ ] The application handles edge cases (empty input, missing files, API errors)
- [ ] There's a clear entry point (`if __name__ == "__main__":`)

## Extending Your Project

Once you have the basics working, extend with:

1. **Add a simple web interface** using FastAPI (Lesson 46)
2. **Add persistence** — save conversations to SQLite (Lesson 51)
3. **Add streaming** — show responses word-by-word
4. **Add tool use** — let the chatbot search the web or run code
5. **Add RAG** — give the chatbot access to your own documents
6. **Deploy it** — host on a free service like Railway or Fly.io

## What You've Accomplished

By completing this course, you can now:

✅ Write clean, idiomatic Python from scratch  
✅ Work with all core data structures and algorithms  
✅ Build object-oriented programs with proper design patterns  
✅ Handle files, APIs, databases, and async I/O  
✅ Analyze data with Pandas, NumPy, and Matplotlib  
✅ Call and work with LLM APIs (OpenAI, LangChain)  
✅ Build AI pipelines with prompt engineering  
✅ Create simple AI agents with tool use  
✅ Understand vector embeddings and semantic search  
✅ Build production-grade REST APIs with FastAPI  
✅ Write tests, use linters, and manage dependencies  

**You are ready to build real AI applications. Go build something amazing! 🚀**

---

### Final Challenge

Build your own original AI application. Requirements:
1. Uses at least one external API (OpenAI, or any other)
2. Stores data (file, database, or in-memory)
3. Has proper error handling
4. Is a tool someone else would actually want to use

Share it on GitHub with a good README!
