# # import os
# # import streamlit as st
# # import google.generativeai as genai

# # # Configure the API key for Gemini
# # genai.configure(api_key='AIzaSyCN4gMQupf11HN0H0_3wnk3AHnuGO9mnbA')

# # # Title for the Streamlit app
# # st.title("Google Ads Generator")

# # # Inputs for product description and tone
# # st.sidebar.header("Input Parameters")
# # product_description = st.sidebar.text_area(
# #     "Product Description",
# #     placeholder="Describe your product here...",
# #     height=150
# # )
# # tone = st.sidebar.selectbox(
# #     "Select the tone for your ad",
# #     ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"]
# # )

# # # Button to generate the ad
# # if st.sidebar.button("Generate Ad"):
# #     if product_description.strip() == "":
# #         st.error("Please provide a product description to proceed!")
# #     else:
# #         # Create the prompt for generating the ad
# #         prompt = f"""
# #         Create a Google Ads description for the following product:

# #         Product Description: {product_description}
# #         Tone: {tone}

# #         Make it engaging and concise, focusing on the key features and benefits.
# #         """
# #         try:
# #             # Generate the ad using the Gemini model
# #             with st.spinner("Generating ad..."):
# #                 response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
# #                     prompt, stream=True
# #                 )
# #                 ad_content = "".join(chunk.text for chunk in response)
            
# #             # Display the generated ad
# #             st.success("Ad Generated!")
# #             st.subheader("Generated Google Ad:")
# #             st.write(ad_content)
# #         except Exception as e:
# #             st.error(f"An error occurred: {e}")

# # # Footer
# # st.sidebar.markdown("---")
# # st.sidebar.info("Powered by Google's Gemini API & Streamlit")



# import os
# import streamlit as st
# import google.generativeai as genai

# # Configure the API key for Gemini
# genai.configure(api_key='AIzaSyCN4gMQupf11HN0H0_3wnk3AHnuGO9mnbA')

# # Page title and description
# st.title("Product Description Enhancer")
# st.write(
#     "Enhance your product descriptions with AI! Provide a basic description, "
#     "and we'll turn it into a polished, professional version."
# )

# # Center-aligned input fields
# with st.form("product_input_form", clear_on_submit=False):
#     product_description = st.text_area(
#         "Enter your product description:",
#         placeholder="Describe your product here...",
#         height=200,
#     )
#     tone = st.selectbox(
#         "Select the tone for the enhanced description:",
#         ["Friendly", "Professional", "Exciting", "Playful", "Persuasive"],
#     )
#     submitted = st.form_submit_button("Enhance Description")

# if submitted:
#     if product_description.strip() == "":
#         st.error("Please provide a product description to proceed!")
#     else:
#         # Create the prompt for enhancing the description
#         prompt = f"""
#         Enhance the following product description to make it engaging, polished, and appealing. Return only the enhanced description in a single paragraph.  

#         Product Description: {product_description}  
#         Desired Tone: {tone}  

#         Make it concise but impactful, highlighting key features and benefits.
#         """
#         try:
#             # Generate enhanced description
#             with st.spinner("Enhancing description..."):
#                 response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
#                     prompt, stream=True
#                 )
#                 enhanced_description = "".join(chunk.text for chunk in response)
            
#             # Display the result
#             st.success("Description Enhanced!")
#             st.subheader("Enhanced Product Description:")
#             st.write(enhanced_description)
#         except Exception as e:
#             st.error(f"An error occurred: {e}")


import os
import streamlit as st
import google.generativeai as genai

# Configure the API key for Gemini
genai.configure(api_key='AIzaSyCN4gMQupf11HN0H0_3wnk3AHnuGO9mnbA')

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
        prompt = f"""
        Enhance the following product description to make it engaging, polished, and appealing. Return only the enhanced description in a single paragraph.  

        Product Description: {product_description}  
        Desired Tone: {tone}  

        Make it concise but impactful, highlighting key features and benefits.
        """
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
