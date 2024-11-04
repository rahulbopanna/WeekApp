import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

st.title("Airline Experience Feedback")

# Prompt for user input on trip experience
user_experience = st.text_input("Share with us your experience of the latest trip:")

# Initialize OpenAI client directly with API key from Streamlit secrets
llm = ChatOpenAI(openai_api_key=st.secrets["OpenAIKey"], model="gpt-4")

# Define the system prompt to classify and respond based on user feedback
if user_experience:
    # Use llm as a callable to get the response
    response = llm([
        {"role": "system", "content": "Analyze the user's feedback on their recent airline experience and respond accordingly. "
                                       "If they had a positive experience, thank them for their feedback. "
                                       "If they had a negative experience caused by the airline, offer sympathies and state that customer service will follow up. "
                                       "If the negative experience was beyond the airline's control, express sympathy and explain that the airline is not liable."},
        {"role": "user", "content": user_experience}
    ])

    # Display the AI's response
    st.write(response["choices"][0]["message"]["content"])
