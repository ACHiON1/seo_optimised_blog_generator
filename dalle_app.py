import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"  # Replace with your actual API key

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="256x256",
    )
    image_url = response["data"][0]["url"]
    return image_url

def main():
    st.title("DPD publication Image Generator")

    # Get user input
    prompt = st.text_input("Enter a prompt for image generation:")

    # Generate and display the image
    if st.button("Generate Image"):
        with st.spinner("Generating image..."):
            image_url = generate_image(prompt)
            st.image(image_url, caption="Generated Image", use_column_width=True)

if __name__ == "__main__":
    main()
