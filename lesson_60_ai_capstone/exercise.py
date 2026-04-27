"""
Lesson 60: Capstone Project — AI Chatbot with Memory
Complete, runnable implementation using a mock LLM.

This is Project B from the instructions — a fully-featured CLI chatbot.

Features:
- Multi-turn conversation with memory
- Configurable persona via system prompt
- Save/load conversation history to JSON
- Commands: /help, /clear, /save, /load, /persona, /quit
- Graceful error handling throughout

To use with real OpenAI API:
  1. pip install openai python-dotenv
  2. Create .env with OPENAI_API_KEY=sk-...
  3. Replace MockOpenAI with real OpenAI client (see comment below)
"""

import json
import os
from datetime import datetime
from pathlib import Path


# ============================================================
# MOCK OPENAI CLIENT
# Replace with:
#   from openai import OpenAI
#   from dotenv import load_dotenv
#   load_dotenv()
#   client = OpenAI()
# ============================================================

class MockOpenAI:
    """Simulates OpenAI chat completions."""
    
    class _Completions:
        def create(self, model, messages, **kwargs):
            # Build context from message history
            history_text = " ".join(m["content"] for m in messages[-5:])
            last_user = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
            system = next((m["content"] for m in messages if m["role"] == "system"), "")
            
            last_lower = last_user.lower()
            
            if "hello" in last_lower or "hi " in last_lower:
                content = "Hello! I'm your AI assistant. How can I help you today?"
            elif "python" in last_lower and "function" in last_lower:
                content = "Here's a Python function example:\n\n```python\ndef greet(name: str) -> str:\n    \"\"\"Return a greeting.\"\"\"\n    return f'Hello, {name}!'\n\nprint(greet('World'))  # Hello, World!\n```"
            elif "explain" in last_lower or "what is" in last_lower:
                content = "Great question! This concept is fundamental to modern programming. Let me break it down step by step with a practical example relevant to AI development..."
            elif "help" in last_lower:
                content = "I can help you with Python programming, AI concepts, data science, and more. What would you like to learn?"
            elif "thanks" in last_lower or "thank you" in last_lower:
                content = "You're welcome! Feel free to ask anything else."
            elif "joke" in last_lower:
                content = "Why do Python developers prefer dark mode? Because light attracts bugs! 🐛"
            else:
                content = f"That's an interesting question about '{last_user[:40]}'. As an AI assistant, I can help you explore this topic. What specific aspect would you like to dive into?"
            
            class Msg:
                pass
            msg = Msg()
            msg.content = content
            
            class Ch:
                pass
            ch = Ch()
            ch.message = msg
            
            class Resp:
                pass
            resp = Resp()
            resp.choices = [ch]
            return resp
    
    def __init__(self, api_key=None):
        self.chat = type('obj', (object,), {'completions': self._Completions()})()


# ============================================================
# CHATBOT IMPLEMENTATION
# ============================================================

DEFAULT_PERSONA = """You are a helpful, knowledgeable AI assistant specializing in Python programming and AI development.
You give clear, accurate, and concise answers.
When showing code, always use proper formatting with code blocks.
You're friendly but professional."""

HISTORY_DIR = Path("chat_histories")


class Conversation:
    """Manages a single conversation with history and persistence."""
    
    def __init__(self, persona: str = DEFAULT_PERSONA):
        self.persona = persona
        self.messages = []
        self.created_at = datetime.now().isoformat()
        self.name = None
    
    def add_message(self, role: str, content: str):
        """Add a message to the conversation history."""
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat()
        })
    
    def get_api_messages(self) -> list:
        """Get messages in the format expected by the OpenAI API."""
        api_msgs = [{"role": "system", "content": self.persona}]
        for msg in self.messages:
            api_msgs.append({"role": msg["role"], "content": msg["content"]})
        return api_msgs
    
    def clear(self):
        """Clear conversation history (keep persona)."""
        self.messages = []
        print("💬 Conversation cleared.")
    
    def save(self, filename: str = None) -> str:
        """Save conversation to a JSON file."""
        HISTORY_DIR.mkdir(exist_ok=True)
        if filename is None:
            filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        filepath = HISTORY_DIR / filename
        data = {
            "name": self.name or filename,
            "persona": self.persona,
            "created_at": self.created_at,
            "messages": self.messages
        }
        
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        
        return str(filepath)
    
    @classmethod
    def load(cls, filepath: str) -> "Conversation":
        """Load a conversation from a JSON file."""
        with open(filepath) as f:
            data = json.load(f)
        
        conv = cls(persona=data.get("persona", DEFAULT_PERSONA))
        conv.messages = data.get("messages", [])
        conv.created_at = data.get("created_at", datetime.now().isoformat())
        conv.name = data.get("name")
        return conv
    
    def __len__(self):
        return len(self.messages)
    
    def __repr__(self):
        return f"Conversation({len(self.messages)} messages)"


