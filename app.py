import streamlit as st
from summarizer import generate_summary
from newspaper import Article

st.set_page_config(page_title="News Article Summarizer")

st.title("📰 AI News Article Summarizer")

st.write("Summarize long news articles automatically using NLP.")

option = st.radio(
    "Choose Input Type",
    ["Paste Article Text", "Enter News URL"]
)

article_text = ""

if option == "Paste Article Text":

    article_text = st.text_area(
        "Paste your news article here",
        height=250
    )

if option == "Enter News URL":

    url = st.text_input("Enter News Article URL")

    if st.button("Fetch Article"):

        try:

            article = Article(url)
            article.download()
            article.parse()

            article_text = article.text

            st.subheader("Original Article")

            st.write(article_text)

        except:
            st.error("Failed to fetch article")

summary_length = st.slider(
    "Select number of sentences for summary",
    1,
    10,
    3
)

if st.button("Generate Summary"):

    if article_text != "":

        with st.spinner("Generating summary..."):

            summary = generate_summary(article_text, summary_length)

        st.subheader("Summary")

        st.success(summary)

    else:
        st.warning("Please enter article text first.")