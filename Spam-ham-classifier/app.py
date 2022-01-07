import streamlit as st
import pickle


def transform_text(text):
    text = text.lower()  # 1. lower case
    text = nltk.word_tokenize(text)  # 2. Tokenize

    y = []
    for i in text:
        if i.isalnum():  # 3. remove special characters
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:  # 4. stopwords and punctuation
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))  # 5. Stemming

    return " ".join(y)

tdidf = pickle.load(open('vectorizer.pkl'), rb)
model = pickle.load(open('model.pkl'), rb)

# Title
st.title("Email or Sms Spam Classifier")

# Input
input = st.text.input("Enter the text")

# 1. Data Preprocessing
transformed_input = (transform_text(input))

# 2. Vectorize the Data
vector_input = tdidf.transform([transformed_input])

# 3. Predict the label
result = model.predict(vector_input)[0]

# 4. Display the Result
if result == 1:
    st.header("Spam")
else:
    st.header("Not Spam")
