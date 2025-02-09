# BLOGIFY
AI Blog & Image Generator

# Overview

This is a Streamlit-based web application that generates AI-written blogs and AI-generated images based on user input. The application utilizes the Hugging Face API to generate text using the Mistral-7B model and images using the Stable Diffusion model. This is totally experimental basis we just want to explore the AI side in this hackathon and learn about it

# Advantages

* Time-Saving: Quickly generates high-quality content without manual effort.

* Enhanced Creativity: AI-generated content provides new perspectives and ideas.

* Customizability: Users can tailor blogs based on job profiles and target audiences.

* Ease of Use: Simple and intuitive UI built using Streamlit.

* Automated Workflow: Reduces the need for manual content creation and image generation.

# Technologies Used

* *Python

* Streamlit

* Hugging Face API

* Requests

* PIL (Pillow) for image processing

# Installation

Install the required dependencies:

pip install streamlit requests pillow

Run the application:

streamlit run app.py

# Configuration

Update the Hugging Face API key in app.py:

HF_API_KEY = "your_hugging_face_api_key"

# Usage

* Enter the blog topic in the input field.

* Select the target audience (Researchers, Data Scientists, General Audience).

* Click on "Generate Blog" to get an AI-generated blog.

* Click on "Generate Image" to generate an AI-based image for the blog.

* API Endpoints Used

* Text Generation: Mistral-7B-Instruct-v0.3 (mistralai/Mistral-7B-Instruct-v0.3)

* Image Generation: Stable Diffusion v1.5 (runwayml/stable-diffusion-v1-5)

# Developed by Varnana Rajeev and Arpitha Bhandary



