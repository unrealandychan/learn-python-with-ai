# Lesson 61: Solution
from abc import ABC, abstractmethod


class LLMProvider(ABC):
    @abstractmethod
    def complete(self, prompt: str) -> str:
        pass

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        pass

    def complete_with_log(self, prompt: str) -> str:
        result = self.complete(prompt)
        print(f"Tokens used: {self.count_tokens(prompt)}")
        return result


class MockOpenAI(LLMProvider):
    def complete(self, prompt: str) -> str:
        return f"[OpenAI] Response to: {prompt}"

    def count_tokens(self, text: str) -> int:
        return len(text.split())


class MockGemini(LLMProvider):
    def complete(self, prompt: str) -> str:
        return f"[Gemini] Response to: {prompt}"

    def count_tokens(self, text: str) -> int:
        return len(text) // 4


try:
    LLMProvider()
except TypeError as e:
    print(f"Cannot instantiate ABC: {e}")

openai = MockOpenAI()
gemini = MockGemini()
print(openai.complete_with_log("What is RAG?"))
print(gemini.complete_with_log("Explain embeddings"))
