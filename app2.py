import streamlit as st
import joblib
import string


def cleaner(x):
    return list(
        (''.join([a for a in x if a not in string.punctuation]))
        .lower()
        .split()
    )

# Load the chatbot model
model = joblib.load('New_chatbot_model.pkl')

# CSS styling for the heart shape
heart_style = """
<style>
.heart {
  color: red;
  font-size: 150px;
  line-height: 1;
  text-align: center;
  display: inline-block;
  transform: rotate(-45deg);
  -webkit-transform: rotate(-45deg);
  -moz-transform: rotate(-45deg);
  -ms-transform: rotate(-45deg);
  -o-transform: rotate(-45deg);
}
</style>
"""

# Render the heart shape
st.markdown(heart_style, unsafe_allow_html=True)
st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)

# Function to generate a response from the chatbot model
def generate_response(input_text):
    return model.predict([input_text])[0]

# Streamlit app
def main():
    # Set title and description
    st.title('Chatbot')
    st.write('Welcome to the chatbot!')

    # Chatbot interface
    form = st.form(key='chat_form')
    user_input = form.text_input('User Input', '')
    submit_button = form.form_submit_button('Send')

    if submit_button:
        # Generate response
        response = generate_response(user_input)

        # Display response
        st.text_area('Bot Response', response)

        if user_input.lower() == 'q':
            st.stop()

# Run the app
if __name__ == '__main__':
    main()