class Chatbot:
    """AI chatbot with persistent memory and commands."""
    
    def __init__(self, model: str = "gpt-4o-mini"):
        self.model = model
        self.client = MockOpenAI()
        self.conversation = Conversation()
        self.running = True
    
    def _get_response(self, user_message: str) -> str:
        """Get a response from the AI."""
        self.conversation.add_message("user", user_message)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.conversation.get_api_messages()
            )
            reply = response.choices[0].message.content
            self.conversation.add_message("assistant", reply)
            return reply
        
        except Exception as e:
            error_msg = f"Error getting response: {e}"
            print(f"❌ {error_msg}")
            # Remove the user message we added since we got no response
            self.conversation.messages.pop()
            return None
    
    def _handle_command(self, command: str) -> bool:
        """
        Handle a slash command.
        Returns True if command was handled, False if it's a normal message.
        """
        parts = command.strip().split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""
        
        if cmd == "/help":
            print("""
📚 Available Commands:
  /help          — Show this help message
  /clear         — Clear conversation history
  /save [name]   — Save conversation to file
  /load <file>   — Load conversation from file
  /persona <text>— Change the AI's persona/system prompt
  /history       — Show conversation history
  /stats         — Show conversation statistics
  /quit or /exit — Exit the chatbot
            """)
            return True
        
        elif cmd == "/clear":
            self.conversation.clear()
            return True
        
        elif cmd == "/save":
            filename = args if args else None
            try:
                filepath = self.conversation.save(filename)
                print(f"✅ Conversation saved to: {filepath}")
            except Exception as e:
                print(f"❌ Failed to save: {e}")
            return True
        
        elif cmd == "/load":
            if not args:
                print("❌ Usage: /load <filename>")
                # Show available files
                if HISTORY_DIR.exists():
                    files = list(HISTORY_DIR.glob("*.json"))
                    if files:
                        print("Available saves:")
                        for f in files:
                            print(f"  {f.name}")
                return True
            
            filepath = HISTORY_DIR / args
            if not filepath.exists():
                filepath = Path(args)  # try absolute path
            
            try:
                self.conversation = Conversation.load(str(filepath))
                print(f"✅ Loaded conversation with {len(self.conversation)} messages.")
            except FileNotFoundError:
                print(f"❌ File not found: {args}")
            except json.JSONDecodeError:
                print(f"❌ Invalid JSON file: {args}")
            return True
        
        elif cmd == "/persona":
            if not args:
                print(f"Current persona:\n{self.conversation.persona}")
            else:
                self.conversation.persona = args
                print(f"✅ Persona updated.")
            return True
        
        elif cmd == "/history":
            if not self.conversation.messages:
                print("No messages yet.")
            else:
                print(f"\n--- Conversation History ({len(self.conversation)} messages) ---")
                for msg in self.conversation.messages:
                    role = "👤 You" if msg["role"] == "user" else "🤖 AI"
                    timestamp = msg.get("timestamp", "")[:19]
                    print(f"\n[{timestamp}] {role}:")
                    print(f"  {msg['content'][:200]}{'...' if len(msg['content']) > 200 else ''}")
            return True
        
        elif cmd == "/stats":
            msgs = self.conversation.messages
            user_msgs = [m for m in msgs if m["role"] == "user"]
            ai_msgs = [m for m in msgs if m["role"] == "assistant"]
            total_chars = sum(len(m["content"]) for m in msgs)
            print(f"""
📊 Conversation Statistics:
  Total messages: {len(msgs)}
  Your messages: {len(user_msgs)}
  AI messages: {len(ai_msgs)}
  Total characters: {total_chars:,}
  Session started: {self.conversation.created_at[:19]}
            """)
            return True
        
        elif cmd in ("/quit", "/exit", "/q"):
            print("\n👋 Goodbye! Your conversation can be saved with /save before quitting.")
            self.running = False
            return True
        
        return False
    
    def run(self):
        """Run the chatbot interactive loop."""
        print("=" * 60)
        print("🤖 AI Chatbot with Memory")
        print("=" * 60)
        print(f"Model: {self.model} (mock mode — swap for real OpenAI)")
        print("Type /help for commands, /quit to exit.\n")
        
        while self.running:
            try:
                user_input = input("You: ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\nInterrupted. Use /quit to exit gracefully.")
                break
            
            if not user_input:
                continue
            
            # Check if it's a command
            if user_input.startswith("/"):
                self._handle_command(user_input)
                continue
            
            # Get AI response
            print("\n🤖 AI: ", end="", flush=True)
            response = self._get_response(user_input)
            if response:
                print(response)
            print()


# ============================================================
# DEMO MODE — runs automatically in non-interactive environments
# ============================================================

def run_demo():
    """Run a scripted demo of the chatbot."""
    print("=" * 60)
    print("🤖 AI Chatbot with Memory — DEMO MODE")
    print("=" * 60)
    
    bot = Chatbot()
    
    # Simulate a conversation
    demo_inputs = [
        "Hello! I'm learning Python.",
        "Can you show me a Python function example?",
        "That's great! What about AI with Python?",
        "/stats",
        "/save demo_conversation.json",
        "Thanks for your help!",
    ]
    
    for user_input in demo_inputs:
        print(f"\nYou: {user_input}")
        
        if user_input.startswith("/"):
            bot._handle_command(user_input)
        else:
            response = bot._get_response(user_input)
            if response:
                print(f"🤖 AI: {response}")
    
    print("\n" + "=" * 60)
    print("Demo complete!")
    print(f"Conversation has {len(bot.conversation)} messages.")
    print("In interactive mode, type /quit to exit.")
    print("=" * 60)


if __name__ == "__main__":
    import sys
    
    # Run demo if not interactive (e.g., running from terminal without TTY)
    if not sys.stdin.isatty():
        run_demo()
    else:
        # Interactive mode
        bot = Chatbot()
        bot.run()
