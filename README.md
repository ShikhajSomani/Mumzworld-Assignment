# 🧠 AI Gift Finder for Mothers (RAG-Based Recommendation System)

## 🚀 Overview
This project is an AI-powered recommendation system designed to help mothers quickly find suitable baby products based on their needs.

Users can enter queries like:
- "Gift for newborn under ₹1000"
- "Stroller under ₹5000"
- "Toy for 2-year-old"

The system returns **relevant product recommendations with explanations**.

---

## 🎯 Problem
Shopping for baby products can be overwhelming due to:
- Too many choices
- Unclear age suitability
- Budget constraints
- Lack of personalized recommendations

This project solves this using **AI + Retrieval-Augmented Generation (RAG)**.

---

## 🧠 Approach

### 🔹 Step 1: Embedding
Products are converted into vector embeddings using:
- `sentence-transformers (all-MiniLM-L6-v2)`

### 🔹 Step 2: Retrieval
- FAISS is used to find similar products based on user query

### 🔹 Step 3: Filtering
Deterministic logic is applied:
- Budget filtering (e.g., "under 5000")
- Age filtering (e.g., "newborn", "2-year-old")
- Category filtering (toy, stroller, etc.)

### 🔹 Step 4: Ranking
- Premium queries → higher-priced items prioritized
- Normal queries → lower-priced items prioritized

### 🔹 Step 5: Output
- Clean structured recommendations (name, reason, age)

---

## ⚙️ Architecture

User Query  
↓  
Embedding Model  
↓  
FAISS Vector Search  
↓  
Filtering (price + age + category)  
↓  
Ranking  
↓  
Structured Output  

---

## 🧩 Features

- ✅ Semantic search using embeddings  
- ✅ Budget-aware recommendations  
- ✅ Age-based filtering  
- ✅ Category-aware ranking  
- ✅ Handles invalid queries gracefully  
- ✅ Clean UI (Streamlit)

---

## 🛠️ Tech Stack

- Python  
- FAISS  
- Sentence Transformers  
- Streamlit  

---

## 📦 Setup Instructions

### 1. Clone Repository
```bash
git clone <your-repo-link>
cd mumzworld-ai
```

##  Create Virtual Environment

```bash
py -3.10 -m venv venv
venv\Scripts\activate
```

##  Install Dependencies

```bash
pip install -r requirements.txt
```

##  Run the App

```bash
streamlit run app.py
```

## 🧪 Evaluation

### Test Cases

| Query | Result |
|------|--------|
| gift for newborn under 1000 | No products (correct – budget constraint) |
| stroller under 5000 | Only relevant low-cost items |
| toy for 2 year old | Age-appropriate toys |
| premium baby gift | Higher-priced items prioritized |
| gift for 10-year-old | Not enough relevant products |

---

### 📊 Key Observations

- Initial system over-relied on LLM → inconsistent output  
- Switched to deterministic filtering → improved reliability  

**Enhancements added:**
- Price filtering  
- Age filtering  
- Category boosting  

---

### ❗ Failure Cases

- Dataset size is small → limits diversity  
- Some queries return limited options  
- No real-world product data  

---

## ⚖️ Tradeoffs

| Decision | Reason |
|---------|--------|
| Used FAISS | Fast local retrieval |
| Limited dataset | Faster prototyping |
| Removed LLM for structure | Improved reliability |
| Rule-based filtering | Deterministic results |

---

## 💡 Improvements (Future Work)

- Larger, real-world dataset  
- Better ranking (multi-factor scoring)  
- Multilingual support (English + Arabic)  
- Personalization (user history)  
- Integration with live product APIs  

---

## 🧠 Key Insight

Initially, the system used an LLM for full decision-making.  
However, this led to inconsistent outputs.

👉 Final approach:

- Use RAG for retrieval  
- Use Python logic for constraints  
- Use AI only where necessary  

This significantly improved **accuracy and reliability**.

---

## 🎥 Demo

👉 Loom video link: https://www.loom.com/share/d21f682017114259888ccaeeec29a778

---

## 📌 Conclusion

This project demonstrates how combining:

- Retrieval (FAISS)  
- Embeddings  
- Deterministic filtering  

can create a **reliable AI-powered recommendation system**.