import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI

# Initialize ChatOpenAI with the API key
chatbot = ChatOpenAI(openai_api_key=st.secrets["OpenAIKey"], model="gpt-4o-mini")

# Streamlit App
st.title("RN Airline Experience Form")

# User feedback input
travel_experience = st.text_input("Please share your recent travel experience with us:", "")

# Template to classify feedback type
feedback_classification_template = """Classify the feedback into one of the following categories:
1. "service_issue" if the feedback is negative and specifically related to the services provided by the airline (e.g., lost luggage, poor cabin service, flight delays).
2. "external_factor" if the feedback is negative but due to reasons beyond the airline's control (e.g., weather disruptions, airport delays).
3. "positive_experience" if the feedback is positive.

# Classification chain
classification_prompt = PromptTemplate(input_variables=["feedback"], template=feedback_classification_template)
classification_chain = LLMChain(llm=chatbot, prompt=classification_prompt)

# Responses dictionary for managing responses
feedback_responses = {
    "service_issue": "We apologize for the inconvenience caused by our service. Our customer support team will reach out to you shortly.",
    "external_factor": "We're sorry for the difficulties caused by circumstances beyond our control. Thank you for your understanding.",
    "positive_experience": "Thank you for your positive feedback! We're delighted to hear you had a wonderful journey with us."
}

# Run the chain if user feedback is provided
if travel_experience:
    try:
        # Get classification result
        classification_result = classification_chain.run({"feedback": travel_experience})

        # Display the appropriate response based on classification without showing the classification result
        response_message = feedback_responses.get(classification_result, "Unexpected classification result: {}".format(classification_result))
        st.write(response_message)
        
    except Exception as error:
        st.error(f"An error occurred while processing your feedback: {error}")
