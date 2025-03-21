import streamlit as st
import ollama

# Streamlit App layout
st.title("-----------GenAI Model-------------")

# Text Input for user to type the question
question = st.text_input("Ask a question:")

# Display a loading spinner when processing
if question:
    with st.spinner('Generating response...'):
        # Generate response from the model
        prompt = question
        
        stream = ollama.generate(
            model='llama3.2-vision',
            prompt=prompt,
            stream=True
        )

        # Create a placeholder for the response
        response_placeholder = st.empty()

        # Print the response in real-time
        response = ''
        for chunk in stream:
            response += chunk['response']
            response_placeholder.markdown(response) 