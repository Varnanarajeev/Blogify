import streamlit as st
import requests
from io import BytesIO
from PIL import Image

# Hugging Face API Endpoints
HF_API_KEY = "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"  
TEXT_GEN_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"
IMAGE_GEN_MODEL ="runwayml/stable-diffusion-v1-5" 

# Function to Generate Blog using Mistral-7B
def get_mistral_response(topic, word_limit, job_profile):
    prompt = f"Write a blog for a {job_profile} job profile on the topic '{topic}' within {word_limit} words."

    headers = {"Authorization": f"Bearer {HF_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": int(word_limit), "temperature": 0.7, "top_p": 0.9}
    }

    try:
        response = requests.post(f"https://api-inference.huggingface.co/models/{TEXT_GEN_MODEL}", headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and len(result) > 0 and "generated_text" in result[0]:
            return result[0]["generated_text"]
        else:
            return "Error: Unexpected response format from API."

    except requests.exceptions.RequestException as e:
        return f"API Request Error: {str(e)}"


def generate_image(prompt):
    url = f"https://api-inference.huggingface.co/models/{IMAGE_GEN_MODEL}"
    headers = {"Content-Type": "application/json"}
    payload = {"inputs": prompt}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return Image.open(BytesIO(response.content))
    
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

# Streamlit UI Configuration
st.set_page_config(page_title="AI Blog & Image Generator", page_icon="📝", layout="centered")

st.title("📝 AI Blog & Image Generator")
st.subheader("Generate Blogs & Related Images Using AI")

# User Inputs
topic = st.text_input("Enter the Blog Topic", placeholder="E.g., The Future of AI")
col1, col2 = st.columns(2)

with col1:
    word_limit = st.text_input("Number of Words", "250")

with col2:
    job_profile = st.selectbox("Writing the blog for", ["Researchers", "Data Scientists", "General Audience"])

# Generate Blog Button
if st.button("Generate Blog"):
    if topic.strip():
        with st.spinner("Generating Blog... ⏳"):
            blog_content = get_mistral_response(topic, word_limit, job_profile)
            st.write(blog_content)
    else:
        st.warning("Please enter a valid blog topic!")

# Generate Image Button
st.subheader("Generate an AI Image for Your Blog")

if st.button("Generate Image"):
    if topic.strip():
        with st.spinner("Generating Image... ⏳"):
            image = generate_image(topic)
            if isinstance(image, Image.Image):
                st.image(image, caption="AI-Generated Image", use_column_width=True)
            else:
                st.error(image)  # Show error message
    else:
        st.warning("Please enter a valid blog topic!")
