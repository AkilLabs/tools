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
st.title("Paragraph Writer")
st.write(
    "Generate paragraphs with the click of a button! Provide a topic or prompt, "
    "and we'll create well-structured paragraphs for your needs."
)

# Input form
with st.form("paragraph_input_form", clear_on_submit=False):
    topic = st.text_area(
        "Enter your topic or prompt:",
        placeholder="What would you like paragraphs about?",
        height=150,
    )
    
    writing_style = st.selectbox(
        "Select the writing style:",
        ["Academic", "Casual", "Creative", "Professional", "Descriptive"]
    )
    
    paragraph_count = st.number_input(
        "Number of paragraphs:",
        min_value=1,
        max_value=5,
        value=1,
        step=1,
        help="Select how many paragraphs you want to generate."
    )
    
    paragraph_length = st.select_slider(
        "Paragraph length:",
        options=["Short", "Medium", "Long"],
        value="Medium",
        help="Choose the approximate length of each paragraph."
    )
    
    submitted = st.form_submit_button("Generate Paragraphs")

if submitted:
    if topic.strip() == "":
        st.error("Please provide a topic or prompt to proceed!")
    else:
        # Create the prompt for generating paragraphs
        prompt = f"""Generate {paragraph_count} {paragraph_length.lower()}-length paragraph(s) 
        in a {writing_style.lower()} style about the following topic: {topic}. 
        Each paragraph should be well-structured, coherent, and flow naturally. 
        Make sure to include relevant details and maintain consistency throughout the text."""
        
        try:
            # Generate paragraphs
            with st.spinner("Generating paragraphs..."):
                paragraphs = []
                for _ in range(paragraph_count):
                    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                        prompt,
                        stream=True
                    )
                    paragraphs.append("".join(chunk.text for chunk in response))
            
            # Display the results
            st.success("Paragraphs Generated!")
            st.subheader("Generated Paragraphs:")
            
            # Display each paragraph with spacing and formatting
            for i, para in enumerate(paragraphs, start=1):
                st.markdown(f"**Paragraph {i}:**")
                st.write(para)
                st.write("")  # Add spacing between paragraphs
                
            # Add a download button for the generated text
            all_paragraphs = "\n\n".join(paragraphs)
            st.download_button(
                label="Download Paragraphs",
                data=all_paragraphs,
                file_name="generated_paragraphs.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")