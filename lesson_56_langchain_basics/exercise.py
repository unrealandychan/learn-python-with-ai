"""
Lesson 56: LangChain Basics — Building AI Pipelines
Exercise File

This file simulates LangChain components so it runs without API keys.
The patterns are identical to real LangChain code.
"""


# ============================================================
# MOCK LANGCHAIN COMPONENTS
# These mimic real LangChain interfaces exactly.
# To use real LangChain, replace these with:
#   from langchain_openai import ChatOpenAI
#   from langchain_core.prompts import ChatPromptTemplate
#   from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
# ============================================================

import json


class HumanMessage:
    def __init__(self, content):
        self.content = content
        self.type = "human"

class SystemMessage:
    def __init__(self, content):
        self.content = content
        self.type = "system"

class AIMessage:
    def __init__(self, content):
        self.content = content
        self.type = "ai"


class MockChatOpenAI:
    """Simulates langchain_openai.ChatOpenAI"""
    
    def __init__(self, model="gpt-4o-mini", temperature=0.7):
        self.model = model
        self.temperature = temperature

    def invoke(self, messages):
        if isinstance(messages, str):
            text = messages
        elif isinstance(messages, list):
            text = " ".join(m.content for m in messages if hasattr(m, 'content'))
        else:
            text = str(messages)

        text_lower = text.lower()
        if "json" in text_lower or "format" in text_lower:
            content = '{"title": "Inception", "rating": 9.2, "summary": "A mind-bending thriller about dream invasion."}'
        elif "name" in text_lower and "alice" in text_lower:
            content = "Your name is Alice."
        elif "generator" in text_lower:
            content = "A generator is a function that yields values lazily, one at a time, using the 'yield' keyword."
        elif "recursion" in text_lower:
            content = "Recursion is when a function calls itself to solve a smaller instance of the same problem."
        elif "explain" in text_lower or "what is" in text_lower:
            content = "This is an important concept in Python that helps you write cleaner, more efficient code."
        else:
            content = f"[LangChain simulated response for: {text[:50]}]"

        return AIMessage(content=content)

    def __or__(self, other):
        """Support pipe operator: llm | parser"""
        return MockChain([self, other])


class MockChatPromptTemplate:
    """Simulates langchain_core.prompts.ChatPromptTemplate"""
    
    def __init__(self, messages_template):
        self.messages_template = messages_template
    
    @classmethod
    def from_template(cls, template):
        obj = cls([("human", template)])
        obj._template = template
        return obj
    
    @classmethod
    def from_messages(cls, messages):
        return cls(messages)
    
    def format_messages(self, **kwargs):
        msgs = []
        for role, template in self.messages_template:
            content = template
            for k, v in kwargs.items():
                content = content.replace("{" + k + "}", str(v))
            if role == "system":
                msgs.append(SystemMessage(content=content))
            elif role == "human":
                msgs.append(HumanMessage(content=content))
            elif role == "ai":
                msgs.append(AIMessage(content=content))
        return msgs
    
    def invoke(self, kwargs):
        return self.format_messages(**kwargs)
    
    def __or__(self, other):
        return MockChain([self, other])


class MockStrOutputParser:
    """Simulates langchain_core.output_parsers.StrOutputParser"""
    
    def invoke(self, message):
        if isinstance(message, AIMessage):
            return message.content
        return str(message)
    
    def __or__(self, other):
        return MockChain([self, other])


class MockJsonOutputParser:
    """Simulates langchain_core.output_parsers.JsonOutputParser"""
    
    def invoke(self, message):
        content = message.content if isinstance(message, AIMessage) else str(message)
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return {"error": "Failed to parse JSON", "raw": content}
    
    def __or__(self, other):
        return MockChain([self, other])


class MockChain:
    """Simulates a LangChain LCEL chain (chained with |)"""
    
    def __init__(self, components):
        self.components = components
    
    def invoke(self, input_data):
        result = input_data
        for component in self.components:
            if isinstance(result, dict):
                result = component.invoke(result)
            else:
                result = component.invoke(result)
        return result
    
    def __or__(self, other):
        return MockChain(self.components + [other])


