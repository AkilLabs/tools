import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Google API key not found in .env file!")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

# Page title and description
st.title("Product Description Enhancer")
st.write(
    "Enhance your product descriptions with AI! Provide a basic description, "
    "and we'll turn it into polished, professional versions."
)

# Center-aligned input fields
with st.form("product_input_form", clear_on_submit=False):
    product_description = st.text_area(
        "Enter your product description:",
        placeholder="Describe your product here...",
        height=200,
    )
    tone = st.selectbox(
        "Select the tone for the enhanced description:",
        ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"],
    )
    num_outputs = st.number_input(
        "Number of outputs:",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
        help="Select the number of enhanced descriptions you want."
    )
    submitted = st.form_submit_button("Enhance Description")

if submitted:
    if product_description.strip() == "":
        st.error("Please provide a product description to proceed!")
    else:
        # Create the prompt for enhancing the description
        prompt = f"Generate a single-line, attention-grabbing headline for the following product description, highlighting key features and benefits in a {tone} tone: {product_description}."


        try:
            # Generate enhanced descriptions
            with st.spinner("Enhancing description..."):
                enhanced_descriptions = []
                for _ in range(num_outputs):
                    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                        prompt, stream=True
                    )
                    enhanced_descriptions.append("".join(chunk.text for chunk in response))
            
            # Display the results
            st.success("Descriptions Enhanced!")
            st.subheader("Enhanced Product Descriptions:")
            for i, desc in enumerate(enhanced_descriptions, start=1):
                st.markdown(f"**Version {i}:**")
                st.write(desc)
        except Exception as e:
            st.error(f"An error occurred: {e}")
