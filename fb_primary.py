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
st.title("Facebook Ad Text Generator")
st.write(
    "Create high-converting Facebook ad texts using AI! Provide a basic description, "
    "and we'll generate professional ad texts to boost leads and sales."
)

# Center-aligned input fields
with st.form("ad_input_form", clear_on_submit=False):
    product_description = st.text_area(
        "Enter your product description:",
        placeholder="Describe your product here...",
        height=200,
    )
    tone = st.selectbox(
        "Select the tone for the ad text:",
        ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"],
    )
    num_outputs = st.number_input(
        "Number of outputs:",
        min_value=1,
        max_value=10,
        value=1,
        step=1,
        help="Select the number of ad text versions you want."
    )
    submitted = st.form_submit_button("Generate Ad Texts")

if submitted:
    if product_description.strip() == "":
        st.error("Please provide a product description to proceed!")
    else:
        # Create the prompt for generating Facebook Ad texts
        prompt = f"Generate a compelling, persuasive Facebook ad primary text in a single paragraph aimed at generating leads and sales. The text should capture attention, emphasize key benefits, and create urgency or excitement, encouraging immediate action and conversions. Product Description: {product_description}, Desired Tone: {tone}."

        try:
            # Generate ad texts
            with st.spinner("Generating ad texts..."):
                ad_texts = []
                for _ in range(num_outputs):
                    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                        prompt, stream=True
                    )
                    ad_texts.append("".join(chunk.text for chunk in response))

            # Display the results
            st.success("Ad Texts Generated!")
            st.subheader("Generated Facebook Ad Texts:")
            for i, ad in enumerate(ad_texts, start=1):
                st.markdown(f"**Version {i}:**")
                st.write(ad)
        except Exception as e:
            st.error(f"An error occurred: {e}")
