from rag_pipeline import run_pipeline

test_cases = [
    "gift for newborn under 1000",
    "stroller under 5000",
    "toy for 2 year old",
    "premium baby gift",
    "gift for 10-year-old"
]

for q in test_cases:
    print("\n==============================")
    print("Query:", q)
    print(run_pipeline(q))