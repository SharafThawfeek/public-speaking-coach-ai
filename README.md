# 🎤 Public Speaking Coach AI

An AI-powered web application that helps users improve their public speaking skills by analyzing speeches, detecting filler words, measuring clarity, and providing actionable feedback.
Built as part of IT 3041 **IT 3041 – Information Retrieval and Web Analytics**.

---

## 📌 Project Overview
This project demonstrates a **multi-agent AI system** integrating:
- **Speech Analysis Agent (NLP):** Speech summarization & key point extraction.
- **Feedback Agent (LLM):** Personalized speech feedback.
- **Information Retrieval Module:** Relevant tips/examples from a knowledge base.
- **Critique & Explainability Module:** Ensures fairness, transparency, and Responsible AI.
- **Security Layer:** Authentication, input sanitization, encryption.

---

## 📂 Repository Structure

```bash
public-speaking-coach-ai/
├── src/              # Source code for AI agents and orchestrator logic
│   ├── server.py     # Flask API server (speech analysis endpoint)
│   ├── utils.py      # Core NLP speech analysis functions
├── Client/           # Frontend client (coach.html and assets)
├── docs/             # Documentation, design diagrams, and technical reports
├── requirements.txt  # Python dependencies for the project
└── README.md         # Project overview and setup instructions

```
---

<h2>👥 Contributors</h2>
<ul>
  <li><strong><a href="https://github.com/SharafThawfeek">Sharaf Thawfeek</a></strong> (Leader) – System design, Flask backend, orchestration</li>
  <li><strong><a href="https://github.com/Ushna001">Ushna Uwais</a></strong> – NLP pipeline, speech analysis, evaluation</li>
  <li><strong><a href="https://github.com/Anas8410">Anas Ahamed</a></strong> – Information retrieval module, security, research</li>
</ul>

---

## ⚙️ Setup
```bash
git clone https://github.com/SharafThawfeek/public-speaking-coach-ai.git
cd public-speaking-coach-ai
pip install -r requirements.txt

