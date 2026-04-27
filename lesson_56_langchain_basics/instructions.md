# Lesson 56: LangChain Basics — Building AI Pipelines

LangChain is the most widely used framework for building LLM-powered applications. It provides high-level abstractions for chains, memory, tools, and agents — letting you build complex AI workflows in clean, composable Python code.

## Why LangChain?

Raw API calls work fine for simple use cases. But production AI apps need:
- **Memory**: Conversations that remember context
- **Chains**: Multi-step workflows where each step's output feeds the next
- **Tools**: AI that can call functions, search the web, query databases
- **Agents**: AI that decides which tools to use and when

LangChain provides all of this.

## Installation

```bash
pip install langchain langchain-openai python-dotenv
```

## Core Concepts

### 1. Chat Models

```python
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

messages = [
    SystemMessage(content="You are a helpful Python tutor."),
    HumanMessage(content="What is a generator?")
]

response = llm.invoke(messages)
print(response.content)
```

### 2. Prompt Templates

```python
from langchain_core.prompts import ChatPromptTemplate

template = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. Answer in {language}."),
    ("human", "{question}")
])

# Format the template with variables
prompt = template.format_messages(
    role="Python expert",
    language="simple English",
    question="What is a context manager?"
)
```

### 3. The LangChain Expression Language (LCEL)

LCEL uses the `|` pipe operator to chain components:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(model="gpt-4o-mini")

chain = (
    ChatPromptTemplate.from_template("Explain {concept} in one sentence.")
    | llm
    | StrOutputParser()
)

result = chain.invoke({"concept": "recursion"})
print(result)  # "Recursion is when a function calls itself..."
```

### 4. Conversation Memory

```python
from langchain_openai import ChatOpenAI
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

llm = ChatOpenAI(model="gpt-4o-mini")
history = InMemoryChatMessageHistory()

chain_with_history = RunnableWithMessageHistory(llm, lambda session_id: history)

# Turn 1
response = chain_with_history.invoke(
    [HumanMessage(content="My name is Alice.")],
    config={"configurable": {"session_id": "session1"}}
)

# Turn 2 — the AI remembers "My name is Alice"
response = chain_with_history.invoke(
    [HumanMessage(content="What's my name?")],
    config={"configurable": {"session_id": "session1"}}
)
print(response.content)  # "Your name is Alice."
```

### 5. Output Parsers

Parse AI output into structured Python objects:

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field

class MovieReview(BaseModel):
    title: str = Field(description="Movie title")
    rating: float = Field(description="Rating from 0 to 10")
    summary: str = Field(description="One sentence summary")

parser = JsonOutputParser(pydantic_object=MovieReview)

template = ChatPromptTemplate.from_template(
    "Review the movie '{movie}'. {format_instructions}"
)

chain = template | llm | parser

# Returns a typed MovieReview object
review = chain.invoke({
    "movie": "Inception",
    "format_instructions": parser.get_format_instructions()
})
print(review.title)   # "Inception"
print(review.rating)  # 9.2
```

### 6. Simple RAG Pattern (Retrieval-Augmented Generation)

```python
from langchain_core.prompts import ChatPromptTemplate

# Your documents/knowledge base
documents = [
    "Python was created by Guido van Rossum in 1991.",
    "The Zen of Python can be read by typing 'import this'.",
    "Python uses indentation to define code blocks."
]

def simple_rag(question: str, docs: list[str]) -> str:
    """Simple RAG: stuff relevant docs into context."""
    context = "\n".join(docs)
    
    template = ChatPromptTemplate.from_messages([
        ("system", "Answer questions using only the provided context.\n\nContext:\n{context}"),
        ("human", "{question}")
    ])
    
    chain = template | llm | StrOutputParser()
    return chain.invoke({"context": context, "question": question})

answer = simple_rag("When was Python created?", documents)
print(answer)  # "Python was created in 1991."
```

## Key LangChain Components

| Component | Purpose |
|-----------|---------|
| `ChatOpenAI` | Interface to OpenAI chat models |
| `ChatPromptTemplate` | Reusable, parameterized prompts |
| `StrOutputParser` | Parse AI response as plain string |
| `JsonOutputParser` | Parse AI response as JSON/dict |
| `InMemoryChatMessageHistory` | Store conversation in memory |
| `RunnableWithMessageHistory` | Wrap a chain with memory |

## When to Use LangChain vs Raw API

| Use Raw API When | Use LangChain When |
|-----------------|-------------------|
| Simple one-shot calls | Multi-step chains |
| Learning the basics | Production applications |
| Minimal dependencies | Need memory, tools, agents |
| Full control needed | Rapid prototyping |

---

### Quiz

1. **What does the `|` operator do in LangChain Expression Language?**
2. **What problem does conversation memory solve?**
3. **What is RAG (Retrieval-Augmented Generation)?**

<details>
  <summary><b>Answer Key</b></summary>
  1. The pipe operator chains components together — the output of the left component becomes the input of the right component.
  2. LLMs are stateless by default. Memory solves this by storing previous messages and including them in each new request, giving the AI conversation context.
  3. RAG retrieves relevant documents from a knowledge base and includes them in the prompt as context, allowing the AI to answer questions based on your specific data rather than just its training data.
</details>
