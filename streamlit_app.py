import streamlit as st
from langchain.chat_models import ChatOpenAI

# Streamlit setup
st.title("Airline Experience Feedback")

# Prompt for user input on trip experience
travel_experience = st.text_input("Please share your recent travel experience with us:")

# Initialize OpenAI client directly with API key from Streamlit secrets
chatbot = ChatOpenAI(openai_api_key=st.secrets["OpenAIKey"], model="gpt-4")

# Define the system prompt for user feedback analysis
if travel_experience:
    try:
        # Prepare the full prompt to send to the model
        full_prompt = (
            "Analyze the user's feedback on their recent airline experience and respond accordingly. "
            "If they had a positive experience, thank them for their feedback. "
            "If they had a negative experience caused by the airline, offer sympathies and state that customer service will follow up. "
            "If the negative experience was beyond the airline's control, express sympathy and explain that the airline is not liable.\n"
            f"User feedback: {travel_experience}"
        )

        # Get the response from the chatbot
        response = chatbot(full_prompt)

        # Display the AI's response
        st.write(response)

    except Exception as error:
        st.error(f"An error occurred while processing your feedback: {error}")
