import streamlit as st
import re
from collections import Counter

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝"
)

st.title("📝 Text Summarization App")

st.write(
    "Paste a long paragraph and get a summary in 3-4 lines."
)

# =====================================================
# SUMMARIZATION FUNCTION
# =====================================================

def summarize_text(text, num_sentences=4):

    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    if len(sentences) <= num_sentences:
        return text

    # Remove punctuation and lowercase
    words = re.findall(r'\w+', text.lower())

    # Word frequencies
    word_freq = Counter(words)

    # Score each sentence
    sentence_scores = {}

    for sentence in sentences:

        sentence_words = re.findall(r'\w+', sentence.lower())

        score = 0

        for word in sentence_words:
            score += word_freq[word]

        sentence_scores[sentence] = score

    # Select top sentences
    top_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:num_sentences]

    # Preserve original order
    summary = []

    for sentence in sentences:
        if sentence in top_sentences:
            summary.append(sentence)

    return " ".join(summary)

# =====================================================
# USER INPUT
# =====================================================

input_text = st.text_area(
    "Enter Text",
    height=250,
    placeholder="Paste your article here..."
)

# =====================================================
# BUTTON
# =====================================================

if st.button("Generate Summary"):

    if not input_text.strip():

        st.warning("Please enter some text.")

    else:

        summary = summarize_text(
            input_text,
            num_sentences=4
        )

        st.subheader("Summary")

        st.success(summary)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")
st.write("Simple Extractive Text Summarizer")python -m streamlit run app.py