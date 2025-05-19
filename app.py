import streamlit as st
import requests

st.title("🈯 Local Translator (LangChain + Ollama)")

text = st.text_area("Enter text to translate")
target_lang = st.text_input("Translate to (e.g., English, French)")

if st.button("Translate"):
    if not text or not target_lang:
        st.warning("Please enter both text and a target language.")
    else:
        #  "http://localhost:11434/api/generate"
        response = requests.post(
            "http://localhost:8000/translate/invoke",
            json={"input": {"text": text, "target_lang": target_lang}}
        )
        if response.status_code == 200:
            data = response.json()
            st.success(f"Detected Language: {data['output']['detected_language']}")
            st.markdown(f"**Translation:** {data['output']['translation']}")
        else:
            st.error("API error: " + response.text)
