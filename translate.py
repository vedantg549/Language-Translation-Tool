pip install googletrans==4.0.0-rc1        
pip install streamlit
import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the Translator
translator = Translator()

# Title of the app
st.title("Language Translation App")

# Display available languages
st.sidebar.header("Select Target Language")
language_options = list(LANGUAGES.values())
language_codes = list(LANGUAGES.keys())
selected_language = st.sidebar.selectbox("Choose a language", language_options)

# Get the corresponding language code
target_language_code = language_codes[language_options.index(selected_language)]

# User input for text to translate
text_to_translate = st.text_area("Enter text to translate:")

# Button to perform translation
if st.button("Translate"):
    if text_to_translate:
        translated_text = translator.translate(text_to_translate, dest=target_language_code)
        st.success(f"Translated text: {translated_text.text}")
    else:
        st.error("Please enter text to translate.")
