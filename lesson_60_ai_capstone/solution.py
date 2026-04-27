"""
Lesson 60: Capstone — Solution

The exercise.py IS the solution for Project B (AI Chatbot with Memory).
This file contains Project A: AI Document Analyzer as an additional complete example.
"""

import json
import re
from datetime import datetime


# ============================================================
# MOCK CLIENT (replace with real OpenAI for production)
# ============================================================
class MockOpenAI:
    class _Completions:
        def create(self, model, messages, **kwargs):
            user_msg = next((m["content"] for m in reversed(messages) if m["role"] == "user"), "")
            system = next((m["content"] for m in messages if m["role"] == "system"), "")
            
            if "summary" in system.lower() or "summarize" in user_msg.lower():
                content = "This document discusses Python programming and AI development, covering key concepts including language fundamentals, data structures, and modern AI libraries."
            elif "topic" in system.lower() or "extract" in user_msg.lower():
                content = '["Python Programming", "AI Development", "Machine Learning", "Data Science", "API Integration"]'
            elif "sentiment" in system.lower():
                content = '{"sentiment": "POSITIVE", "confidence": 0.92, "reason": "The document uses encouraging language and highlights opportunities."}'
            elif "insight" in system.lower():
                content = "1. Python's simplicity makes it ideal for rapid AI prototyping.\n2. The AI ecosystem is maturing rapidly with standardized libraries.\n3. Developers should prioritize learning async patterns for LLM applications."
            else:
                content = "[AI response based on document context]"
            
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
# PROJECT A: AI DOCUMENT ANALYZER
# ============================================================

class DocumentAnalyzer:
    """Analyzes text documents using an LLM."""
    
    def __init__(self, model: str = "gpt-4o-mini"):
        self.client = MockOpenAI()
        self.model = model
    
    def _call_llm(self, system: str, user: str) -> str:
        """Make a single LLM call."""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {e}"
    
    def summarize(self, text: str, max_sentences: int = 3) -> str:
        """Generate a concise summary of the text."""
        return self._call_llm(
            system=f"Summarize the following text in {max_sentences} sentences. Be concise and capture the key points.",
            user=text[:3000]  # Limit to avoid token limits
        )
    
    def extract_topics(self, text: str, max_topics: int = 5) -> list:
        """Extract the main topics from the text."""
        result = self._call_llm(
            system=f"Extract the top {max_topics} main topics from this text. Return as a JSON array of strings only.",
            user=text[:3000]
        )
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            # Fallback: extract quoted strings
            return re.findall(r'"([^"]+)"', result)[:max_topics]
    
    def analyze_sentiment(self, text: str) -> dict:
        """Analyze the overall sentiment of the text."""
        result = self._call_llm(
            system='Analyze sentiment. Return JSON: {"sentiment": "POSITIVE/NEGATIVE/NEUTRAL", "confidence": 0.0-1.0, "reason": "one sentence"}',
            user=text[:2000]
        )
        try:
            return json.loads(result)
        except json.JSONDecodeError:
            return {"sentiment": "NEUTRAL", "confidence": 0.5, "reason": "Could not parse"}
    
    def generate_insights(self, text: str) -> list:
        """Generate actionable insights from the text."""
        result = self._call_llm(
            system="Generate 3 key actionable insights from this document. Number each insight (1. 2. 3.).",
            user=text[:3000]
        )
        # Parse numbered list
        insights = []
        for line in result.split("\n"):
            line = line.strip()
            if line and line[0].isdigit() and "." in line:
                insights.append(line.split(".", 1)[1].strip())
        return insights[:3] if insights else [result]
    
    def analyze(self, text: str) -> dict:
        """Run full analysis pipeline on a document."""
        print("📄 Analyzing document...")
        
        print("  ▸ Generating summary...")
        summary = self.summarize(text)
        
        print("  ▸ Extracting topics...")
        topics = self.extract_topics(text)
        
        print("  ▸ Analyzing sentiment...")
        sentiment = self.analyze_sentiment(text)
        
        print("  ▸ Generating insights...")
        insights = self.generate_insights(text)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "word_count": len(text.split()),
            "char_count": len(text),
            "summary": summary,
            "topics": topics,
            "sentiment": sentiment,
            "insights": insights
        }
    
    def print_report(self, analysis: dict):
        """Print a formatted analysis report."""
        print("\n" + "=" * 60)
        print("📊 DOCUMENT ANALYSIS REPORT")
        print("=" * 60)
        print(f"Analyzed: {analysis['timestamp'][:19]}")
        print(f"Document size: {analysis['word_count']} words, {analysis['char_count']} characters\n")
        
        print("📝 SUMMARY")
        print("-" * 40)
        print(analysis["summary"])
        
        print("\n🏷️  MAIN TOPICS")
        print("-" * 40)
        for i, topic in enumerate(analysis["topics"], 1):
            print(f"  {i}. {topic}")
        
        print("\n😊 SENTIMENT")
        print("-" * 40)
        s = analysis["sentiment"]
        sentiment_emoji = {"POSITIVE": "😊", "NEGATIVE": "😔", "NEUTRAL": "😐"}.get(s.get("sentiment", ""), "")
        print(f"  {sentiment_emoji} {s.get('sentiment', 'Unknown')} "
              f"(confidence: {s.get('confidence', 0):.0%})")
        print(f"  Reason: {s.get('reason', 'N/A')}")
        
        print("\n💡 KEY INSIGHTS")
        print("-" * 40)
        for i, insight in enumerate(analysis["insights"], 1):
            print(f"  {i}. {insight}")
        
        print("\n" + "=" * 60)
    
    def save_report(self, analysis: dict, filename: str = None) -> str:
        """Save the analysis report to a JSON file."""
        if filename is None:
            filename = f"analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, "w") as f:
            json.dump(analysis, f, indent=2)
        return filename


# ============================================================
# DEMO
# ============================================================

SAMPLE_DOCUMENT = """
Python has emerged as the dominant programming language for artificial intelligence 
and machine learning. Its clean syntax, extensive library ecosystem, and strong 
community support make it the ideal choice for both beginners and experts in the field.

The rise of large language models (LLMs) like GPT-4 has created an entirely new 
category of AI applications. Developers can now build sophisticated chatbots, document 
analyzers, code assistants, and autonomous agents using just a few hundred lines of Python.

Key libraries driving this revolution include: OpenAI's Python SDK for LLM access, 
LangChain for building AI pipelines, Pandas and NumPy for data processing, FastAPI 
for serving AI models as APIs, and vector databases like Chroma for semantic search.

The opportunity for Python developers has never been greater. Companies across every 
industry are investing heavily in AI capabilities, creating strong demand for developers 
who understand both Python fundamentals and modern AI tooling. This course has equipped 
you with exactly these skills.

The next steps are to build real projects, contribute to open-source AI tools, and 
continue learning as the field evolves rapidly. The foundation you've built here will 
serve you well as you tackle increasingly complex AI engineering challenges.
"""

if __name__ == "__main__":
    analyzer = DocumentAnalyzer()
    analysis = analyzer.analyze(SAMPLE_DOCUMENT)
    analyzer.print_report(analysis)
    
    # Save report
    filename = analyzer.save_report(analysis, "sample_analysis.json")
    print(f"\n✅ Report saved to: {filename}")
