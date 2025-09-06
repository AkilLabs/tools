
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    st.error("Google API key not found in .env file!")
else:
    genai.configure(api_key=GOOGLE_API_KEY)

st.set_page_config(page_title="AI Content Tools Hub", layout="wide")
st.title("🛠️ AI Content Tools Hub")
st.write("Select a tool from the sidebar to get started.")

# --- Tool Functions ---
def clickbait_tool():
    st.header("🎯 Clickbait Title Generator")
    topic = st.text_area("What's your content about?", placeholder="Describe your article, video, or content...", height=100)
    title_style = st.selectbox("Choose your clickbait style:", ["Number-based", "Question-based", "How-to", "Shocking"])
    target_audience = st.text_input("Target audience (optional)", placeholder="e.g., Parents, Gamers, Professionals")
    emotion = st.selectbox("Emotional appeal:", ["Curiosity", "Surprise", "Fear of Missing Out", "Excitement", "Controversy"])
    num_titles = st.number_input("Number of titles to generate:", min_value=1, max_value=10, value=3)
    with st.expander("Advanced Options"):
        include_emojis = st.checkbox("Include emojis", value=True)
        max_length = st.slider("Maximum title length", 30, 100, 60)
    if st.button("Generate Clickbait Titles! 🚀"):
        if topic.strip() == "":
            st.error("Please provide a topic to generate titles!")
        else:
            prompt = f"""Generate {num_titles} clickbait titles for the following content:\n\nTopic: {topic}\nStyle: {title_style}\nTarget Audience: {target_audience if target_audience else 'General'}\nEmotional Appeal: {emotion}\nMaximum Length: {max_length} characters\n\nThe titles should be:\n1. Attention-grabbing and impossible to ignore\n2. Create curiosity or emotional response\n3. Use power words and strong hooks\n4. Stay within {max_length} characters\n5. {'Include relevant emojis' if include_emojis else 'No emojis'}\n\nMake each title unique and compelling while maintaining credibility."""
            try:
                with st.spinner("Crafting irresistible titles..."):
                    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                    generated_text = "".join(chunk.text for chunk in response)
                    titles = [title.strip() for title in generated_text.split('\n') if title.strip()]
                st.success("Your clickbait titles are ready! 🎉")
                for i, title in enumerate(titles, 1):
                    st.markdown(f"**{i}. {title}**")
                all_titles = "\n\n".join(titles)
                st.download_button("Download All Titles 📥", all_titles, "clickbait_titles.txt", "text/plain")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def fb_headline_tool():
    st.header("Facebook Ad Headlines")
    product_description = st.text_area("Enter your product description:", placeholder="Describe your product here...", height=200)
    tone = st.selectbox("Select the tone for the headline:", ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"])
    num_outputs = st.number_input("Number of outputs:", min_value=1, max_value=10, value=1, step=1)
    if st.button("Generate Headlines"):
        if product_description.strip() == "":
            st.error("Please provide a product description to proceed!")
        else:
            prompt = f"Generate a single-line, attention-grabbing headline for the following product description, highlighting key features and benefits in a {tone} tone: {product_description}."
            try:
                with st.spinner("Generating headlines..."):
                    headlines = []
                    for _ in range(num_outputs):
                        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                        headlines.append("".join(chunk.text for chunk in response))
                st.success("Headlines Generated!")
                for i, desc in enumerate(headlines, 1):
                    st.markdown(f"**Version {i}:** {desc}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def fb_primary_tool():
    st.header("Facebook Ad Text Generator")
    product_description = st.text_area("Enter your product description:", placeholder="Describe your product here...", height=200)
    tone = st.selectbox("Select the tone for the ad text:", ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"])
    num_outputs = st.number_input("Number of outputs:", min_value=1, max_value=10, value=1, step=1)
    if st.button("Generate Ad Texts"):
        if product_description.strip() == "":
            st.error("Please provide a product description to proceed!")
        else:
            prompt = f"Generate a compelling, persuasive Facebook ad primary text in a single paragraph aimed at generating leads and sales. The text should capture attention, emphasize key benefits, and create urgency or excitement, encouraging immediate action and conversions. Product Description: {product_description}, Desired Tone: {tone}."
            try:
                with st.spinner("Generating ad texts..."):
                    ad_texts = []
                    for _ in range(num_outputs):
                        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                        ad_texts.append("".join(chunk.text for chunk in response))
                st.success("Ad Texts Generated!")
                for i, ad in enumerate(ad_texts, 1):
                    st.markdown(f"**Version {i}:** {ad}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def google_ad_headline_tool():
    st.header("Google Ad Headline Generator")
    product_description = st.text_area("Enter your product description:", placeholder="Describe your product here...", height=200)
    tone = st.selectbox("Select the tone for the headline:", ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"])
    num_outputs = st.number_input("Number of outputs:", min_value=1, max_value=10, value=1, step=1)
    if st.button("Generate Headlines"):
        if product_description.strip() == "":
            st.error("Please provide a product description to proceed!")
        else:
            prompt = f"Generate a single-line, attention-grabbing headline for the following product description, highlighting key features and benefits in a {tone} tone: {product_description}."
            try:
                with st.spinner("Generating headlines..."):
                    headlines = []
                    for _ in range(num_outputs):
                        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                        headlines.append("".join(chunk.text for chunk in response))
                st.success("Headlines Generated!")
                for i, desc in enumerate(headlines, 1):
                    st.markdown(f"**Version {i}:** {desc}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def google_ad_tool():
    st.header("Google Ad Description Generator")
    product_description = st.text_area("Enter your product description:", placeholder="Describe your product here...", height=200)
    tone = st.selectbox("Select the tone for the ad:", ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"])
    num_outputs = st.number_input("Number of outputs:", min_value=1, max_value=10, value=1, step=1)
    if st.button("Generate Descriptions"):
        if product_description.strip() == "":
            st.error("Please provide a product description to proceed!")
        else:
            prompt = f"""
            Enhance the following product description to make it engaging, polished, and appealing. Return only the enhanced description in a single paragraph.  \n\nProduct Description: {product_description}  \nDesired Tone: {tone}  \n\nMake it concise but impactful, highlighting key features and benefits.
            """
            try:
                with st.spinner("Generating descriptions..."):
                    descriptions = []
                    for _ in range(num_outputs):
                        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                        descriptions.append("".join(chunk.text for chunk in response))
                st.success("Descriptions Generated!")
                for i, desc in enumerate(descriptions, 1):
                    st.markdown(f"**Version {i}:** {desc}")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def landingpage_tool():
    st.header("Landing Page Copy Generator")
    business_name = st.text_input("Business/Product Name:", placeholder="Enter your business or product name")
    industry = st.selectbox("Industry:", ["E-commerce", "SaaS", "Education", "Healthcare", "Real Estate", "Technology", "Finance", "Fitness", "Other"])
    target_audience = st.text_area("Target Audience:", placeholder="Describe your ideal customer (age, interests, pain points, etc.)", height=100)
    main_features = st.text_area("Key Features/Benefits:", placeholder="List the main features or benefits of your product/service", height=100)
    tone = st.selectbox("Tone of Voice:", ["Professional", "Friendly", "Enthusiastic", "Authoritative", "Innovative", "Empathetic"])
    unique_selling_point = st.text_area("Unique Selling Proposition:", placeholder="What makes your product/service unique?", height=100)
    with st.expander("Advanced Options"):
        sections = st.multiselect("Select sections to generate:", ["Hero Section", "Features Section", "Benefits Section", "Social Proof Section", "CTA Section", "FAQ Section"], default=["Hero Section", "Features Section", "CTA Section"])
        include_stats = st.checkbox("Include placeholder statistics/numbers", value=True)
        cta_type = st.radio("Call-to-Action Type:", ["Sign Up", "Learn More", "Get Started", "Buy Now", "Contact Us"])
    if st.button("Generate Landing Page Copy"):
        if not business_name or not target_audience or not main_features:
            st.error("Please fill in all required fields (Business Name, Target Audience, and Key Features)!")
        else:
            try:
                with st.spinner("Generating your landing page copy..."):
                    generated_sections = {}
                    for section in sections:
                        prompt = f"""
                        Generate the {section} for a landing page.\n\nBusiness Name: {business_name}\nIndustry: {industry}\nTarget Audience: {target_audience}\nMain Features: {main_features}\nTone: {tone}\nUnique Selling Point: {unique_selling_point}\nInclude Stats: {'Yes' if include_stats else 'No'}\nCTA Type: {cta_type}\nSection: {section}
                        """
                        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                        generated_sections[section] = "".join(chunk.text for chunk in response)
                st.success("Landing Page Copy Generated!")
                for section, content in generated_sections.items():
                    with st.expander(f"{section} (Click to expand)", expanded=True):
                        st.markdown(content)
                all_content = "\n\n---\n\n".join(f"# {section}\n\n{content}" for section, content in generated_sections.items())
                st.download_button("Download as Markdown", all_content, "landing_page_copy.md", "text/markdown")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def paragraph_tool():
    st.header("Paragraph Writer")
    topic = st.text_area("Enter your topic or prompt:", placeholder="What would you like paragraphs about?", height=150)
    writing_style = st.selectbox("Select the writing style:", ["Academic", "Casual", "Creative", "Professional", "Descriptive"])
    paragraph_count = st.number_input("Number of paragraphs:", min_value=1, max_value=5, value=1, step=1)
    paragraph_length = st.select_slider("Paragraph length:", options=["Short", "Medium", "Long"], value="Medium")
    if st.button("Generate Paragraphs"):
        if topic.strip() == "":
            st.error("Please provide a topic or prompt to proceed!")
        else:
            prompt = f"Generate {paragraph_count} {paragraph_length.lower()}-length paragraph(s) in a {writing_style.lower()} style about the following topic: {topic}. Each paragraph should be well-structured, coherent, and flow naturally. Make sure to include relevant details and maintain consistency throughout the text."
            try:
                with st.spinner("Generating paragraphs..."):
                    paragraphs = []
                    for _ in range(paragraph_count):
                        response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                        paragraphs.append("".join(chunk.text for chunk in response))
                st.success("Paragraphs Generated!")
                for i, para in enumerate(paragraphs, 1):
                    st.markdown(f"**Paragraph {i}:**")
                    st.write(para)
                all_paragraphs = "\n\n".join(paragraphs)
                st.download_button("Download Paragraphs", all_paragraphs, "generated_paragraphs.txt", "text/plain")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def sentence_tool():
    st.header("Sentence Generator")
    sentence_type = st.selectbox("Sentence Type:", ["Simple", "Compound", "Complex", "Compound-Complex", "Random"])
    sentence_style = st.selectbox("Writing Style:", ["Formal", "Casual", "Creative", "Technical", "Poetic"])
    sentence_mood = st.selectbox("Sentence Mood:", ["Declarative", "Interrogative", "Exclamatory", "Imperative"])
    sentence_tense = st.selectbox("Tense:", ["Present", "Past", "Future", "Mixed"])
    topic = st.text_area("Topic or Keywords (optional):", placeholder="Enter specific words, themes, or topics you'd like included in the sentences...", height=100)
    num_sentences = st.number_input("Number of sentences to generate:", min_value=1, max_value=10, value=3)
    with st.expander("Advanced Options"):
        min_words = st.slider("Minimum words per sentence:", min_value=5, max_value=30, value=8)
        max_words = st.slider("Maximum words per sentence:", min_value=5, max_value=30, value=15)
        if min_words > max_words:
            st.warning("Minimum words should not exceed maximum words")
    if st.button("Generate Sentences"):
        if min_words > max_words:
            st.error("Please adjust the word limits - minimum should not exceed maximum!")
        else:
            base_prompt = f"Generate {num_sentences} unique {sentence_type.lower()} sentences in a {sentence_style.lower()} style using {sentence_mood.lower()} mood and {sentence_tense.lower()} tense. Each sentence should be between {min_words} and {max_words} words."
            if topic.strip():
                base_prompt += f" Include these themes or keywords where appropriate: {topic}"
            try:
                with st.spinner("Generating sentences..."):
                    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(base_prompt, stream=True)
                    generated_text = "".join(chunk.text for chunk in response)
                    sentences = [s.strip() for s in generated_text.split('\n') if s.strip()]
                st.success("Sentences Generated!")
                for i, sentence in enumerate(sentences, 1):
                    st.write(f"{i}. {sentence}")
                all_sentences = "\n".join(f"{i}. {s}" for i, s in enumerate(sentences, 1))
                st.download_button("Download All Sentences", all_sentences, "generated_sentences.txt", "text/plain")
            except Exception as e:
                st.error(f"An error occurred: {e}")

def slogan_tool():
    st.header("Slogan Generator")
    business_name = st.text_input("Business/Product Name:", placeholder="Enter your business or product name...")
    business_description = st.text_area("Business/Product Description:", placeholder="Describe what your business/product does, target audience, and key benefits...", height=150)
    industry = st.selectbox("Select your industry:", ["Technology", "Food & Beverage", "Fashion & Apparel", "Health & Wellness", "Education", "Entertainment", "Financial Services", "Real Estate", "Other"])
    tone = st.selectbox("Select the tone for your slogan:", ["Professional", "Playful", "Inspirational", "Bold", "Modern", "Traditional"])
    slogan_length = st.select_slider("Preferred slogan length:", options=["Very Short", "Short", "Medium", "Long"], value="Short")
    num_outputs = st.number_input("Number of slogans to generate:", min_value=1, max_value=10, value=3, step=1)
    if st.button("Generate Slogans"):
        if not business_name or not business_description:
            st.error("Please provide both business name and description to proceed!")
        else:
            prompt = f"""
            Create {num_outputs} unique and memorable slogans for the following business:\n\nBusiness Name: {business_name}\nIndustry: {industry}\nDescription: {business_description}\n\nRequirements:\n- Tone: {tone}\n- Length: {slogan_length}\n- Each slogan should be catchy and memorable\n- Focus on benefits or unique value propositions\n- Make it relevant to the target audience\n- Keep it simple and easy to remember\n\nReturn only the slogans, one per line, without any additional commentary.
            """
            try:
                with st.spinner("Generating creative slogans..."):
                    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt, stream=True)
                    slogans = "".join(chunk.text for chunk in response)
                    individual_slogans = [s.strip() for s in slogans.split('\n') if s.strip()]
                st.success("Slogans Generated!")
                for i, slogan in enumerate(individual_slogans, 1):
                    st.markdown(f"**{i}. {slogan}**")
                st.download_button("Download Slogans", slogans, "slogans.txt", "text/plain")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- Sidebar Navigation ---
tool = st.sidebar.selectbox(
    "Choose a tool:",
    [
        "Clickbait Title Generator",
        "Facebook Ad Headline",
        "Facebook Ad Text",
        "Google Ad Headline",
        "Google Ad Description",
        "Landing Page Copy",
        "Paragraph Writer",
        "Sentence Generator",
        "Slogan Generator"
    ]
)

if tool == "Clickbait Title Generator":
    clickbait_tool()
elif tool == "Facebook Ad Headline":
    fb_headline_tool()
elif tool == "Facebook Ad Text":
    fb_primary_tool()
elif tool == "Google Ad Headline":
    google_ad_headline_tool()
elif tool == "Google Ad Description":
    google_ad_tool()
elif tool == "Landing Page Copy":
    landingpage_tool()
elif tool == "Paragraph Writer":
    paragraph_tool()
elif tool == "Sentence Generator":
    sentence_tool()
elif tool == "Slogan Generator":
    slogan_tool()