class MockMemory:
    """Simulates conversation memory"""
    
    def __init__(self):
        self.messages = []
        self.name = None
    
    def add_message(self, message):
        self.messages.append(message)
        # Extract name if mentioned
        if "my name is" in message.content.lower():
            words = message.content.lower().split("my name is ")
            if len(words) > 1:
                self.name = words[1].strip().split()[0].capitalize()


# ---- Convenient aliases ----
ChatOpenAI = MockChatOpenAI
ChatPromptTemplate = MockChatPromptTemplate
StrOutputParser = MockStrOutputParser
JsonOutputParser = MockJsonOutputParser


# ===========================================================
# EXERCISE 1: Basic LangChain Chain
# ===========================================================
# TODO: Create an LCEL chain that:
# 1. Takes a topic as input
# 2. Uses ChatPromptTemplate.from_template() to create a prompt:
#    "Explain {topic} to a complete beginner in Python in 2 sentences."
# 3. Pipes it through ChatOpenAI
# 4. Pipes the result through StrOutputParser
# 5. Invoke the chain with topic="list comprehensions"
# 6. Print the result

print("=" * 50)
print("Exercise 1: Basic LCEL Chain")
print("=" * 50)

llm = ChatOpenAI(model="gpt-4o-mini")

# YOUR CODE HERE:


# ===========================================================
# EXERCISE 2: Multi-Variable Prompt Template
# ===========================================================
# TODO: Build a chain using ChatPromptTemplate.from_messages() with:
# - A system message: "You are a {persona}."
# - A human message: "Please {action} the following: {content}"
# Chain it with the LLM and StrOutputParser.
# Invoke it to:
#   persona = "Python code reviewer"
#   action = "review"
#   content = "for i in range(len(my_list)): print(my_list[i])"

print("\n" + "=" * 50)
print("Exercise 2: Multi-Variable Template")
print("=" * 50)

# YOUR CODE HERE:


# ===========================================================
# EXERCISE 3: Conversation with Memory
# ===========================================================
# TODO: Simulate a multi-turn conversation that remembers context.
# Use the MockMemory class to store messages.
# Conversation:
#   Turn 1: "My name is Bob and I'm learning Python."
#   Turn 2: "What's my name?" (AI should say "Bob")
#   Turn 3: "What am I learning?" (AI should say "Python")
#
# Build a simple function chat(memory, user_message) that:
# 1. Adds user message to memory
# 2. Builds a prompt from all messages in memory
# 3. Gets a response from the LLM
# 4. Adds AI response to memory
# 5. Returns the AI response

print("\n" + "=" * 50)
print("Exercise 3: Conversation with Memory")
print("=" * 50)

memory = MockMemory()

def chat(memory: MockMemory, user_message: str) -> str:
    """Simple chat function with memory."""
    # YOUR CODE HERE
    pass


# Test the conversation:
turns = [
    "My name is Bob and I'm learning Python.",
    "What's my name?",
    "What am I learning?"
]
for message in turns:
    response = chat(memory, message)
    print(f"User: {message}")
    print(f"AI: {response}\n")


# ===========================================================
# EXERCISE 4: Simple RAG Chain
# ===========================================================
# TODO: Implement a simple RAG (Retrieval-Augmented Generation) function.
# Given a list of documents and a question:
# 1. Join all documents as context
# 2. Build a prompt that includes the context
# 3. Ask the LLM to answer ONLY based on the context
# 4. Return the answer

KNOWLEDGE_BASE = [
    "Python was created by Guido van Rossum and first released in 1991.",
    "Python 3.12, released in 2023, includes a 5% performance improvement.",
    "The OpenAI Python SDK can be installed with: pip install openai",
    "LangChain is a framework for building applications powered by LLMs.",
    "FastAPI is a modern, fast web framework for building APIs with Python.",
]

def simple_rag(question: str, documents: list, llm) -> str:
    """Answer a question using context from documents."""
    # YOUR CODE HERE
    pass


print("=" * 50)
print("Exercise 4: Simple RAG Chain")
print("=" * 50)
questions = [
    "When was Python created?",
    "How do I install the OpenAI SDK?",
]
for q in questions:
    answer = simple_rag(q, KNOWLEDGE_BASE, llm)
    print(f"Q: {q}")
    print(f"A: {answer}\n")


print("✅ LangChain exercises complete!")
