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
st.title("Sentence Generator")
st.write(
    "Generate sentences with the click of a button! Perfect for writing practice, "
    "examples, or creative inspiration. Customize the type, complexity, and style "
    "of sentences you need."
)

# Input form
with st.form("sentence_input_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    
    with col1:
        sentence_type = st.selectbox(
            "Sentence Type:",
            ["Simple", "Compound", "Complex", "Compound-Complex", "Random"]
        )
        
        sentence_style = st.selectbox(
            "Writing Style:",
            ["Formal", "Casual", "Creative", "Technical", "Poetic"]
        )
    
    with col2:
        sentence_mood = st.selectbox(
            "Sentence Mood:",
            ["Declarative", "Interrogative", "Exclamatory", "Imperative"]
        )
        
        sentence_tense = st.selectbox(
            "Tense:",
            ["Present", "Past", "Future", "Mixed"]
        )
    
    topic = st.text_area(
        "Topic or Keywords (optional):",
        placeholder="Enter specific words, themes, or topics you'd like included in the sentences...",
        height=100
    )
    
    num_sentences = st.number_input(
        "Number of sentences to generate:",
        min_value=1,
        max_value=10,
        value=3,
        help="Choose how many sentences you want to generate"
    )
    
    advanced_options = st.expander("Advanced Options")
    with advanced_options:
        min_words = st.slider(
            "Minimum words per sentence:",
            min_value=5,
            max_value=30,
            value=8
        )
        max_words = st.slider(
            "Maximum words per sentence:",
            min_value=5,
            max_value=30,
            value=15
        )
        
        if min_words > max_words:
            st.warning("Minimum words should not exceed maximum words")
    
    submitted = st.form_submit_button("Generate Sentences")

if submitted:
    if min_words > max_words:
        st.error("Please adjust the word limits - minimum should not exceed maximum!")
    else:
        # Create the prompt for generating sentences
        base_prompt = f"""Generate {num_sentences} unique {sentence_type.lower()} sentences 
        in a {sentence_style.lower()} style using {sentence_mood.lower()} mood and {sentence_tense.lower()} tense. 
        Each sentence should be between {min_words} and {max_words} words."""
        
        if topic.strip():
            base_prompt += f" Include these themes or keywords where appropriate: {topic}"
            
        try:
            # Generate sentences
            with st.spinner("Generating sentences..."):
                response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                    base_prompt,
                    stream=True
                )
                generated_text = "".join(chunk.text for chunk in response)
                
                # Split the response into sentences and clean them
                sentences = [s.strip() for s in generated_text.split('\n') if s.strip()]
            
            # Display the results
            st.success("Sentences Generated!")
            
            # Create tabs for different views
            tab1, tab2 = st.tabs(["Regular View", "Analysis View"])
            
            with tab1:
                for i, sentence in enumerate(sentences, 1):
                    st.write(f"{i}. {sentence}")
            
            with tab2:
                for i, sentence in enumerate(sentences, 1):
                    with st.expander(f"Sentence {i} Analysis"):
                        st.write("**Sentence:**", sentence)
                        st.write("**Word Count:**", len(sentence.split()))
                        st.write("**Character Count:**", len(sentence))
                
            # Add download option for all sentences
            all_sentences = "\n".join(f"{i}. {s}" for i, s in enumerate(sentences, 1))
            st.download_button(
                label="Download All Sentences",
                data=all_sentences,
                file_name="generated_sentences.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Add footer with helpful tips
st.markdown("---")
with st.expander("Tips for Better Results"):
    st.markdown("""
    - Use specific keywords in the topic field for more relevant sentences
    - Adjust word limits based on your needs
    - Try different combinations of sentence types and moods
    - For creative writing, try the 'Creative' style with 'Complex' sentence type
    - For formal documents, use 'Formal' style with 'Simple' or 'Compound' types
    """)