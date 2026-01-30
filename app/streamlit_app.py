import streamlit as st
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from core.coordinator import CoordinatorAgent

# Translations dictionary
translations = {
    "en": {
        "title": "🇮🇳 Government Scheme AI Agent",
        "age": "Age",
        "income": "Annual Income",
        "occupation": "Occupation",
        "language": "Language",
        "occupations": ["student", "farmer", "worker"],
        "languages": ["en", "hi"],
        "button": "Find Government Schemes",
        "no_schemes": "No schemes found",
        "benefit": "Benefit:",
        "how_to_apply": "How to Apply:"
    },
    "hi": {
        "title": "🇮🇳 सरकारी योजना AI एजेंट",
        "age": "आयु",
        "income": "वार्षिक आय",
        "occupation": "व्यवसाय",
        "language": "भाषा",
        "occupations": ["छात्र", "किसान", "मजदूर"],
        "languages": ["English", "हिंदी"],
        "button": "सरकारी योजनाएं खोजें",
        "no_schemes": "कोई योजना नहीं मिली",
        "benefit": "लाभ:",
        "how_to_apply": "आवेदन कैसे करें:"
    }
}

# Language selection at the top
language = st.selectbox("Language / भाषा", ["en", "hi"])

# Get translations for selected language
t = translations[language]

st.title(t["title"])

age = st.number_input(t["age"], 18, 100)
income = st.number_input(t["income"], 0)
occupation = st.selectbox(t["occupation"], t["occupations"])
# Note: occupation is passed as is, but for user dict, we need to map back to English for processing
occupation_map = {"छात्र": "student", "किसान": "farmer", "मजदूर": "worker"}
user_occupation = occupation_map.get(occupation, occupation)

if st.button(t["button"]):
    user = {
        "age": age,
        "income": income,
        "occupation": user_occupation,
        "language": language
    }

    agent = CoordinatorAgent()
    results = agent.run(user)

    if not results:
        st.warning(t["no_schemes"])
    else:
        for s in results:
            st.subheader(s["name"])
            st.write(f"**{t['benefit']}**", s["benefit"])
            st.write(f"**{t['how_to_apply']}**")
            for step in s["steps"]:
                st.write("•", step)
