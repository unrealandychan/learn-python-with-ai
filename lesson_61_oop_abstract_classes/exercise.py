# Lesson 61: Exercise — Abstract Classes

# TODO: Import ABC and abstractmethod from abc

# TODO: Define LLMProvider(ABC) with:
#   @abstractmethod complete(self, prompt: str) -> str
#   @abstractmethod count_tokens(self, text: str) -> int
#   complete_with_log(self, prompt: str) -> str — calls complete(), prints token count

# TODO: MockOpenAI(LLMProvider)
#   complete: returns f"[OpenAI] {prompt}"
#   count_tokens: returns len(text.split())

# TODO: MockGemini(LLMProvider)
#   complete: returns f"[Gemini] {prompt}"
#   count_tokens: returns len(text) // 4

# Verify TypeError when instantiating abstract class directly
# try:
#     LLMProvider()
# except TypeError as e:
#     print(e)

# openai = MockOpenAI()
# print(openai.complete_with_log("What is RAG?"))
