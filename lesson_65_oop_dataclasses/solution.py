# Lesson 65: Solution
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(frozen=True)
class Role:
    value: str

Role.SYSTEM = Role("system")
Role.USER = Role("user")
Role.ASSISTANT = Role("assistant")


@dataclass
class Message:
    role: Role
    content: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class ConversationWindow:
    max_tokens: int = 512
    messages: list = field(default_factory=list)
    _token_count: int = field(init=False, default=0)

    def _count(self, msg: Message) -> int:
        return len(msg.content.split())

    def add(self, msg: Message) -> None:
        self.messages.append(msg)
        self._token_count += self._count(msg)
        i = 0
        while self._token_count > self.max_tokens and i < len(self.messages):
            if self.messages[i].role != Role.SYSTEM:
                self._token_count -= self._count(self.messages[i])
                self.messages.pop(i)
            else:
                i += 1

    @property
    def token_usage(self) -> dict:
        return {"used": self._token_count, "max": self.max_tokens}


win = ConversationWindow(max_tokens=20)
win.add(Message(Role.SYSTEM, "You are a helpful assistant."))
win.add(Message(Role.USER, "What is machine learning?"))
win.add(Message(Role.ASSISTANT, "ML is a subset of artificial intelligence."))
for m in win.messages:
    print(f"[{m.role.value}] {m.content[:50]}")
print(win.token_usage)
