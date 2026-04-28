import streamlit as st
from rag_pipeline import run_pipeline

st.title("🧠 AI Gift Finder for Mothers")

query = st.text_input("Enter your requirement")

if st.button("Search") and query:
    result = run_pipeline(query)

    if result.get("recommendations"):
        st.success("Here are some recommendations for you 👇")

        for item in result["recommendations"]:
            st.markdown(f"### 🛍️ {item['name']}")
            st.write(f"👶 Age: {item['age']}")
            st.write(f"💡 {item['reason']}")
            st.divider()
    else:
        st.warning("⚠️ No relevant products found.")