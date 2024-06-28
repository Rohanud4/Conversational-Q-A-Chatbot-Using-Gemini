import streamlit as st

# Set the page configuration at the beginning
st.set_page_config(page_title="Q&A Demo")

from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load all the environment variables
load_dotenv()

# Configure the generative AI client with the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("API key not found in environment variables.")
else:
    genai.configure(api_key=api_key)

# Function to load the correct model and get responses
model_name = "models/gemini-pro"
st.write(f"Using model: {model_name}")
model = genai.GenerativeModel(model_name)

def get_gemini_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None

# Initialize the Streamlit app
st.header("Gemini LLM Application")

input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit is clicked 
if submit:
    response = get_gemini_response(input_text)
    if response:
        st.subheader("The Response is")
        st.write(response)
