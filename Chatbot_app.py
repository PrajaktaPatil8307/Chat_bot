import streamlit as st
import joblib
import string


def cleaner(x):
    return list(
        (''.join([a for a in x if a not in string.punctuation]))
        .lower()
        .split()
    )

model = joblib.load('New_chatbot_model.pkl')

# Function to get the chatbot response
def get_chatbot_response(question):
    question_vectorized = [question]
    return model.predict(question_vectorized)[0]

st.title('Chat with your Virtul Friend')
st.subheader('You can find the relation here')

# # Chat loop
# while True:
#     user_input = st.text_input('Enter a message')
#     if user_input.lower() == 'quit':
#         break
#     response = get_chatbot_response(user_input)
#     st.write("Chatbot:", response)

# Chat loop
while True:
    user_input = st.text_input('Enter a message')
    if user_input.lower() == 'quit':
        break
    response = get_chatbot_response(user_input)
    st.write("Chatbot:", response)