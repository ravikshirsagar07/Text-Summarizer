import streamlit as st
import re
from collections import Counter

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Text Summarizer",
    page_icon="📝",
    layout="centered"
)

# ==========================================
# TITLE
# ==========================================

st.title("📝 Text Summarization App")
st.write("Paste a long paragraph or article and generate a short summary.")

# ==========================================
# SUMMARIZATION FUNCTION
# ==========================================

def summarize_text(text, num_sentences=4):
    """
    Simple Extractive Text Summarization
    """

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    if len(sentences) <= num_sentences:
        return text

    words = re.findall(r'\w+', text.lower())
    word_freq = Counter(words)

    sentence_scores = {}

    for sentence in sentences:
        sentence_words = re.findall(r'\w+', sentence.lower())

        if len(sentence_words) == 0:
            continue

        score = sum(word_freq[word] for word in sentence_words)
        sentence_scores[sentence] = score

    top_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:num_sentences]

    summary = [
        sentence
        for sentence in sentences
        if sentence in top_sentences
    ]

    return " ".join(summary)

# ==========================================
# USER INPUT
# ==========================================

input_text = st.text_area(
    "Enter Text",
    height=250,
    placeholder="Paste your article here..."
)

summary_length = st.slider(
    "Number of sentences in summary",
    min_value=1,
    max_value=10,
    value=4
)

# ==========================================
# GENERATE BUTTON
# ==========================================

if st.button("Generate Summary"):

    if not input_text.strip():
        st.warning("Please enter some text.")
    else:
        summary = summarize_text(
            input_text,
            num_sentences=summary_length
        )

        st.subheader("Summary")
        st.success(summary)

        st.subheader("Statistics")
        st.write(f"Original Words: {len(input_text.split())}")
        st.write(f"Summary Words: {len(summary.split())}")

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")
st.caption("Simple Extractive Text Summarizer using Python and Streamlit")
