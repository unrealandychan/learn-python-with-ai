"""
Lesson 56: LangChain Basics — Solutions
"""

import json


# ---- Same mock classes as exercise ----
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
    def __init__(self, model="gpt-4o-mini", temperature=0.7):
        self.model = model
        self.temperature = temperature

    def invoke(self, messages):
        if isinstance(messages, list):
            text = " ".join(m.content for m in messages if hasattr(m, 'content'))
        else:
            text = str(messages)
        
        text_lower = text.lower()
        if "json" in text_lower:
            content = '{"title": "Inception", "rating": 9.2, "summary": "A mind-bending thriller."}'
        elif "bob" in text_lower and ("name" in text_lower):
            content = "Your name is Bob."
        elif "learning" in text_lower and "what" in text_lower:
            content = "You are learning Python."
        elif "1991" in text_lower or "when was python" in text_lower:
            content = "Python was created by Guido van Rossum and first released in 1991."
        elif "install" in text_lower and "openai" in text_lower:
            content = "You can install the OpenAI Python SDK with: pip install openai"
        elif "comprehension" in text_lower or "explain" in text_lower:
            content = "List comprehensions are a concise way to create lists. For example: [x*2 for x in range(5)] creates [0, 2, 4, 6, 8]."
        elif "review" in text_lower:
            content = "Code review: Instead of 'for i in range(len(my_list))', use 'for item in my_list:' which is more Pythonic and readable."
        else:
            content = f"[Response to: {text[:50]}]"
        
        return AIMessage(content=content)
    
    def __or__(self, other):
        return MockChain([self, other])


class MockChatPromptTemplate:
    def __init__(self, messages_template):
        self.messages_template = messages_template
    
    @classmethod
    def from_template(cls, template):
        obj = cls([("human", template)])
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
        return msgs
    
    def invoke(self, kwargs):
        return self.format_messages(**kwargs)
    
    def __or__(self, other):
        return MockChain([self, other])


class MockStrOutputParser:
    def invoke(self, message):
        return message.content if isinstance(message, AIMessage) else str(message)
    def __or__(self, other):
        return MockChain([self, other])


class MockChain:
    def __init__(self, components):
        self.components = components
    
    def invoke(self, input_data):
        result = input_data
        for component in self.components:
            result = component.invoke(result)
        return result
    
    def __or__(self, other):
        return MockChain(self.components + [other])


class MockMemory:
    def __init__(self):
        self.messages = []
    
    def add_message(self, message):
        self.messages.append(message)


ChatOpenAI = MockChatOpenAI
ChatPromptTemplate = MockChatPromptTemplate
StrOutputParser = MockStrOutputParser
llm = ChatOpenAI(model="gpt-4o-mini")


# ===========================================================
# SOLUTION 1: Basic LCEL Chain
# ===========================================================
print("=" * 50)
print("Exercise 1: Basic LCEL Chain")
print("=" * 50)

chain = (
    ChatPromptTemplate.from_template("Explain {topic} to a complete beginner in Python in 2 sentences.")
    | llm
    | StrOutputParser()
)

result = chain.invoke({"topic": "list comprehensions"})
print(result)


# ===========================================================
# SOLUTION 2: Multi-Variable Prompt Template
# ===========================================================
print("\n" + "=" * 50)
print("Exercise 2: Multi-Variable Template")
print("=" * 50)

review_chain = (
    ChatPromptTemplate.from_messages([
        ("system", "You are a {persona}."),
        ("human", "Please {action} the following: {content}")
    ])
    | llm
    | StrOutputParser()
)

result = review_chain.invoke({
    "persona": "Python code reviewer",
    "action": "review",
    "content": "for i in range(len(my_list)): print(my_list[i])"
})
print(result)


# ===========================================================
# SOLUTION 3: Conversation with Memory
# ===========================================================
print("\n" + "=" * 50)
print("Exercise 3: Conversation with Memory")
print("=" * 50)

memory = MockMemory()

def chat(memory: MockMemory, user_message: str) -> str:
    # Add user message to history
    memory.add_message(HumanMessage(content=user_message))
    
    # Build full message list for the LLM
    messages = [SystemMessage(content="You are a helpful assistant with memory.")] + memory.messages
    
    # Get response
    response = llm.invoke(messages)
    
    # Save AI response to memory
    memory.add_message(AIMessage(content=response.content))
    
    return response.content


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
# SOLUTION 4: Simple RAG Chain
# ===========================================================
KNOWLEDGE_BASE = [
    "Python was created by Guido van Rossum and first released in 1991.",
    "Python 3.12, released in 2023, includes a 5% performance improvement.",
    "The OpenAI Python SDK can be installed with: pip install openai",
    "LangChain is a framework for building applications powered by LLMs.",
    "FastAPI is a modern, fast web framework for building APIs with Python.",
]

def simple_rag(question: str, documents: list, llm) -> str:
    context = "\n".join(f"- {doc}" for doc in documents)
    
    messages = [
        SystemMessage(content=f"Answer questions using ONLY the provided context. If the answer isn't in the context, say 'I don't have that information.'\n\nContext:\n{context}"),
        HumanMessage(content=question)
    ]
    
    response = llm.invoke(messages)
    return response.content


print("=" * 50)
print("Exercise 4: Simple RAG Chain")
print("=" * 50)
for q in ["When was Python created?", "How do I install the OpenAI SDK?"]:
    print(f"Q: {q}")
    print(f"A: {simple_rag(q, KNOWLEDGE_BASE, llm)}\n")
