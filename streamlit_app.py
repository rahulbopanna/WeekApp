import streamlit as st
from langchain.chat_models import ChatOpenAI

# Streamlit setup
st.title("Airline Experience Feedback")

# Prompt for user input on trip experience
travel_experience = st.text_input("Please share your recent travel experience with us:")

# Initialize OpenAI client directly with API key from Streamlit secrets
chatbot = ChatOpenAI(openai_api_key=st.secrets["OpenAIKey"], model="gpt-4")

# Define the system prompt to classify and respond based on user feedback
if travel_experience:
    try:
        # Prepare messages for the model as a single input
        system_message = "Analyze the user's feedback on their recent airline experience and respond accordingly. " \
                         "If they had a positive experience, thank them for their feedback. " \
                         "If they had a negative experience caused by the airline, offer sympathies and state that customer service will follow up. " \
                         "If the negative experience was beyond the airline's control, express sympathy and explain that the airline is not liable."
        
        user_message = travel_experience
        
        # Get response from the chatbot
        response = chatbot([{"role": "system", "content": system_message}, 
                             {"role": "user", "content": user_message}])

        # Display the AI's response
        st.write(response['choices'][0]['message']['content'])

    except Exception as error:
        st.error(f"An error occurred while processing your feedback: {error}")
