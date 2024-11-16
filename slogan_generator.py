import os
import streamlit as st
import google.generativeai as genai

# Configure the API key for Gemini
genai.configure(api_key='AIzaSyCadd13-EHegOxuzgVr_17N-HTTJWvlD-k')

# Page title and description
st.title("Slogan Generator")
st.write(
    "Create catchy and memorable slogans for your business or product! "
    "Provide some basic information, and we'll generate creative slogans that capture your brand's essence."
)

# Create the input form
with st.form("slogan_input_form", clear_on_submit=False):
    business_name = st.text_input(
        "Business/Product Name:",
        placeholder="Enter your business or product name..."
    )
    
    business_description = st.text_area(
        "Business/Product Description:",
        placeholder="Describe what your business/product does, target audience, and key benefits...",
        height=150
    )
    
    industry = st.selectbox(
        "Select your industry:",
        [
            "Technology", "Food & Beverage", "Fashion & Apparel", 
            "Health & Wellness", "Education", "Entertainment",
            "Financial Services", "Real Estate", "Other"
        ]
    )
    
    tone = st.selectbox(
        "Select the tone for your slogan:",
        ["Professional", "Playful", "Inspirational", "Bold", "Modern", "Traditional"]
    )
    
    slogan_length = st.select_slider(
        "Preferred slogan length:",
        options=["Very Short", "Short", "Medium", "Long"],
        value="Short"
    )
    
    num_outputs = st.number_input(
        "Number of slogans to generate:",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        help="Select how many different slogan options you want."
    )
    
    submitted = st.form_submit_button("Generate Slogans")

if submitted:
    if not business_name or not business_description:
        st.error("Please provide both business name and description to proceed!")
    else:
        # Create the prompt for generating slogans
        prompt = f"""
        Create {num_outputs} unique and memorable slogans for the following business:
        
        Business Name: {business_name}
        Industry: {industry}
        Description: {business_description}
        
        Requirements:
        - Tone: {tone}
        - Length: {slogan_length}
        - Each slogan should be catchy and memorable
        - Focus on benefits or unique value propositions
        - Make it relevant to the target audience
        - Keep it simple and easy to remember
        
        Return only the slogans, one per line, without any additional commentary.
        """
        
        try:
            # Generate slogans
            with st.spinner("Generating creative slogans..."):
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt, stream=True)
                
                # Process and display results
                st.success("Slogans Generated!")
                st.subheader("Your Custom Slogans:")
                
                # Split the response into individual slogans and display them
                slogans = [chunk.text for chunk in response]
                combined_slogans = "".join(slogans)
                individual_slogans = [s.strip() for s in combined_slogans.split('\n') if s.strip()]
                
                for i, slogan in enumerate(individual_slogans, 1):
                    with st.container():
                        st.markdown(f"**{i}. {slogan}**")
                        col1, col2 = st.columns([0.85, 0.15])
                        with col2:
                            if st.button("📋", key=f"copy_{i}"):
                                st.write("Copied!")
                                st.clipboard(slogan)
                
                st.divider()
                st.caption("Click the clipboard icon to copy any slogan you like!")
                
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")