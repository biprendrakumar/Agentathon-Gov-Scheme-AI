import streamlit as st
from core.coordinator import CoordinatorAgent

st.title("🇮🇳 Government Scheme AI Agent")

age = st.number_input("Age", 18, 100)
income = st.number_input("Annual Income", 0)
occupation = st.selectbox("Occupation", ["student", "farmer", "worker"])
language = st.selectbox("Language", ["en", "hi"])

if st.button("Find Government Schemes"):
    user = {
        "age": age,
        "income": income,
        "occupation": occupation,
        "language": language
    }

    agent = CoordinatorAgent()
    results = agent.run(user)

    if not results:
        st.warning("No schemes found")
    else:
        for s in results:
            st.subheader(s["name"])
            st.write("**Benefit:**", s["benefit"])
            st.write("**How to Apply:**")
            for step in s["steps"]:
                st.write("•", step)
