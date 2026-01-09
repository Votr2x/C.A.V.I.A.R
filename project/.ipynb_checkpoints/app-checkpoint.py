import streamlit as st
import pickle

@st.cache_resource
def load_model():
    with open('vectorizer.pkl', 'rb') as f:
        vectorizer = pickle.load(f)
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    return vectorizer, model

vectorizer, model = load_model()

st.markdown("""
    <style>
    * {
        font-family: 'Garamond', 'Times New Roman', serif !important;
    }
    
    html, body, [class*="css"], p, span, div, label, input, textarea, button {
        font-family: 'Garamond', 'Times New Roman', serif !important;
    }
    
    h1 {
        text-align: center;
        font-family: 'Garamond', 'Times New Roman', serif !important;
    }
    
    .stButton > button {
        display: block;
        margin: 0 auto;
    }
    
    .stTextArea label, .stTextArea textarea {
        font-family: 'Garamond', 'Times New Roman', serif !important;
    }
    </style>
    """, unsafe_allow_html=True)


st.title("Phishing Email Detector")

if 'email_text' not in st.session_state:
    st.session_state.email_text = ""


email_text = st.text_area("Paste your email content:", value=st.session_state.email_text, height=200, placeholder="Paste email text here...")


col1, col2, col3 = st.columns([2, 1, 2])
with col2:
    search_button = st.button("Search")


if search_button:
    if email_text.strip():
        st.session_state.email_text = email_text
        
        email_clean = email_text.lower().strip()
        
        email_tfidf = vectorizer.transform([email_clean])
        prediction = model.predict(email_tfidf)[0]
        probabilities = model.predict_proba(email_tfidf)[0]
        
        st.subheader("Results:")
        
        if prediction == 1:
            st.error("Prediction: **Phishing**")
        else:
            st.success("Prediction: **Safe**")
        
        # Show confidence scores (simplified format)
        st.write(f"**Safe:** {probabilities[0]*100:.2f}%")
        st.write(f"**Phishing:** {probabilities[1]*100:.2f}%")
        
        # Show reset button only after prediction
        col_reset1, col_reset2, col_reset3 = st.columns([2, 1, 2])
        with col_reset2:
            if st.button("Reset"):
                st.session_state.email_text = ""
                st.rerun()
    else:
        st.warning("Please enter some email text to analyze.")