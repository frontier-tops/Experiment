import streamlit as st
import requests
import json
import os
# API endpoint and token
endpoint_url = os.getenv("ENDPOINT_URL")
api_token = os.getenv("API_TOKEN")
# Streamlit UI setup
st.title("Code Generation with Llama3 🦙")
st.write("Enter your coding requirement below:")

user_question = st.text_area("Your Question", placeholder="e.g., 'Generate Python code to sort a list of dictionaries by key.'")

if st.button("Generate Code"):
    if not user_question.strip():
        st.error("Please enter a question to generate code.")
    else:
        prompt = f"""Generate clear, concise, and well-commented Python code based on the following user request:\n\n'{user_question}'\n\nProvide only the code in a formatted Python code block."""

        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        payload = {
            "model": "meta/llama3-8b-instruct",
            "prompt": prompt,
            "max_tokens": 500,
            "temperature": 0.3,
            "top_p": 1.0,
            "n": 1,
            "stream": False,
        }

        with st.spinner("Generating code..."):
            response = requests.post(endpoint_url, headers=headers, data=json.dumps(payload), verify=False)

        if response.status_code == 200:
            response_data = response.json()
            completion_text = response_data.get("choices", [{}])[0].get("text", "").strip()
            st.success("✅ Code generated successfully!")
            st.code(completion_text, language="python")
        else:
            st.error(f"Request failed: {response.status_code} - {response.text}")

