<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,30,2&height=160&section=header&text=learn--python--with--ai&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=The+only+Python+course+you+need+in+the+AI+era&descAlignY=58&descSize=14" alt="Header"/>

[![Stars](https://img.shields.io/github/stars/unrealandychan/learn-python-with-ai?style=for-the-badge&logo=github&color=f78166&logoColor=white&labelColor=0d1117)](https://github.com/unrealandychan/learn-python-with-ai/stargazers)
[![Forks](https://img.shields.io/github/forks/unrealandychan/learn-python-with-ai?style=for-the-badge&logo=github&color=79c0ff&logoColor=white&labelColor=0d1117)](https://github.com/unrealandychan/learn-python-with-ai/network/members)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&style=for-the-badge&logoColor=white&labelColor=0d1117)](https://python.org)
[![60 Lessons](https://img.shields.io/badge/60_Lessons-AI--First-blueviolet?style=for-the-badge&labelColor=0d1117)](.)
[![License](https://img.shields.io/github/license/unrealandychan/learn-python-with-ai?style=for-the-badge&labelColor=0d1117)](LICENSE)

</div>

---

# 🤖 The Only Python Course You Need in the AI Era

[中文版](README_zh.md) | [Quick Start](#-quick-start) | [Curriculum](#-curriculum) | [Tech Stack](#-tech-stack)

![Banner](public/banner.png)

> **60 lessons. Zero prerequisites. One goal: make you a Python developer who builds real AI applications.**

---

## 🎯 Course Philosophy

Most Python courses teach you to print "Hello, World!" and move on. This course is different.

**Every concept is taught through an AI lens:**

- Instead of "learn variables" → **"parse an LLM API response into variables"**
- Instead of "learn lists" → **"process a batch of AI-generated outputs"**
- Instead of "learn file I/O" → **"save and load conversation histories"**
- Instead of "learn classes" → **"build reusable AI pipeline components"**

By the end, you won't just know Python — you'll be able to build AI applications that actually work.

---

## ✨ Highlights

| | |
|---|---|
| 🎓 **60 Lessons** | From "Hello World" to production AI apps |
| 🤖 **AI-First** | Every exercise uses AI context and real-world patterns |
| 🔨 **Project-Based** | Build real things: chatbots, agents, APIs, data pipelines |
| 📦 **Modern Stack** | OpenAI SDK, LangChain, FastAPI, Pandas, NumPy |
| 🆓 **No API Key Needed** | All exercises run with mock clients — swap in real API when ready |
| 🔰 **Zero Prerequisites** | Truly beginner friendly — no prior programming experience required |

---

## 🚀 Quick Start

### 1. Get the Code

```bash
git clone https://github.com/unrealandychan/learn-python-with-ai.git
cd learn-python-with-ai
```

### 2. Set Up Python (3.11+)

```bash
# Check your version
python --version   # Should be 3.11 or higher

# If not installed: https://www.python.org/downloads/
```

### 3. Create a Virtual Environment

```bash
# Using uv (recommended — fastest)
curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv && source .venv/bin/activate

# OR using standard pip
python -m venv .venv && source .venv/bin/activate  # macOS/Linux
python -m venv .venv && .venv\Scripts\activate      # Windows
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Start Learning!

```bash
# Start with lesson 1
cd lesson_01_intro_to_python
python exercise.py
```

### 6. (Optional) Add Your OpenAI API Key

```bash
# Create a .env file
echo "OPENAI_API_KEY=sk-your-key-here" > .env
```

> **Note**: All lessons work with mock AI clients — you don't need an API key to learn. Add one when you're ready to use the real APIs.

---

## 📚 Curriculum

### 🟢 Module 1: Python Foundations (Lessons 1–20)
*Core Python with an AI context — understand every concept in terms of how it's used in AI development.*

| Lesson | Topic | AI Application |
|--------|-------|----------------|
| 01 | Intro to Python | Why Python dominates AI |
| 02 | Variables & Data Types | Storing LLM responses in variables |
| 03 | Basic Operators | Processing API response scores |
| 04 | User Input & Type Casting | Building interactive AI tools |
| 05 | Conditional Statements | Routing based on AI classification results |
| 06 | Lists | Storing multiple AI-generated items |
| 07 | List Methods | Managing conversation message arrays |
| 08 | For Loops | Iterating over batch AI results |
| 09 | While Loops | Retry logic for API calls |
| 10 | Dictionaries | Parsing JSON API responses |
| 11 | Tuples & Sets | Deduplicating AI outputs |
| 12 | Defining Functions | Reusable AI helper functions |
| 13 | Function Arguments & Returns | Building flexible API wrappers |
| 14 | Variable Scope | Managing API keys and config |
| 15 | Modules & Importing | Using the AI library ecosystem |
| 16 | File I/O: Reading | Loading prompts and knowledge bases |
| 17 | File I/O: Writing | Saving AI outputs to disk |
| 18 | Error Handling | Robust API call error handling |
| 19 | OOP Intro | Modeling AI conversations as objects |
| 20 | Next Steps | Mini project: command-line AI assistant |

### 🟡 Module 2: Advanced Python (Lessons 21–40)
*Advanced patterns that every AI engineer uses daily.*

| Lesson | Topic | AI Application |
|--------|-------|----------------|
| 21 | OOP Inheritance | Specialized AI model clients |
| 22 | OOP Polymorphism | Interchangeable AI providers |
| 23 | OOP Encapsulation | Protecting API keys in classes |
| 24 | OOP Dunder Methods | Custom AI response objects |
| 25 | Static & Class Methods | Shared configuration across AI clients |
| 26 | List Comprehensions | Transforming batches of AI outputs |
| 27 | Dict & Set Comprehensions | Aggregating AI result metrics |
| 28 | Lambda Functions | Inline transformation of AI data |
| 29 | Map, Filter, Reduce | Functional pipelines for AI data |
| 30 | Generators | Memory-efficient streaming of AI responses |
| 31 | Decorators | Rate limiting, logging, caching AI calls |
| 32 | Collections Module | Counting tokens, frequency analysis |
| 33 | Dates & Times | Timestamping AI interactions |
| 34 | JSON Data | Parsing LLM JSON output |
| 35 | OS & Sys Modules | File system operations for AI pipelines |
| 36 | Multithreading | Parallel AI API calls |
| 37 | Multiprocessing | CPU-bound AI preprocessing |
| 38 | Asyncio Intro | Understanding async AI workflows |
| 39 | Async/Await | Async LLM calls with streaming |
| 40 | Advanced Project | Build an async AI pipeline |

### 🔵 Module 3: Essential Libraries (Lessons 41–53)
*The libraries that power real-world Python and AI applications.*

| Lesson | Topic | AI Application |
|--------|-------|----------------|
| 41 | Requests | Calling REST APIs and LLM endpoints |
| 42 | BeautifulSoup4 | Scraping training data from the web |
| 43 | Pandas | Data preparation for ML models |
| 44 | Matplotlib | Visualizing AI model metrics |
| 45 | Seaborn | Statistical visualization for model analysis |
| 46 | FastAPI | Serving AI models as REST APIs |
| 47 | Git & GitHub | Version-controlling your AI projects |
| 48 | Pytest | Testing AI application components |
| 49 | Ruff | Code quality for production AI code |
| 50 | UV Dependency Management | Managing AI project dependencies |
| 51 | Databases | Storing AI conversation history |
| 52 | Config Management | Secure API key management with .env |
| 53 | Python for MCP & Skills | Building tool-calling infrastructure |

### 🔴 Module 4: AI & LLM Integration (Lessons 54–60)
*The cutting edge — calling, prompt-engineering, and building with LLMs.*

| Lesson | Topic | AI Application |
|--------|-------|----------------|
| 54 | **OpenAI SDK** | Chat completions, streaming, function calling, JSON mode |
| 55 | **Prompt Engineering** | Few-shot prompting, CoT, output formatting, templates |
| 56 | **LangChain Basics** | LCEL chains, memory, output parsers, RAG pattern |
| 57 | **NumPy for AI** | Vector math, cosine similarity, softmax, embeddings |
| 58 | **AI Agents** | ReAct pattern, tool registries, the agent loop |
| 59 | **Vector Embeddings** | Semantic search, simple vector DB, chunking |
| 60 | **Capstone Project** | Build a complete AI application from scratch |

---

## 🛠 Tech Stack

This course uses the modern Python AI ecosystem:

| Category | Libraries |
|----------|-----------|
| **LLM APIs** | `openai`, `langchain`, `langchain-openai` |
| **Data Science** | `numpy`, `pandas`, `matplotlib`, `seaborn` |
| **Web / APIs** | `fastapi`, `httpx`, `requests`, `uvicorn` |
| **Config** | `python-dotenv` |
| **Dev Tools** | `pytest`, `ruff`, `uv` |
| **Databases** | `sqlalchemy` |
| **Scraping** | `beautifulsoup4` |

---

## 📋 Prerequisites

**None.** This course starts from absolute zero.

You need:
- A computer (Windows, macOS, or Linux)
- Internet connection
- Curiosity and willingness to learn

You do NOT need:
- Prior programming experience
- Math background
- An OpenAI API key (all exercises work with mock clients)

---

## 📁 Lesson Structure

Every lesson follows the same structure:

```
lesson_XX_topic_name/
├── instructions.md    ← Read this first: theory, examples, concepts
├── exercise.py        ← Your playground: complete the TODO exercises
└── solution.py        ← Check your work after trying yourself
```

**How to use each lesson:**
1. 📖 Read `instructions.md` from top to bottom
2. ✏️ Open `exercise.py` and complete the `# YOUR CODE HERE` sections
3. 🚀 Run your file: `python exercise.py`
4. 🔍 Compare with `solution.py` if you're stuck

---

## 💡 Learning Tips

- **Type the code** — don't copy-paste. Typing builds muscle memory.
- **Break things** — modify the examples and see what happens.
- **Use AI as a tutor** — ask ChatGPT or Copilot to explain concepts you find confusing.
- **Don't skip** — each lesson builds on the previous ones.
- **Build something** — after each module, try building a small project with what you've learned.

---

## 🗺 Learning Path

```
Weeks 1-4:   Lessons 01-20  → Python Foundations
Weeks 5-8:   Lessons 21-40  → Advanced Python
Weeks 9-12:  Lessons 41-53  → Essential Libraries  
Weeks 13-15: Lessons 54-60  → AI & LLM Integration
```

> At ~4 lessons/week, you'll complete the course in ~15 weeks. Take your time — depth over speed.

---

## 🤝 Contributing

Found a bug? Have an improvement? Pull requests are welcome!

1. Fork the repo
2. Create a branch: `git checkout -b fix/lesson-42-typo`
3. Make your changes
4. Push and open a PR

---

## 📄 License

[MIT License](LICENSE) — free to use, share, and modify.

---

<div align="center">

**Happy learning! Build something amazing. 🚀**

*If this course helped you, please ⭐ star the repo — it helps others find it!*

</div>
