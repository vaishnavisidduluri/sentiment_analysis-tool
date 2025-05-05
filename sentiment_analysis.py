import streamlit as st
from textblob import TextBlob


st.set_page_config(
    page_title="Sentiment Analysis Tool",
    page_icon="📝",
    layout="centered",
    initial_sidebar_state="auto",
)

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        color: #333333;
        margin: 0;
        padding: 0;
    }
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        color: #d35400;
        text-align: center;
        margin-top: 2rem;
        margin-bottom: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 1px 1px 2px #f39c12;
    }
    .card {
        background: #ffffff;
        max-width: 700px;
        margin: 0 auto 3rem auto;
        padding: 2rem 3rem;
        border-radius: 25px;
        box-shadow: 0 8px 24px rgba(243, 156, 18, 0.3);
        transition: box-shadow 0.3s ease;
        border: 2px solid #f39c12;
    }
    .card:hover {
        box-shadow: 0 12px 36px rgba(243, 156, 18, 0.5);
        border-color: #e67e22;
    }
    .input-box {
        font-size: 1.2rem;
        padding: 15px;
        width: 100%;
        border-radius: 15px;
        border: 3px solid #f39c12;
        resize: none;
        box-sizing: border-box;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .input-box:focus {
        border-color: #e67e22;
        outline: none;
        box-shadow: 0 0 12px #e67e22;
    }
    .analyze-button {
        background: linear-gradient(45deg, #f39c12, #f1c40f);
        color: white;
        font-weight: 700;
        padding: 1rem 2.5rem;
        border: none;
        border-radius: 15px;
        cursor: pointer;
        font-size: 1.3rem;
        transition: background 0.4s ease, transform 0.3s ease, box-shadow 0.3s ease;
        margin-top: 1.5rem;
        width: 100%;
        box-shadow: 0 6px 20px rgba(243, 156, 18, 0.7);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .analyze-button:hover {
        background: linear-gradient(45deg, #f1c40f, #f39c12);
        transform: scale(1.1);
        box-shadow: 0 8px 28px rgba(241, 196, 15, 0.9);
    }
    .result-box {
        margin-top: 2rem;
        font-size: 1.5rem;
        font-weight: 700;
        padding: 1.8rem 2.5rem;
        border-radius: 25px;
        text-align: center;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        box-shadow: 0 8px 28px rgba(243, 156, 18, 0.15);
        transition: background-color 0.4s ease, color 0.4s ease;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .positive {
        background: linear-gradient(135deg, #a8e063, #56ab2f);
        color: #1b3a1a;
        border: 3px solid #1b3a1a;
        box-shadow: 0 0 15px #56ab2f;
    }
    .negative {
        background: linear-gradient(135deg, #f85032, #e73827);
        color: #4a0a0a;
        border: 3px solid #4a0a0a;
        box-shadow: 0 0 15px #e73827;
    }
    .neutral {
        background: linear-gradient(135deg, #bdc3c7, #2c3e50);
        color: #1c1c1c;
        border: 3px solid #1c1c1c;
        box-shadow: 0 0 15px #2c3e50;
    }
    footer {
        margin-top: 5rem;
        text-align: center;
        color: #d35400;
        font-size: 1.1rem;
        font-weight: 600;
        padding-bottom: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-shadow: 1px 1px 3px #f39c12;
    }
    /* Sidebar styling */
    .css-1d391kg {
        background: #f39c12 !important;
        color: white !important;
    }
    .css-1d391kg .css-1v3fvcr {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown('<h1 class="main-header">Sentiment Analysis Tool</h1>', unsafe_allow_html=True)

# Card container for input and button
st.markdown('<div class="card">', unsafe_allow_html=True)

# Text input box (textarea)
user_input = st.text_area("Enter your text here:", height=160, max_chars=1000, key="input", placeholder="Type or paste your sentence or review...", help="Enter the text you want to analyze the sentiment for.", label_visibility="visible",)

# Button to analyze sentiment
if st.button("Analyze Sentiment", key="analyze", help="Click to analyze the sentiment of the entered text."):
    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        # Analyze sentiment with TextBlob
        blob = TextBlob(user_input)
        polarity = blob.sentiment.polarity

        # Determine sentiment category
        if polarity > 0.1:
            sentiment = "Positive"
            css_class = "positive"
            emoji = "😊"
        elif polarity < -0.1:
            sentiment = "Negative"
            css_class = "negative"
            emoji = "☹️"
        else:
            sentiment = "Neutral"
            css_class = "neutral"
            emoji = "😐"

        # Display the result
        st.markdown(
            f'<div class="result-box {css_class}">{emoji} Sentiment: {sentiment} (Polarity: {polarity:.2f})</div>',
            unsafe_allow_html=True,
        )

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <footer>
        Created with ❤️ using Python &amp; TextBlob | Powered by Streamlit
    </footer>
    """,
    unsafe_allow_html=True,
)
