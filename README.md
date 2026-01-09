This project implements a simple phishing email detection system using Natural Language Processing and a traditional machine learning approach. The model analyzes the email body text and classifies it as either phishing or legitimate. The focus of the project is to demonstrate that a lightweight and interpretable model can achieve strong performance without complex architectures.

The text is transformed using a TF-IDF vectorizer with a maximum of 5000 features, and classification is performed using Logistic Regression. With this setup, the system achieves an accuracy of 97.05% on the evaluation dataset. No email headers, URLs, or HTML structure are used in this version; the decision is based solely on the textual content of the email.

The project includes a Streamlit web application that allows the model to be used directly in a browser. By running the run_app.py file with Streamlit, users can paste an email message into the interface and instantly receive a phishing prediction. This makes the system easy to test, demonstrate, and extend.

This implementation is intended as a baseline solution and a starting point for further improvements, such as incorporating email headers, URL analysis, or more advanced language models.
