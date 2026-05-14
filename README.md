<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,30,2&height=160&section=header&text=learn--python--with--ai&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=The+only+Python+course+you+need+in+the+AI+era&descAlignY=58&descSize=14" alt="Header"/>

[![Stars](https://img.shields.io/github/stars/unrealandychan/learn-python-with-ai?style=for-the-badge&logo=github&color=f78166&logoColor=white&labelColor=0d1117)](https://github.com/unrealandychan/learn-python-with-ai/stargazers)
[![Forks](https://img.shields.io/github/forks/unrealandychan/learn-python-with-ai?style=for-the-badge&logo=github&color=79c0ff&logoColor=white&labelColor=0d1117)](https://github.com/unrealandychan/learn-python-with-ai/network/members)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&style=for-the-badge&logoColor=white&labelColor=0d1117)](https://python.org)
[![75 Lessons](https://img.shields.io/badge/75_Lessons-AI--First-blueviolet?style=for-the-badge&labelColor=0d1117)](.)
[![License](https://img.shields.io/github/license/unrealandychan/learn-python-with-ai?style=for-the-badge&labelColor=0d1117)](LICENSE)

</div>

---

# 🤖 The Only Python Course You Need in the AI Era

[中文版](README_zh.md) | [Español](README_es.md) | [Quick Start](#-quick-start) | [Curriculum](#-curriculum) | [Tech Stack](#-tech-stack)

![Banner](public/banner.png)

> **75 lessons. Zero prerequisites. One goal: make you a Python developer who builds real AI applications.**

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
| 🎓 **75 Lessons** | From "Hello World" to production AI apps |
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
cd module_01_python_foundations/lesson_01_intro_to_python
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

> 75 lessons organised into 6 modules. Each lesson has `instructions.md`, `exercise.py`, and `solution.py`.

---

### 🟢 Module 1 — Python Foundations (`module_01_python_foundations`)
*Core Python — every concept taught through the lens of AI development.*

| Lesson | Topic | AI Application |
|--------|-------|----------------|
| 01 | Intro to Python | Why Python dominates AI |
| 02 | Variables & Data Types | Storing LLM responses |
| 03 | Basic Operators | Processing API response scores |
| 04 | User Input & Type Casting | Building interactive AI tools |
| 05 | Conditional Statements | Routing based on AI classification |
| 06 | Lists | Storing AI-generated items |
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

---

### 🔵 Module 2 — Object-Oriented Programming (`module_02_oop`)
*Foundations to advanced OOP — 4 pillars, design patterns, ABCs, and modern Python OOP.*

| Lesson | Topic | Key Concept |
|--------|-------|-------------|
| 19 | OOP Intro | Classes, objects, `__init__`, `self` |
| 20 | Next Steps | Mini project: CLI AI assistant |
| 21 | Inheritance | `super()`, parent/child classes |
| 22 | Polymorphism | Method overriding, duck typing |
| 23 | Encapsulation | Public / `_protected` / `__private` |
| 24 | Dunder Methods | `__str__`, `__repr__`, `__len__`, `__add__` |
| 25 | Static & Class Methods | `@staticmethod`, `@classmethod` |
| 61 | **Abstract Classes & ABCs** | `abc.ABC`, `@abstractmethod`, LLM Provider pattern |
| 62 | **Multiple Inheritance & MRO** | C3 linearization, diamond problem, Mixins |
| 63 | **@property** | Getters, setters, computed attributes |
| 64 | **Design Patterns** | Singleton, Factory, Observer, Strategy |
| 65 | **Dataclasses** | `@dataclass`, `frozen`, `field`, `__post_init__` |

---

### 🟡 Module 3 — Advanced Python (`module_03_advanced_python`)
*Advanced patterns that every AI engineer uses daily.*

| Lesson | Topic | AI Application |
|--------|-------|----------------|
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

---

### 🔴 Module 4 — Data Structures & Algorithms (`module_04_data_structures_and_algorithms`)
*CS fundamentals for coding interviews — Big-O, classic data structures, algorithm patterns.*

| Lesson | Topic | Key Concept |
|--------|-------|-------------|
| 66 | **Stack & Queue** | MinStack, BrowserHistory, `collections.deque` |
| 67 | **Linked List** | Reverse, find middle, remove duplicates |
| 68 | **Binary Trees & BST** | Traversals, height, is_balanced |
| 69 | **Heap & Priority Queue** | `heapq`, MedianFinder (two-heap), Top-K |
| 70 | **Graphs: BFS & DFS** | Adjacency list, shortest path, is_connected |
| 71 | **Big-O Complexity** | All rules, Python built-in complexities |
| 72 | **Recursion & DP** | Memoisation, tabulation, Coin Change, LCS |
| 73 | **Sorting & Binary Search** | Merge Sort, Binary Search, Rotated Array |
| 74 | **Hash Maps & Sets** | Two-Sum, Group Anagrams, LRU Cache |
| 75 | **Interview Cheat Sheet** | OOP/DS/algorithms quick reference |

---

### 🟣 Module 5 — Essential Libraries (`module_05_essential_libraries`)
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

---

### 🟠 Module 6 — AI & LLM Integration (`module_06_ai_and_llm`)
*The cutting edge — calling, prompt-engineering, and building with LLMs.*

| Lesson | Topic | Key Concept |
|--------|-------|-------------|
| 54 | OpenAI SDK | Chat completions, streaming, function calling |
| 55 | Prompt Engineering | Few-shot, CoT, output formatting, templates |
| 56 | LangChain Basics | LCEL, memory, RAG chains |
| 57 | NumPy | Vectors, cosine similarity, softmax |
| 58 | AI Agents | ReAct pattern, tool registries |
| 59 | Vector Embeddings | Semantic search, vector databases |
| 60 | AI Capstone | Full end-to-end AI application |

---

## 📁 Lesson Structure

Every lesson follows the same structure:

```
module_XX_name/lesson_XX_topic_name/
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
Weeks 1-4:   Module 1 (Lessons 01-18) → Python Foundations
Weeks 5-8:   Module 2 (Lessons 19-25, 61-65) → OOP
Weeks 9-10:  Module 3 (Lessons 26-40) → Advanced Python
Weeks 11-12: Module 4 (Lessons 66-75) → Data Structures & Algorithms
Weeks 13-14: Module 5 (Lessons 41-53) → Essential Libraries
Weeks 15-16: Module 6 (Lessons 54-60) → AI & LLM Integration
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
