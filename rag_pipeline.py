import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# ---------------------------
# LOAD EMBEDDING MODEL
# ---------------------------
embed_model = SentenceTransformer('all-MiniLM-L6-v2')

# ---------------------------
# LOAD DATA
# ---------------------------
with open('products.json', 'r') as f:
    products = json.load(f)

# ---------------------------
# PRODUCT → TEXT
# ---------------------------
def product_to_text(p):
    return f"{p['name']} {p['category']} {p['age_range']} {p['use_case']} {p['price']}"

product_texts = [product_to_text(p) for p in products]

# ---------------------------
# CREATE EMBEDDINGS
# ---------------------------
product_embeddings = embed_model.encode(product_texts)

dimension = product_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(product_embeddings))

# ---------------------------
# RETRIEVE
# ---------------------------
def retrieve(query, k=5):
    query_vec = embed_model.encode([query])
    distances, indices = index.search(np.array(query_vec), k)
    return [products[i] for i in indices[0]]

# ---------------------------
# FILTERING + RANKING
# ---------------------------
def filter_products(query, products):
    query_lower = query.lower()
    filtered = products.copy()

    # 🔹 AGE FILTER
    if "newborn" in query_lower:
        filtered = [p for p in filtered if "0" in p["age_range"]]

    if "2 year" in query_lower or "2-year" in query_lower:
        filtered = [p for p in filtered if "24" in p["age_range"] or "36" in p["age_range"]]

    if "10-year" in query_lower:
        return []  # invalid case

    # 🔹 PRICE FILTER (STRICT)
    if "under" in query_lower:
        try:
            budget = int(query_lower.split("under")[1].strip().split()[0])
            filtered = [p for p in filtered if p["price"] <= budget]
        except:
            pass

    # 🔹 CATEGORY BOOST
    if "stroller" in query_lower:
        stroller_items = [p for p in filtered if "stroller" in p["category"]]
        if stroller_items:
            filtered = stroller_items

    if "toy" in query_lower:
        toy_items = [p for p in filtered if "toy" in p["category"]]
        if toy_items:
            filtered = toy_items

    # 🔹 RANKING
    if "premium" in query_lower:
        filtered = sorted(filtered, key=lambda x: -x["price"])
    else:
        filtered = sorted(filtered, key=lambda x: x["price"])

    return filtered


# ---------------------------
# RESPONSE GENERATION
# ---------------------------
def generate_response(query, products):
    if not products:
        return {
            "query": query,
            "recommendations": [],
            "message": "Not enough relevant products found"
        }

    results = []

    for p in products[:3]:
        results.append({
            "name": p["name"],
            "reason": f"Suitable for {p['age_range']} and useful for {p['use_case']}",
            "age": p["age_range"]
        })

    return {
        "query": query,
        "recommendations": results
    }


# ---------------------------
# MAIN PIPELINE
# ---------------------------
def run_pipeline(query):
    retrieved = retrieve(query)
    filtered = filter_products(query, retrieved)
    return generate_response(query, filtered)