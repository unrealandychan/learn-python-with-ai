# Lesson 65: Exercise — Dataclasses
from dataclasses import dataclass, field
from datetime import datetime

# TODO: @dataclass(frozen=True) class Role
#   Attribute: value (str)
#   After class definition, add: Role.SYSTEM = Role("system") etc.

# TODO: @dataclass class Message
#   role: Role
#   content: str
#   timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

# TODO: @dataclass class ConversationWindow
#   max_tokens: int = 512
#   messages: list = field(default_factory=list)
#   _token_count: int = field(init=False, default=0)
#
#   def add(self, msg: Message) -> None

# Test
# win = ConversationWindow(max_tokens=20)
# win.add(Message(Role.SYSTEM, "You are a helpful assistant."))
# win.add(Message(Role.USER, "What is machine learning?"))
# for m in win.messages:
#     print(f"[{m.role.value}] {m.content}")
