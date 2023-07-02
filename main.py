import pickle
import streamlit as st
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import string
import re

#function to preprocess the text data
def text_preproces(text):
    text = text.lower()

    # remmoving the punctuation from the data
    nonpunc = [char for char in text if char not in string.punctuation]
    nonpunc = ''.join(nonpunc)

    # apply the regex to reomvoe the number
    txt = re.sub('[0-9]', '', nonpunc)

    # removing the stopwords

    no_stopwords = [word for word in txt.split() if word not in stopwords.words('english')]

    return no_stopwords


#adding the background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

#Load the model

with open('pipe.pkl', 'rb') as f:
    model = pickle.load(f)
#model=pickle.load('pipe.pkl')

# Set the title of the web app
st.title('SMS SPAM Detection')

# Create an input text box
user_input = st.text_input("Enter a message")

# Create a button to trigger the prediction
if st.button('Predict'):
    if user_input:
        # Preprocess the user input
        processed_input = [user_input]

        # Make the prediction
        prediction = model.predict(processed_input)[0]

        # Display the prediction
        if prediction == 'ham':
            st.success('NOT SPAM')
        else:
            st.error('SPAM.')
    else:
        st.warning("Please enter a message.")
