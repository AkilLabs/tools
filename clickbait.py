import os
import streamlit as st
import google.generativeai as genai
import random

# Configure the API key for Gemini
genai.configure(api_key='AIzaSyCN4gMQupf11HN0H0_3wnk3AHnuGO9mnbA')

# Custom CSS for better styling
st.markdown("""
    <style>
    .title-card {
        background-color: #1E1E1E;
        color: #FFFFFF;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        border: 1px solid #333333;
    }
    .title-text {
        font-size: 1.1rem;
        margin: 0;
        color: #FFFFFF;
    }
    .copy-button {
        background-color: #4CAF50;
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 0.3rem;
        cursor: pointer;
    }
    </style>
""", unsafe_allow_html=True)

# Page title and description with eye-catching emoji
st.title("🎯 Clickbait Title Generator")
st.write(
    "Generate attention-grabbing titles that get clicks! Transform your content "
    "into irresistible headlines that make readers want to know more."
)

# Helper function for title patterns
def get_title_patterns():
    return {
        "Number-based": [
            "{number} {subject} That Will {action} Your {target}",
            "Top {number} {subject} You Won't Believe {action}",
            "{number} Secret {subject} {professionals} Don't Want You to Know"
        ],
        "Question-based": [
            "Why Are {subject} {action}? The Truth Will Shock You!",
            "Can This {subject} Really {action}? We Tested It!",
            "Is Your {subject} {action}? Here's What You Need to Know"
        ],
        "How-to": [
            "How to {action} Your {subject} in {timeframe}",
            "This {adjective} Trick Will {action} Your {subject} Instantly",
            "The Secret to {action} Your {subject} Like a Pro"
        ],
        "Shocking": [
            "You Won't Believe What This {subject} Did to {action}!",
            "Shocking: This {subject} {action} and Nobody Noticed",
            "The {subject} Industry Doesn't Want You to See This!"
        ]
    }

# Input form
with st.form("clickbait_input_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    
    with col1:
        topic = st.text_area(
            "What's your content about?",
            placeholder="Describe your article, video, or content...",
            height=100
        )
        
        title_style = st.selectbox(
            "Choose your clickbait style:",
            ["Number-based", "Question-based", "How-to", "Shocking"]
        )
    
    with col2:
        target_audience = st.text_input(
            "Target audience (optional)",
            placeholder="e.g., Parents, Gamers, Professionals"
        )
        
        emotion = st.selectbox(
            "Emotional appeal:",
            ["Curiosity", "Surprise", "Fear of Missing Out", "Excitement", "Controversy"]
        )
    
    num_titles = st.number_input(
        "Number of titles to generate:",
        min_value=1,
        max_value=10,
        value=3
    )
    
    advanced_options = st.expander("Advanced Options")
    with advanced_options:
        include_emojis = st.checkbox("Include emojis", value=True)
        max_length = st.slider("Maximum title length", 30, 100, 60)
    
    submitted = st.form_submit_button("Generate Clickbait Titles! 🚀")

if submitted:
    if topic.strip() == "":
        st.error("Please provide a topic to generate titles!")
    else:
        # Create the prompt for generating clickbait titles
        prompt = f"""Generate {num_titles} clickbait titles for the following content:
        
        Topic: {topic}
        Style: {title_style}
        Target Audience: {target_audience if target_audience else 'General'}
        Emotional Appeal: {emotion}
        Maximum Length: {max_length} characters
        
        The titles should be:
        1. Attention-grabbing and impossible to ignore
        2. Create curiosity or emotional response
        3. Use power words and strong hooks
        4. Stay within {max_length} characters
        5. {'Include relevant emojis' if include_emojis else 'No emojis'}
        
        Make each title unique and compelling while maintaining credibility."""
        
        try:
            # Generate titles
            with st.spinner("Crafting irresistible titles..."):
                response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                    prompt,
                    stream=True
                )
                generated_text = "".join(chunk.text for chunk in response)
                titles = [title.strip() for title in generated_text.split('\n') if title.strip()]
            
            # Display results
            st.success("Your clickbait titles are ready! 🎉")
            
            # Display titles in cards with copy buttons
            for i, title in enumerate(titles, 1):
                cols = st.columns([8, 2])
                with cols[0]:
                    st.markdown(f"""
                        <div class="title-card">
                            <p class="title-text">{title}</p>
                        </div>
                    """, unsafe_allow_html=True)
                with cols[1]:
                    if st.button(f"📋 Copy", key=f"copy_{i}", help=f"Copy title {i} to clipboard"):
                        st.toast(f"Title {i} copied to clipboard! 📋")
            
            # Add download option with styled button
            st.markdown("<br>", unsafe_allow_html=True)
            all_titles = "\n\n".join(titles)
            st.download_button(
                label="Download All Titles 📥",
                data=all_titles,
                file_name="clickbait_titles.txt",
                mime="text/plain",
                key="download_button",
                help="Download all generated titles as a text file"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Add tips section with styled cards
with st.expander("Tips for Better Clickbait Titles"):
    st.markdown("""
    <div style="background-color: #1E1E1E; padding: 1rem; border-radius: 0.5rem; margin-bottom: 1rem;">
        <h3 style="color: #FFFFFF;">📝 Tips for Writing Effective Clickbait:</h3>
        <ol style="color: #FFFFFF;">
            <li><strong>Use Numbers:</strong> Lists and statistics grab attention</li>
            <li><strong>Create Mystery:</strong> Don't reveal everything in the title</li>
            <li><strong>Use Power Words:</strong> "Secret", "Shocking", "Incredible", etc.</li>
            <li><strong>Add Urgency:</strong> Make readers feel they need to click now</li>
            <li><strong>Target Emotions:</strong> Curiosity, surprise, or fear of missing out</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)