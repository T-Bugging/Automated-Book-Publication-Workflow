# 📖 **Automated Book Publication Workflow**

A modular AI-powered system for automatically scraping, rewriting, reviewing, and searching book chapters, with full support for human-in-the-loop control, semantic memory, and reinforcement learning-based retrieval.

---

## 🔍 **What It Does**

Automates the transformation of book chapters using AI agents and a clean content pipeline. It supports:

-  Web scraping from literary sources (e.g., Wikisource)
-  Full-page screenshot capture
-  AI-generated rewrites with multiple styles
-  Professional editing through AI review agents
-  Human input between every stage
-  Versioned storage of raw, spun, and reviewed content
-  Smart story retrieval using ChromaDB + RL-based ranking

---

## **Agents Overview**

###  AI Writer Agent
Generates rewritten versions of the original chapter in various styles:
- Summary  
- Simplified  
- Poetic  
- Creative Rewrite  
- Custom Prompt  

Supports human input by letting the user choose or write their own prompt before generating.

---

###  AI Reviewer Agent
Refines and polishes the AI Writer’s output for:
- Clarity  
- Grammar  
- Flow  
- Tone consistency  

Also allows the user to choose between a default editing instruction or supply their own — enabling human-in-the-loop control.

---

##  **Current Folder Structure**

```bash
output/
├── Raw_text/          # Scraped original text
├── Spun_text/         # AI Writer outputs
├── Reviewed_text/     # Finalized reviewed content
├── screenshots/       # Full-page browser screenshots
```

Each output is versioned (`text_1.txt`, `spunText_1.txt`, etc.) to avoid overwriting previous runs.

---

## ⚙️ **Core Tools & Technologies**

| Component             | Description                                       |
|------------------------|---------------------------------------------------|
| `Playwright`           | Browser automation for scraping + screenshots     |
| `Gemini API`           | Powers both the Writer and Reviewer agents        |
| `ChromaDB`             | Persistent vector DB for semantic search and storage |
| `dotenv`               | Manages API keys securely                         |
| `Python`               | Core development language                         |

---

##  **Semantic Search & RL Feedback System**

The system uses **ChromaDB** to store all reviewed content in a searchable vector format. Each story is saved with semantic embeddings and metadata (e.g., type, title).

This enables:
-  Natural language story search (e.g., “a sailor trapped in ice”)
-  Filtering by type (e.g., only “reviewed” versions)
   Re-ranking based on human preferences

---

###  **How the Feedback Loop Works**

A lightweight RL-inspired algorithm is used to learn from user choices. When a user views story search results and selects the most relevant one, that feedback improves future rankings.

#### ⚙️ Algorithm Overview

```python
# Sample structure of feedback_scores.json
{
  "doc_id_abc": 3,
  "doc_id_xyz": 1
}

# 1. Search ChromaDB
results = collection.query(query_texts=["ancient prophecy"], n_results=3)

# 2. Re-rank using stored feedback
combined = zip(results["ids"], results["documents"], results["metadatas"])
ranked = sorted(combined, key=lambda x: feedback_scores.get(x[0], 0), reverse=True)

# 3. User selects preferred result
feedback_scores[selected_doc_id] += 1

# 4. Save feedback to disk
json.dump(feedback_scores, open("feedback_scores.json", "w"))
```

Over time, this loop ensures better, personalized search results without retraining any models.

---

##  **Human-in-the-Loop Support**

-  Customizable prompt selection for AI Writer and Reviewer  
-  Optional retry of review stage with new instructions  
-  Final confirmation step before saving reviewed output  
-  User-driven feedback on search results (used for RL ranking)

---

##  **How to Run**

1. Clone the repository  
2. Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```bash
   pip install playwright chromadb python-dotenv google-generativeai
   playwright install
   ```
4. Run the system:
   ```bash
   python main.py
   ```

---

## 📜 **License**

This repository is for educational, learning, and evaluation purposes only.
