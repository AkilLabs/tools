import os
import streamlit as st
import google.generativeai as genai

# Configure the API key for Gemini
genai.configure(api_key='AIzaSyCN4gMQupf11HN0H0_3wnk3AHnuGO9mnbA')

# Page title and description
st.title("Landing Page Copy Generator")
st.write(
    "Generate compelling landing page copy in seconds! Input your product or service details, "
    "and we'll create persuasive copy that converts visitors into customers."
)

# Input form
with st.form("landing_page_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    
    with col1:
        business_name = st.text_input(
            "Business/Product Name:",
            placeholder="Enter your business or product name"
        )
        
        industry = st.selectbox(
            "Industry:",
            ["E-commerce", "SaaS", "Education", "Healthcare", "Real Estate", 
             "Technology", "Finance", "Fitness", "Other"]
        )
        
        target_audience = st.text_area(
            "Target Audience:",
            placeholder="Describe your ideal customer (age, interests, pain points, etc.)",
            height=100
        )
    
    with col2:
        main_features = st.text_area(
            "Key Features/Benefits:",
            placeholder="List the main features or benefits of your product/service",
            height=100
        )
        
        tone = st.selectbox(
            "Tone of Voice:",
            ["Professional", "Friendly", "Enthusiastic", "Authoritative", 
             "Innovative", "Empathetic"]
        )
        
        unique_selling_point = st.text_area(
            "Unique Selling Proposition:",
            placeholder="What makes your product/service unique?",
            height=100
        )
    
    # Advanced options in an expander
    with st.expander("Advanced Options"):
        sections = st.multiselect(
            "Select sections to generate:",
            ["Hero Section", "Features Section", "Benefits Section", 
             "Social Proof Section", "CTA Section", "FAQ Section"],
            default=["Hero Section", "Features Section", "CTA Section"]
        )
        
        include_stats = st.checkbox(
            "Include placeholder statistics/numbers", 
            value=True
        )
        
        cta_type = st.radio(
            "Call-to-Action Type:",
            ["Sign Up", "Learn More", "Get Started", "Buy Now", "Contact Us"]
        )
    
    submitted = st.form_submit_button("Generate Landing Page Copy")

if submitted:
    if not business_name or not target_audience or not main_features:
        st.error("Please fill in all required fields (Business Name, Target Audience, and Key Features)!")
    else:
        try:
            # Generate different sections based on user selection
            with st.spinner("Generating your landing page copy..."):
                generated_sections = {}
                
                for section in sections:
                    # Create section-specific prompts
                    if section == "Hero Section":
                        prompt = f"""Create a compelling hero section for a landing page with:
                        - An attention-grabbing headline
                        - A persuasive subheadline
                        - A brief value proposition
                        
                        Business: {business_name}
                        Industry: {industry}
                        Target Audience: {target_audience}
                        USP: {unique_selling_point}
                        Tone: {tone}
                        
                        Format the output with clear headings for each element."""
                    
                    elif section == "Features Section":
                        prompt = f"""Create a features section highlighting the main benefits of {business_name}.
                        Key Features: {main_features}
                        Tone: {tone}
                        Make it benefit-focused and scannable.
                        Include 3-4 compelling feature descriptions."""
                    
                    elif section == "Benefits Section":
                        prompt = f"""Create a benefits section that shows how {business_name} solves 
                        the target audience's problems.
                        Target Audience: {target_audience}
                        Main Benefits: {main_features}
                        Tone: {tone}
                        Include specific examples and outcomes."""
                    
                    elif section == "Social Proof Section":
                        prompt = f"""Generate placeholder testimonial content and social proof elements 
                        that would be relevant for {business_name} in the {industry} industry.
                        Include 2-3 testimonial examples and relevant statistics."""
                    
                    elif section == "CTA Section":
                        prompt = f"""Create a compelling call-to-action section for {business_name}
                        CTA Type: {cta_type}
                        Include:
                        - Main CTA heading
                        - Supporting text
                        - Button text
                        - Optional urgency element"""
                    
                    elif section == "FAQ Section":
                        prompt = f"""Generate 4-5 relevant FAQ questions and answers for {business_name}
                        based on the industry ({industry}) and target audience concerns ({target_audience}).
                        Make them specific and helpful."""
                    
                    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
                        prompt,
                        stream=True
                    )
                    generated_sections[section] = "".join(chunk.text for chunk in response)
            
            # Display the results
            st.success("Landing Page Copy Generated!")
            
            # Display each section with proper formatting
            for section, content in generated_sections.items():
                with st.expander(f"{section} (Click to expand)", expanded=True):
                    st.markdown(content)
            
            # Combine all sections for download
            all_content = "\n\n---\n\n".join(
                f"# {section}\n\n{content}" 
                for section, content in generated_sections.items()
            )
            
            # Add download buttons
            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download as Markdown",
                    data=all_content,
                    file_name="landing_page_copy.md",
                    mime="text/markdown"
                )
            with col2:
                st.download_button(
                    label="Download as Text",
                    data=all_content,
                    file_name="landing_page_copy.txt",
                    mime="text/plain"
                )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Add helpful tips in the sidebar
with st.sidebar:
    st.subheader("Tips for Better Results")
    st.markdown("""
    - Be specific about your target audience
    - List concrete benefits, not just features
    - Include numerical values where possible
    - Focus on what makes your offering unique
    - Consider your audience's pain points
    """)
    
    st.subheader("About Different Sections")
    st.markdown("""
    - **Hero Section**: First impression, main value proposition
    - **Features Section**: Key product/service capabilities
    - **Benefits Section**: How features help customers
    - **Social Proof**: Testimonials and trust indicators
    - **CTA Section**: Converting visitor interest to action
    - **FAQ Section**: Addressing common concerns
    """)