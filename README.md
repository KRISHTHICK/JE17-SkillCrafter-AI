# JE17-SkillCrafter-AI
Gen Ai

🧪💡 SkillCrafter AI – Personalized Micro-Skill Builder using RAG + Agents
🧠 Project Idea:
SkillCrafter AI is a personalized micro-learning agent that helps users build small, specific skills (like "how to write better cold emails" or "basics of digital painting") in bite-sized lessons using RAG (Retrieval-Augmented Generation) and a local LLM agent (Ollama).

It pulls content from PDFs, articles, or curated docs and responds with short tutorials, tips, and even mini practice tasks.

🧩 Key Features:
Feature	Description
📥 Upload Learning Material	Upload any article/PDF to base skill generation on
🧠 Micro-Skill Agent (Ollama)	Ask anything related to skill development in natural language
📚 RAG-Powered Learning Cards	Generates flashcard-style outputs using real documents
🧪 Daily Practice Generator	Provides daily bite-sized challenges
🧭 Learning Path Recommender	Suggests what to learn next based on goals
📈 Skill Tracker (basic JSON)	Tracks skills covered and confidence level


#RUN STEPS
pip install -r requirements.txt
streamlit run app.py
Start Ollama backend
ollama serve
ollama run tinyllama
